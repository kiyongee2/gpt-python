
class Cart:
  def __init__(self):
    self.items = []  # 장바구니에 담긴 아이템 목록
    
  # 아이템 추가
  def add_item(self, item):
    self.items.append(item)  # 아이템을 장바구니에 추가

  # 장바구니에 담긴 아이템 목록 출력
  def get_items(self):
    print("장바구니:", self.items)
    
  # 아이템 제거
  def remove_item(self, item):
    if item in self.items:
      self.items.remove(item)
    else:
      print(f"{item}은(는) 장바구니에 없습니다.")
      
  # 장바구니 비우기
  def clear_cart(self):
    self.items = []
    print("장바구니가 비워졌습니다.")
    
  # 장바구니에 담긴 아이템 수 확인
  def item_count(self):
    return len(self.items)
  
my_cart = Cart()
my_cart.add_item("사과")
my_cart.add_item("바나나")
my_cart.get_items()
print("장바구니 아이템 수:", my_cart.item_count())

my_cart.remove_item("사과")
my_cart.remove_item("오렌지")  # 장바구니에 없는 아이템 제거 시도
my_cart.get_items()
print("장바구니 아이템 수:", my_cart.item_count())

# 장바구니 비우기 테스트
my_cart.clear_cart()
my_cart.get_items()
print("장바구니 아이템 수:", my_cart.item_count())