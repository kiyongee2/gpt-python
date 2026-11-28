
# 카드 클래스를 정의
class Card:
  count = 1000  # 클래스 변수 (모든 카드 객체가 공유하는 카드 번호)

  def __init__(self, owner):
    self.owner = owner
    Card.count += 1   # 카드 번호를 1 증가시킴

  def get_info(self):
    print(f"카드 소유자: {self.owner}, 카드 번호: {Card.count}")
    
c1 = Card("김파이")
c1.get_info()

c2 = Card("오자바")
c2.get_info()