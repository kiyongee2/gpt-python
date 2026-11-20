import random

menus = ["김치찌게", "비빔밥", "돈까스", "칼국수", "제육볶음", "초밥", "자장면"]

chosen_menus = random.sample(menus, 2)

# 고른 두 메뉴를 화면에 보여 줍니다.
print("오늘의 점심 후보 두 가지:")
for menu in chosen_menus:
    print(f"- {menu}")