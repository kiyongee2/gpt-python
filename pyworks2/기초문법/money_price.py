
money = 20000
price = 4500
count = 0

while money >= price:
  money = money - price  # 커피값 내기
  count = count + 1
  
print(f"아메리카노 {count}잔을 살 수 있어요");
print(f"남은 돈 {money}원")

if money >= 3000:
  print("쿠키도 하나 살 수 있어요!")
else:
  print("쿠키는 다음에...")