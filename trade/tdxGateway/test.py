from tdxGateway import TdxGateway
from tdxApi.event.eventEngine import EventEngine
import sys

if __name__ == "__main__":
    inst = TdxGateway(EventEngine())
    inst.connect()
