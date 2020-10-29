from  base.functions import *

class TradingEngine:
    settingFileName = "trading_setting.json"
    settingFilePath = getJsonPath(settingFileName)

    def __init__(self,mainEngine,eventEngine):
        self.mainEngine = mainEngine
        self.eventEngine = eventEngine

        self.strategyDict = {}
        self.tickStrategyDict = {}
        self.orderStrategyDict = {}
        self.strategyOrderDict = {}
        self.tradeSet = set()
    
    def sendOrder(self,symbol,orderType,price,volume,strategy):
        pass

    def cancelOrder(self,OrderID):
        pass

    def processTickEvent(self,event):
        pass

    def processOrderEvent(self,event):
        pass

    def processTradeEvent(self,event):
        pass

    def registerEvent(self):
        pass

    def loadStrategy(self,setting):
        pass

    def subscribeMarketData(self, strategy):
        pass

    def initStrategy(self, name):
        pass

    def startStrategy(self, name):
        pass

     def stopStrategy(self, name):
         pass

    def initAll(self):
        pass

    def startAll(self):
        pass

    def stopAll(self):
        pass

    def callStrategyFunc(self, strategy, func, params=None):
        pass

    def saveSyncData(self, strategy):
        pass

    def loadSyncData(self, strategy):
        pass

    def roundToPriceTick(self, priceTick, price):
        pass

    def stop(self):
        pass

    def cancelAll(self, name):
        pass

