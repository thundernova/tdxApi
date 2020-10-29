
from tdxApi.base.functions import *
from tdxApi.trade.mainEngine import *
from abc import ABC,abstractmethod
from tdxApi.event.eventType import *


class Gateway(ABC):
    def __init__(self,eventEngine,gatewayName):
        self.eventEngine = eventEngine
        self.gatewayName = gatewayName
        
    def onTick(self,tick):
        event = Event(type_=EVENT_TICK)
        event.dict_["data"] = tick
        self.eventEngine.put(event)

    def onTrade(self,trade):
        event = Event(type_=EVENT_TRADE)
        event.dict_["data"] = trade
        self.eventEngine.put(event)

    def onOrder(self,order):
        event = Event(type_=EVENT_ORDER)
        event.dict_["data"] = order
        self.eventEngine.put(event)

    def onPosition(self,position):
        event = Event(type_=position)
        event.dict_["data"] = position
        self.eventEngine.put(event)
    
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def subscribe(self,subscribeReq):
        pass
    
    @abstractmethod
    def sendOrder(self,orderReq):
        pass
    
    @abstractmethod
    def cancelOrder(self,cancelOrderReq):
        pass

    @abstractmethod
    def qryAccount(self):
        pass
    
    @abstractmethod
    def qryPosition(self):
        pass

    @abstractmethod
    def close(self):
        pass