EVENT_TIMER = 'eTimer'                  # 计时器事件
EVENT_TICK = 'eTick.'                   # 行情事件
EVENT_TRADE = 'eTrade.'                 # 成交回报事件
EVENT_ORDER = 'eOrder.'                 # 报单回报事件
EVENT_POSITION = 'ePosition.'           # 持仓回报事件


class Event:
    def __init__(self,type_=None):
        self.type_ = type_
        self.dict_ = {}
