from tdxApi.base.constant import *

class CatsMdApi:
    def __init__(self, gateway):
        self.gateway = gateway                  # gateway对象
        self.gatewayName = gateway.gatewayName  # gateway对象名称
        
        self.connectionStatus = False       # 连接状态
        
        self.subscribedSymbols = set()      # 已订阅合约代码        
        
        self.address = EMPTY_STRING         # 服务器地址
        self.port = EMPTY_INT               # 服务器端口
    
    def onDepthMarketData(self, data):
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

    def connect(self, userID, password, clientID, address, port):
        self.address = address              # 服务器地址
        self.port = port                    # 端口号
    
    def close(self):
        self.exit()