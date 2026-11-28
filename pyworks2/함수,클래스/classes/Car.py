
# 자동차 클래스를 정의
class Car:
  def __init__(self, color, model, wheel):
    self.color = color
    self.model = model
    self.wheel = wheel

  def drive(self):
    print(f"{self.color} {self.model} 자동차가 달린다. 바퀴 수: {self.wheel}")
 
# 자동차 객체 생성 및 주행
car1 = Car("흰색", "Avante", 4)
car1.drive()

car2 = Car("검정", "Sonata", 4)
car2.drive()


# 객체 리스트
print("객체 리스트에 있는 자동차 정보:")
car_list = [
  Car("은색", "EV6", 4),
  Car("빨강", "K5", 4),
  Car("파랑", "Sorento", 4)
]
for car in car_list:
  car.drive()
  print("총 자동차 수:", len(car_list))