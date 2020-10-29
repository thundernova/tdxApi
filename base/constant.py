# encoding: UTF-8

# 默认空值
EMPTY_STRING = ''
EMPTY_UNICODE = u''
EMPTY_INT = 0
EMPTY_FLOAT = 0.0

# 方向常量
DIRECTION_LONG = u'long'
DIRECTION_SHORT = u'short'

# 开平常量
OFFSET_OPEN = u'open'
OFFSET_CLOSE = u'close'
OFFSET_CLOSETODAY = u'close today'
OFFSET_CLOSEYESTERDAY = u'close yesterday'

# 状态常量
STATUS_NOTTRADED = u'pending'
STATUS_PARTTRADED = u'partial filled'
STATUS_ALLTRADED = u'filled'
STATUS_CANCELLED = u'cancelled'
STATUS_REJECTED = u'rejected'
STATUS_UNKNOWN = u'unknown'

# 价格类型常量
PRICETYPE_LIMITPRICE = u'limit order'
PRICETYPE_MARKETPRICE = u'market order'
PRICETYPE_FAK = u'FAK'
PRICETYPE_FOK = u'FOK'

# 交易所类型
EXCHANGE_SSE = 'SSE'       # 上交所
EXCHANGE_SZSE = 'SZSE'     # 深交所

# K线周期类型
INTERVAL_1M = u'1-Minute'
INTERVAL_5M = u'5-Minute'
INTERVAL_15M = u'15-Minute'
INTERVAL_30M = u'30-Minute'
INTERVAL_1H = u'1-Hour'
INTERVAL_4H = u'4-Hour'
INTERVAL_DAILY = u'Daily'
INTERVAL_WEEKLY = u'Weekly'