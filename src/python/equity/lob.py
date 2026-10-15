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

if __name__ == "__main__":
  sample_order = Order(
    order_id=1,
    side=Side.BUY,
    order_type=OrderType.LIMIT,
    price=100.50,
    qty=10,
    timestamp=1693564800.0
  )
print("Ordine creato con successo:")
print(sample_order)
