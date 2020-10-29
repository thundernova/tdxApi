from tdxApi.base.constant import *

class TdxTdApi:
    def __init__(self, gateway):
        """API对象的初始化函数"""
        super(XtpTdApi, self).__init__()
        
        self.gateway = gateway                  # gateway对象
        self.gatewayName = gateway.gatewayName  # gateway对象名称
        
        self.reqID = EMPTY_INT              # 操作请求编号
        
        self.connectionStatus = False       # 连接状态
        self.loginStatus = False            # 登录状态
        
        self.userID = EMPTY_STRING          # 账号
        self.password = EMPTY_STRING        # 密码
        self.address = EMPTY_STRING         # 服务器地址
        self.port = EMPTY_INT               # 服务器端口
        self.clientID = EMPTY_INT           # 客户编号
        
        self.sessionID = EMPTY_INT          # 会话编号
        
        self.orderDict = {}                 # 委托缓存字典

    #----------------------------------------------------------------------
    def onDisconnected(self, session, reason):
        """连接断开"""
        self.connectionStatus = False
        self.loginStatus = False
        self.gateway.tdConnected = False
    
        content = (u'交易服务器连接断开，原因：%s' %reason)
        self.writeLog(content)
        
        # 发起重新连接
        n = self.login(self.address, self.port, self.userID, self.password, 1)
        
        if n:
            self.sessionID = n
            self.connectionStatus = True
            self.loginStatus = True
            self.gateway.tdConnected = True
            self.writeLog(u'交易服务器登录成功，会话编号：%s' %n)
        else:
            self.writeLog(u'交易服务器登录失败')                     
        
    #----------------------------------------------------------------------
    def onError(self, data):
        """错误回报"""
        err = VtErrorData()
        err.gatewayName = self.gatewayName
        err.errorID = error['error_id']
        err.errorMsg = error['error_msg'].decode('gbk')
        self.gateway.onError(err)    
        
    #----------------------------------------------------------------------
    def onOrderEvent(self, data, error, session):
        """委托数据回报"""
        orderID = str(data['order_xtp_id'])
        
        if orderID not in self.orderDict:
            # 创建报单数据对象
            order = VtOrderData()
            order.gatewayName = self.gatewayName
            
            # 保存代码和报单号
            order.symbol = data['ticker']
            order.exchange = marketMapReverse.get(data['market'], EXCHANGE_UNKNOWN)
            order.vtSymbol = '.'.join([order.symbol, order.exchange])
            
            order.orderID = orderID
            order.vtOrderID = '.'.join([self.gatewayName, order.orderID])
    
            order.sessionID = self.sessionID
            order.frontID = self.getClientIDByXTPID(data['order_xtp_id'])
    
            # 开平和方向
            order.direction, order.offset = sideMapReverse.get(data['side'], 
                                                               (DIRECTION_UNKNOWN, OFFSET_UNKNOWN))
            
            # 不变的字段
            order.price = data['price']
            order.totalVolume = data['quantity']    
            order.priceType = priceTypeMapReverse.get(data['price_type'], '')
            
            self.orderDict[orderID] = order
        else:
            order = self.orderDict[orderID]
            
        # 变化字段
        order.status = statusMapReverse.get(data['order_status'], STATUS_UNKNOWN)
        order.tradedVolume = data['qty_traded']
        
        if data['insert_time']:
            timestamp = str(data['insert_time'])
            order.orderTime = '%s:%s:%s' %(timestamp[8:10], timestamp[10:12], timestamp[12:14])

        if data['cancel_time']:
            timestamp = str(data['cancel_time'])
            order.cancelTime = '%s:%s:%s' %(timestamp[8:10], timestamp[10:12], timestamp[12:14])
            
        # 推送
        self.gateway.onOrder(order)        
        
        # 错误信息
        if error['error_id']:
            err = VtErrorData()
            err.gatewayName = self.gatewayName
            err.errorID = error['error_id']
            err.errorMsg = u'委托号' + str(order.orderID) + ':' + error['error_msg'].decode('gbk')
            err.errorTime = order.orderTime
            self.gateway.onError(err)           
        
    #----------------------------------------------------------------------
    def onTradeEvent(self, data, session):
        """成交推送"""
        # 创建报单数据对象
        trade = VtTradeData()
        trade.gatewayName = self.gatewayName
        
        # 保存代码和报单号
        trade.symbol = data['ticker']
        trade.exchange = marketMapReverse.get(data['market'], EXCHANGE_UNKNOWN)
        trade.vtSymbol = '.'.join([trade.symbol, trade.exchange])
        
        trade.tradeID = str(data['exec_id'])
        trade.vtTradeID = '.'.join([self.gatewayName, trade.tradeID])
        
        orderID = str(data['order_xtp_id'])
        trade.orderID = orderID
        trade.vtOrderID = '.'.join([self.gatewayName, trade.orderID])
        
        # 开平和方向
        trade.direction, trade.offset = sideMapReverse.get(data['side'], 
                                                           (DIRECTION_UNKNOWN, OFFSET_UNKNOWN))
            
        # 价格、报单量等数值
        trade.price = data['price']
        trade.volume = data['quantity']

        if data['trade_time']:
            timestamp = str(data['trade_time'])
            trade.tradeTime = '%s:%s:%s' %(timestamp[8:10], timestamp[10:12], timestamp[12:14])
        
        # 推送
        self.gateway.onTrade(trade)
        
        # 更新委托数据
        order = self.orderDict.get(orderID, None)
        if (not order or 
            order.status is STATUS_ALLTRADED or
            order.status is STATUS_CANCELLED):
            return
            
        order.tradedVolume += trade.volume
        
        if order.status is STATUS_NOTTRADED:
            order.status = STATUS_PARTTRADED
            
        self.gateway.onOrder(order)
        
    #----------------------------------------------------------------------
    def onCancelOrderError(self, data, error, session):
        """撤单错误回报"""
        if error['error_id']:
            err = VtErrorData()
            err.gatewayName = self.gatewayName
            err.errorID = error['error_id']
            err.errorMsg = u'委托号' + str(data['order_xtp_id']) + ':' + error['error_msg'].decode('gbk')
            self.gateway.onError(err)   
        
    #----------------------------------------------------------------------
    def onQueryOrder(self, data, error, reqid, last, session):
        """委托查询回报"""
        pass
        
    #----------------------------------------------------------------------
    def onQueryTrade(self, data, error, reqid, last, session):
        """成交查询回报"""
        pass       
        
    #----------------------------------------------------------------------
    def onQueryPosition(self, data, error, reqid, last, session):
        """查询持仓回报"""
        pos = VtPositionData()
        pos.gatewayName = self.gatewayName
        
        # 保存代码
        pos.symbol = data['ticker']
        pos.exchange = marketMapReverse.get(data['market'], EXCHANGE_UNKNOWN)
        pos.vtSymbol = '.'.join([pos.symbol, pos.exchange])
        pos.name = data['ticker_name'].decode('UTF-8')
        
        # 方向和持仓冻结数量
        pos.direction = DIRECTION_LONG
        pos.position = data['total_qty']
        pos.frozen = data['total_qty'] - data['sellable_qty']
        pos.price = data['avg_price']
        
        # VT系统持仓名
        pos.vtPositionName = '.'.join([pos.vtSymbol, pos.direction])
        
        # 推送
        self.gateway.onPosition(pos)     
        
    #----------------------------------------------------------------------
    def onQueryAsset(self, data, error, reqid, last, session):
        """账户查询回报"""
        account = VtAccountData()
        account.gatewayName = self.gatewayName
    
        # 账户代码
        account.accountID = self.userID
        account.vtAccountID = '.'.join([self.gatewayName, account.accountID])
    
        # 数值相关
        account.balance = float(data['total_asset'])
        account.available = float(data['buying_power'])
        account.commission = float(data['fund_buy_fee']) + float(data['fund_sell_fee'])
    
        # 推送
        self.gateway.onAccount(account)
    
    #----------------------------------------------------------------------
    def onQueryStructuredFund(self, data, error, reqid, last, session):
        """"""
        pass
        
    #----------------------------------------------------------------------
    def onQueryFundTransfer(self, data, error, reqid, last, session):
        """"""
        pass
        
    #----------------------------------------------------------------------
    def onFundTransfer(self, data, error, session):
        """"""
        pass
        
    #----------------------------------------------------------------------
    def onQueryETF(self, data, error, reqid, last, session):
        """"""
        pass
        
    #----------------------------------------------------------------------
    def onQueryETFBasket(self, data, error, reqid, last, session):
        """"""
        pass
        
    #----------------------------------------------------------------------
    def onQueryIPOInfoList(self, data, error, reqid, last, session):
        """"""
        pass
        
    #----------------------------------------------------------------------
    def onQueryIPOQuotaInfo(self, data, error, reqid, last, session):
        """"""
        pass
           
    #----------------------------------------------------------------------
    def connect(self, userID, password, clientID, softwareKey, address, port):
        """初始化连接"""
        self.userID = userID                # 账号
        self.password = password            # 密码
        self.address = address              # 服务器地址
        self.port = port                    # 端口号
        self.clientID = clientID
        
        # 如果尚未建立服务器连接，则进行连接
        if not self.connectionStatus:
            path = os.getcwd() + '/temp/' + self.gatewayName + '/'
            if not os.path.exists(path):
                os.makedirs(path)
            self.createTraderApi(clientID, path)
            
            # 设置软件编码，认证用
            self.setSoftwareKey(softwareKey)
            
            # 设置订单和成交回报重传模式
            self.subscribePublicTopic(0)
            
            # 发起登录
            n = self.login(address, port, userID, password, 1)
            
            if n:
                self.sessionID = n
                self.connectionStatus = True
                self.loginStatus = True
                self.gateway.tdConnected = True
                self.writeLog(u'交易服务器登录成功，会话编号：%s' %n)
            else:
                self.writeLog(u'交易服务器登录失败')             
        
    #----------------------------------------------------------------------
    def qryAccount(self):
        """查询账户"""
        if self.sessionID:
            self.reqID += 1
            self.queryAsset(self.sessionID, self.reqID)
        
    #----------------------------------------------------------------------
    def qryPosition(self):
        """查询持仓"""
        if self.sessionID:
            self.reqID += 1
            self.queryPosition('', self.sessionID, self.reqID)
        
    #----------------------------------------------------------------------
    def sendOrder(self, orderReq):
        """发单"""
        req = {}
        req['ticker'] = orderReq.symbol
        req['price'] = orderReq.price
        req['quantity'] = orderReq.volume
        req['price_type'] = priceTypeMap.get(orderReq.priceType, 0)
        req['market'] = marketMap.get(orderReq.exchange, 0)
        req['business_type'] = 0        # 目前只支持买卖业务

        # 目前尚未支持衍生品交易，因此不适用
        #req['side'] = sideMap.get((orderReq.direction, OFFSET_NONE), 0)
        if orderReq.direction == DIRECTION_LONG:
            req['side'] = 1
        else:
            req['side'] = 2

        # 发出委托
        orderID = str(self.insertOrder(req, self.sessionID))        
        vtOrderID = '.'.join([self.gatewayName, orderID])

        # 返回订单号（字符串），便于某些算法进行动态管理
        return vtOrderID
    
    #----------------------------------------------------------------------
    def sendCancel(self, cancelOrderReq):
        """撤单，因为cancelOrder的命名已经被原生接口使用了，所以改为sendCancel"""
        self.cancelOrder(int(cancelOrderReq.orderID), self.sessionID)
        
    #----------------------------------------------------------------------
    def close(self):
        """关闭"""
        self.exit()