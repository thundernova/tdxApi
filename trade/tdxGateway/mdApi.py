from tdxApi.base.constant import *

class TdxMdApi:
    def __init__(self, gateway):
        self.gateway = gateway                  # gateway对象
        self.gatewayName = gateway.gatewayName  # gateway对象名称
        
        self.reqID = EMPTY_INT              # 操作请求编号
        
        self.connectionStatus = False       # 连接状态
        self.loginStatus = False            # 登录状态
        
        self.subscribedSymbols = set()      # 已订阅合约代码        
        
        self.userID = EMPTY_STRING          # 账号
        self.password = EMPTY_STRING        # 密码
        self.address = EMPTY_STRING         # 服务器地址
        self.port = EMPTY_INT               # 服务器端口
    
    #----------------------------------------------------------------------
    def onDisconnected(self, reason):
        """连接断开"""
        self.connectionStatus = False
        self.loginStatus = False
        self.gateway.mdConnected = False
    
        content = (u'行情服务器连接断开，原因：%s' %reason)
        self.writeLog(content)
        
        # 重新连接
        n = self.login(self.address, self.port, self.userID, self.password, 1)
        if not n:
            self.connectionStatus = True
            self.loginStatus = True
            self.gateway.mdConnected = True
            self.writeLog(u'行情服务器登录成功')
        else:
            self.writeLog(u'行情服务器登录失败，原因:%s' %n)        
        
    #----------------------------------------------------------------------
    def onError(self, error):
        """错误回报"""
        err = VtErrorData()
        err.gatewayName = self.gatewayName
        err.errorID = error['error_id']
        err.errorMsg = error['error_msg'].decode('gbk')
        self.gateway.onError(err)        
        
    #----------------------------------------------------------------------
    def onSubMarketData(self, data, error, last):
        """订阅行情回报"""
        pass
        
    #----------------------------------------------------------------------
    def onUnSubMarketData(self, data, error, last):
        """退订行情回报"""
        pass
        
    #----------------------------------------------------------------------
    def onDepthMarketData(self, data):
        """行情推送"""
        tick = VtTickData()
        tick.gatewayName = self.gatewayName
    
        tick.symbol = data['ticker']
        tick.exchange = exchangeMapReverse.get(data['exchange_id'], EXCHANGE_UNKNOWN)
        tick.vtSymbol = '.'.join([tick.symbol, tick.exchange])
    
        tick.lastPrice = data['last_price']
        tick.volume = data['qty']
        tick.openInterest = data['open_interest']

        timestamp = str(data['data_time'])
        tick.date = timestamp[:8]
        tick.time = '%s:%s:%s.%s' %(timestamp[8:10], timestamp[10:12], timestamp[12:14], timestamp[14])
        
        tick.openPrice = data['open_price']
        tick.highPrice = data['high_price']
        tick.lowPrice = data['low_price']
        tick.preClosePrice = data['pre_close_price']
    
        tick.upperLimit = data['upper_limit_price']
        tick.lowerLimit = data['lower_limit_price']
        
        tick.bidPrice1, tick.bidPrice2, tick.bidPrice3, tick.bidPrice4, tick.bidPrice5 = data['bid'][0:5]
        tick.askPrice1, tick.askPrice2, tick.askPrice3, tick.askPrice4, tick.askPrice5 = data['ask'][0:5]
        tick.bidVolume1, tick.bidVolume2, tick.bidVolume3, tick.bidVolume4, tick.bidVolume5 = data['bid_qty'][0:5]
        tick.askVolume1, tick.askVolume2, tick.askVolume3, tick.askVolume4, tick.askVolume5 = data['ask_qty'][0:5]  
    
        self.gateway.onTick(tick)        
        
    #----------------------------------------------------------------------
    def onQueryAllTickers(self, data, error, last):
        """合约信息推送"""
        if error and error['error_id']:
            err = VtErrorData()
            err.gatewayName = self.gatewayName
            err.errorID = error['error_id']
            err.errorMsg = error['error_msg'].decode('gbk')
            self.gateway.onError(err)
            return
        
        contract = VtContractData()
        contract.gatewayName = self.gatewayName
        
        contract.symbol = data['ticker']
        contract.exchange = exchangeMapReverse.get(data['exchange_id'], EXCHANGE_UNKNOWN)
        contract.vtSymbol = '.'.join([contract.symbol, contract.exchange])
        
        contract.name = data['ticker_name'].decode('UTF-8')
        contract.size = 1
        contract.priceTick = data['price_tick']
        contract.productClass = productClassMapReverse.get(data['ticker_type'], PRODUCT_UNKNOWN)
        
        self.gateway.onContract(contract)
        
    #----------------------------------------------------------------------
    def onSubOrderBook(self, data, error, last):
        """"""
        pass
        
    #----------------------------------------------------------------------
    def onUnSubOrderBook(self, data, error, last):
        """"""
        pass
        
    #----------------------------------------------------------------------
    def onOrderBook(self, data):
        """"""
        pass
        
    #----------------------------------------------------------------------
    def onSubTickByTick(self, data, error, last):
        """"""
        pass
        
    #----------------------------------------------------------------------
    def onUnSubTickByTick(self, data, error, last):
        """"""
        pass
        
    #----------------------------------------------------------------------
    def onTickByTick(self, data):
        """"""
        pass
        
    #----------------------------------------------------------------------
    def onSubscribeAllMarketData(self, error):
        """"""
        pass
        
    #----------------------------------------------------------------------
    def onUnSubscribeAllMarketData(self, error):
        """"""
        pass
        
    #----------------------------------------------------------------------
    def onSubscribeAllOrderBook(self, error):
        """"""
        pass
        
    #----------------------------------------------------------------------
    def onUnSubscribeAllOrderBook(self, error):
        """"""
        pass
        
    #----------------------------------------------------------------------
    def onSubscribeAllTickByTick(self, error):
        """"""
        pass
        
    #----------------------------------------------------------------------
    def onUnSubscribeAllTickByTick(self, error):
        """"""
        pass
        
    #----------------------------------------------------------------------
    def onQueryTickersPriceInfo(self, data, error, last):
        """"""
        pass

    #----------------------------------------------------------------------
    def connect(self, userID, password, clientID, address, port):
        """初始化连接"""
        self.userID = userID                # 账号
        self.password = password            # 密码
        self.address = address              # 服务器地址
        self.port = port                    # 端口号
        
        # 如果尚未建立服务器连接，则进行连接
        if not self.connectionStatus:
            path = os.getcwd() + '/temp/' + self.gatewayName + '/'
            if not os.path.exists(path):
                os.makedirs(path)
            self.createQuoteApi(clientID, path)
            
            n = self.login(address, port, userID, password, 1)
            if not n:
                self.connectionStatus = True
                self.loginStatus = True
                self.gateway.mdConnected = True
                self.writeLog(u'行情服务器登录成功')
                
                self.writeLog(u'查询合约信息')
                self.queryAllTickers(1)         # 上交所
                self.queryAllTickers(2)         # 深交所
            else:
                self.writeLog(u'行情服务器登录失败，原因:%s' %n)
        
    #----------------------------------------------------------------------
    def subscribe(self, subscribeReq):
        """订阅合约"""
        # 这里的设计是，如果尚未登录就调用了订阅方法
        # 则先保存订阅请求，登录完成后会自动订阅
        if self.loginStatus:
            self.subscribeMarketData(str(subscribeReq.symbol), 
                                     exchangeMap[subscribeReq.exchange])
        
        self.subscribedSymbols.add(subscribeReq)   
        
    #----------------------------------------------------------------------
    def unSubscribe(self, subscribeReq):
        """"""
        if self.loginStatus:
            self.unSubscribeMarketData(str(subscribeReq.symbol), 
                                       exchangeMap[subscribeReq.exchange])
    
    #----------------------------------------------------------------------
    def close(self):
        """关闭"""
        self.exit()