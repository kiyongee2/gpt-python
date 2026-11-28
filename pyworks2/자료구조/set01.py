# 집합 생성 및 출력
s = {1, 2, 2, 3}
print(s)  # {1, 2, 3}, 중복된 2는 제거됨

# 집합에 요소 추가
s.add(4)
print(s)  # {1, 2, 3, 4} 출력, 요소 추가 확인

# 집합에서 요소 제거
s.remove(2)
print(s)  # {1, 3, 4} 출력, 요소 제거 확인

# 문자열 집합
text = "hello"
s2 = set(text)
print(s2)  # {'e', 'l', 'h', 'o'} 순서없고, 중복 없음

# 집합 연산 예제
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # 합집합 {1, 2, 3, 4, 5}
print(a & b)  # 교집합 {3}
print(a - b)  # 차집합 {1, 2}
print(b - a)  # 차집합 {4, 5}

# 대칭 차집합
print(a ^ b)  # {1, 2, 4, 5} 출력, a와 b에 모두 속하지 않는 요소들

numbers = [3, 1, 2, 3, 1, 4]
s3 = set(numbers)
print(s3)  # {1, 2, 3, 4} 출력, 리스트의 중복 요소 제거 후 집합 생성

hobby1 = {"영화", "독서", "게임"}
hobby2 = {"게임", "독서", "운동"}
print(hobby1 & hobby2)  # {'독서', '게임'} 출력, 교집합 확인
print(hobby1 | hobby2)  # {'영화', '독서', '게임', '운동'} 출력, 합집합 확인
print(hobby1 - hobby2)  # {'영화'} 출력, 차집합 확인
print(hobby2 - hobby1)  # {'운동'} 출력, 차집합 확인
print(hobby1 ^ hobby2)  # {'영화', '운동'} 출력, 대칭 차집합 확인