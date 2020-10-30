from tdxApi.base.gateway import Gateway
from tdxApi.api import TradeX2
from tdxApi.base.functions import *
from mdApi import CatsMdApi
from tdApi import TdxTdApi
import json
import sys

class TdxGateway(Gateway):
    def __init__(self,eventEgine,gatewayName="Tdx"):
        super(TdxGateway,self).__init__(eventEgine,gatewayName)
        
        self.mdApi = CatsMdApi(self)
        self.tdApi = TdxTdApi(self)

        self.mdConnected = False
        self.tdConnected = False

        self.qryEnabled = False

        self.fileName = self.gatewayName + "_connect.json"
        self.filePath = getJsonPath(self.fileName,__file__)

    def connect(self):
        with open(self.filePath,'rb') as f:
            setting = json.load(f)
        try:
            mktHost = setting["mktHost"]
            mktPort = setting["mktPort"]
            nQsid = setting["nQsid"]
            tdHost = setting["tdHost"]
            tdPort = setting["tdPort"]
            nVersion = setting["nVersion"]
            nBranchID = setting["nBranchID"]
            nAccountType = setting["nAccountType"]
            sClientAccount = setting["sClientAccount"]
            sBrokerAccount = setting["sBrokerAccount"]
            sPassword = setting["sPassword"]
            sTxPassword = setting["sTxPassword"]
        except KeyError:
            print("KeyError")
            sys.exit(-1)

        try:
            clientHq = TradeX2.TdxHq_Connect(mktHost, mktPort)
        except TradeX2.error as err:
            print ("error: ", err)
            sys.exit(-1)
        print ("\n\t连接成功!\n")
    
    def subscribe(self,subscribeReq):
        pass
    
    def sendOrder(self,orderReq):
        pass
    
    def cancelOrder(self,cancelOrderReq):
        pass

    def qryAccount(self):
        pass
    
    def qryPosition(self):
        pass

    def close(self):
        pass

    
class TdxMdApi:
    def __init__(self,gateway):
        pass

    def connect(self):
        pass

class TdxTdApi:
    def __init__(self,gateway):
        pass

    def connect(self):
        pass


