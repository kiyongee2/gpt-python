
x = 10

def show():
  y = 5
  print(x, y)
  
show() #호출
print(x)
# print(y) # y는 함수 내부에서만 유효하므로 에러 발생

# 전역 변수와 함수 내에서의 전역 변수 사용 예제
count = 0
def up():
  global count  # 전역 변수 count를 사용하겠다는 의미
  count += 1
  print(count)

up() # 호출
up() # 호출
print(count)

# 배송비 계산 프로그램
def calculate_shipping(cost):
  if cost >= 40000:
    return cost + 3000
  else:
    return cost

price = 45000 #구매 금액
total_price = calculate_shipping(price)
print("총 비용:", total_price)
