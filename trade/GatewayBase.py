from ..event.eventType import *
from ..base.constant import *
from .mainEngine import *
from abc import ABC,abstractmethod

class Gateway(ABC):
    def __init__(self,eventEngine,gatewayName):
        self.eventEngine = eventEngine
        self.gatewayName = gatewayName

    def onTick(self,tick):
        pass

    def onTrade(self,trade):
        pass

    def onOrder(self,order):
        pass

    def onPosition(self,position):
        pass
    
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