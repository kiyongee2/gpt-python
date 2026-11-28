# 이메일 주소에서 아이디와 도메인을 분리하여 출력하는 예제
email = "user@naver.com"

parts = email.split('@')
user = parts[0]
domain = parts[1]

'''
user = email.split('@')[0]
domain = email.split('@')[1]
'''

print(f"아이디: {user}")
print(f"도메인: {domain}")

# 출생연도로 지원금 신청일 안내
birth_year = input("출생연도를 입력하세요: ")

'''
if birth_year <= 2000:
    print("지원금 신청일: 2024-07-01")
else:
    print("지원금 신청일: 2024-08-01")
'''

last_digit = birth_year[-1];
year = int(birth_year)

if year < 1900 or year > 2006:
    print("지원금 신청 대상이 아닙니다.")
else:
    if last_digit in ['1', '6']:
      print("신청일은 월요일입니다.")
    elif last_digit in ['2', '7']:
      print("신청일은 화요일입니다.")
    elif last_digit in ['3', '8']:
      print("신청일은 수요일입니다.")
    elif last_digit in ['4', '9']:
      print("신청일은 목요일입니다.")
    elif last_digit in ['5', '0']:
      print("신청일은 금요일입니다.")
  


