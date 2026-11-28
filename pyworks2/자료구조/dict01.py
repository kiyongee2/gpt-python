# 항목별 지출 (딕셔너리: 이름표와 값의 짝)
spending = {
  "식비": 35000, 
  "교통비": 12000, 
  "카페": 9000, 
}
print(spending)  # {'식비': 35000, '교통비': 12000, '카페': 9000}
print(spending.keys())    # 지출 항목들만 출력
print(spending.values())  # 지출 금액들만 출력
print(spending.items())   # 항목과 금액 쌍을 모두 출력

# 항목별 지출 출력
for item, cost in spending.items():
    print(f"{item}: {cost:,}원")

# 총합을 구하는 함수
def total(data):
    return sum(data.values())   # 값들만 모아 더한다

# print("지출 내역")
# print('=' * 20)
# for item, cost in spending.items():
#     print(f"{item}: {cost:,}원")
# print(f"합계: {total(spending):,}원")

# 학생 성적 관리
student_list = [
    {"name": "이대한", "kor": 95, "eng": 80, "math": 80},
    {"name": "박민국", "kor": 80, "eng": 75, "math": 75},
    {"name": "오상식", "kor": 90, "eng": 85, "math": 90}
]

print("=====성적표 =====")
print("이름\t국어\t영어\t수학\t총점\t평균")
for student in student_list:
    name = student['name']
    kor = student['kor']
    eng = student['eng']
    math = student['math']
    total = kor + eng + math
    avg = total / 3
    print(f"{name}\t{kor}\t{eng}\t{math}\t{total}\t{avg:.2f}")