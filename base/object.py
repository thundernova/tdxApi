from tdxApi.base.constant import *

class TickData:
    def __init__(self):
        self.symbol = EMPTY_STRING
        self.exchange = EMPTY_STRING
        self.vtSymbol = EMPTY_STRING

        self.time = EMPTY_STRING
        self.last = EMPTY_FLOAT
        self.preClose = EMPTY_FLOAT
        self.high = EMPTY_FLOAT
        self.low = EMPTY_FLOAT
        self.upperLimit = EMPTY_FLOAT
        self.lowerLimit = EMPTY_FLOAT
        self.curVolume = EMPTY_INT
        self.volume = EMPTY_INT
        self.turnover = EMPTY_FLOAT
        
        self.ask_1 = EMPTY_FLOAT
        self.ask_2 = EMPTY_FLOAT
        self.ask_3 = EMPTY_FLOAT
        self.ask_4 = EMPTY_FLOAT
        self.ask_5 = EMPTY_FLOAT
        self.askVol_1 = EMPTY_INT
        self.askVol_2 = EMPTY_INT
        self.askVol_3 = EMPTY_INT
        self.askVol_4 = EMPTY_INT
        self.askVol_5 = EMPTY_INT

        self.bid_1 = EMPTY_FLOAT
        self.bid_2 = EMPTY_FLOAT
        self.bid_3 = EMPTY_FLOAT
        self.bid_4 = EMPTY_FLOAT
        self.bid_5 = EMPTY_FLOAT
        self.bidVol_1  = EMPTY_INT
        self.bidVol_2  = EMPTY_INT
        self.bidVol_3  = EMPTY_INT
        self.bidVol_4  = EMPTY_INT
        self.bidVol_5  = EMPTY_INT

        self.accer = EMPTY_FLOAT


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
        