from eventType import *
from eventEngine import EventEngine
import os
import tdxApi

def timer_fun(event):
    print("test_func:{}".format(event.type_))

if __name__ == "__main__":
    engine = EventEngine()
    engine.register(EVENT_TIMER,timer_fun)
    engine.start()
    
    


