from dataclasses import dataclass
from enum import Enum

class Side(Enum):
  BUY = 1
  SELL = 2

class OrderType(Enum):
  LIMIT = 1
  MARKET = 2
  CANCEL = 3

@dataclass
class Order:
  order_id: int
  side: Side
  order_type: OrderType
  price: float
  qty: int
  timestamp: float
