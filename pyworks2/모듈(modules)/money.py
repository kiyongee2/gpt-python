
spending = {
  "식비": 35000,
  "교통비": 12000,
  "카페": 9000,
  "책": 15000
}

print(spending.values())
print(sum(spending.values()))

def total(data):
  return sum(data.values()) #값들만 더한다.

for item, cost in spending.items():
  print(f"{item}: {cost:,}원")
print(f"합계: {total(spending)}원")