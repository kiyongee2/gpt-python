# 2차원 리스트 생성
a = [
  [1, 2, 3],
  [4, 5, 6]
]

print(a[0][0])  # 첫 번째 행의 첫 번째 요소 출력
print(a[1][1])  # 두 번째 행의 두 번째 요소 출력
    
# 2차원 리스트의 각 행 출력
for row in a:
    print(row)
    
# 2차원 리스트의 각 요소 출력
for row in a:
    for e in row:  #element in row
        print(e, end=' ')
    print()
    
# 2차원 리스트의 각 요소에 접근
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
    
# 학생 3명의 두 과목 점수입니다.
scores = [
    [90, 80],
    [70, 100],
    [60, 75]
]

# 각 학생의 총점 출력
for row in scores:
  total = sum(row)
  print(f"총점: {total}")
  
# 각 학생의 평균 점수 출력
for row in scores:
  avg = sum(row) / len(row)
  print(f"평균 점수: {avg}")

# 각 학생의 점수 출력
for i, score in enumerate(scores):
    print(f"학생 {i+1} 점수: {score}")
    
# 각 학생의 평균 점수 출력
for i, score in enumerate(scores):
    avg = sum(score) / len(score)
    print(f"학생 {i+1} 평균 점수: {avg}")
    
