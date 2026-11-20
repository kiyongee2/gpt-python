
goal = 0  # 목표 잔수
cups = 0  # 지금까지 마신 잔 수

for hour in range(9, 18):
  cups = cups + 1
  print(hour, "시: 물", cups, "잔")
  
if cups >= goal:
  print(f"오늘 목표 달성: 총 {cups}잔")
else:
  print(f"목표까지 {goal - cups}잔 남았어요.")