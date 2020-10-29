from tdxApi.base.constant import *

class TickData:
    def __init__(self):
        self.symbol = EMPTY_STRING
        self.exchange = EMPTY_STRING

        self.time = EMPTY_STRING
        self.last = EMPTY_FLOAT
        self.last_vol = EMPTY_INT
        self.total_vol = EMPTY_INT
        
        self.bidPrice1 = EMPTY_FLOAT
        self.bidPrice2 = EMPTY_FLOAT
        self.bidPrice3 = EMPTY_FLOAT
        self.bidPrice4 = EMPTY_FLOAT
        self.bidPrice5 = EMPTY_FLOAT
        
        self.askPrice1 = EMPTY_FLOAT
        self.askPrice2 = EMPTY_FLOAT
        self.askPrice3 = EMPTY_FLOAT
        self.askPrice4 = EMPTY_FLOAT
        self.askPrice5 = EMPTY_FLOAT        
        
        self.bidVolume1 = EMPTY_INT
        self.bidVolume2 = EMPTY_INT
        self.bidVolume3 = EMPTY_INT
        self.bidVolume4 = EMPTY_INT
        self.bidVolume5 = EMPTY_INT
        
        self.askVolume1 = EMPTY_INT
        self.askVolume2 = EMPTY_INT
        self.askVolume3 = EMPTY_INT
        self.askVolume4 = EMPTY_INT
        self.askVolume5 = EMPTY_INT


class BarData:
    def __init__(self):
        self.symbol = EMPTY_STRING
        self.exchange = EMPTY_STRING

        self.time = None
        self.open = EMPTY_FLOAT
        self.high = EMPTY_FLOAT
        self.low = EMPTY_FLOAT
        self.close = EMPTY_FLOAT
        self.vol = EMPTY_INT
        self.interval = EMPTY_UNICODE


class OrderData:
    def __init__(self):
        self.symbol = EMPTY_STRING              
        self.exchange = EMPTY_STRING            
        self.vtSymbol = EMPTY_STRING  
        
        self.orderID = EMPTY_STRING            
        self.vtOrderID = EMPTY_STRING 
        
        self.direction = EMPTY_UNICODE     
        self.offset = EMPTY_UNICODE             
        self.price = EMPTY_FLOAT              
        self.totalVolume = EMPTY_INT            
        self.tradedVolume = EMPTY_INT          
        self.status = EMPTY_UNICODE            
        
        self.orderTime = EMPTY_STRING         
        self.cancelTime = EMPTY_STRING          


class TradeData:
    def __init__(self):
        self.symbol = EMPTY_STRING              
        self.exchange = EMPTY_STRING          
        self.vtSymbol = EMPTY_STRING           

        self.tradeID = EMPTY_STRING  
        self.vtTradeID = EMPTY_STRING          
        
        self.orderID = EMPTY_STRING             
        self.vtOrderID = EMPTY_STRING           
        
        self.direction = EMPTY_UNICODE          
        self.offset = EMPTY_UNICODE             
        self.price = EMPTY_FLOAT                
        self.volume = EMPTY_INT                
        self.tradeTime = EMPTY_STRING  


class PositionData:
    def __init__(self):
        self.symbol = EMPTY_STRING              
        self.exchange = EMPTY_STRING            
        self.vtSymbol = EMPTY_STRING        
        
        self.direction = EMPTY_STRING           
        self.position = EMPTY_INT            
        self.frozen = EMPTY_INT                 
        self.price = EMPTY_FLOAT                
        self.vtPositionName = EMPTY_STRING     
        self.ydPosition = EMPTY_INT             
        self.positionProfit = EMPTY_FLOAT      


class SubscribeReq:
    def __init__(self):
        self.symbol = EMPTY_STRING             
        self.exchange = EMPTY_STRING     

    
class OrderReq:                    
    def __init__(self):
        self.symbol = EMPTY_STRING              
        self.exchange = EMPTY_STRING            
        self.price = EMPTY_FLOAT                
        self.volume = EMPTY_INT                 
    
        self.priceType = EMPTY_STRING           
        self.direction = EMPTY_STRING         
        self.offset = EMPTY_STRING             


class CancelOrderReq:
    def __init__(self):
        self.symbol = EMPTY_STRING              
        self.exchange = EMPTY_STRING                  
        