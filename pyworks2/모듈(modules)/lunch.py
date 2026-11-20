import random

menus = ["김치찌게", "비빔밥", "돈까스", "칼국수", "제육볶음"]

def pick_menu():
  return random.choice(menus)

print("오늘의 점심 추천:", pick_menu())