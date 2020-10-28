import eventType
from eventEngine import EventEngine


def timer_fun(event):
    print("test_func:{}".format(event.type_))

if __name__ == "__main__":
    engine = EventEngine()
    engine.register(eventType.EVENT_TIMER,timer_fun)
    engine.start()


