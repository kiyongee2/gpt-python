
FILE = "todo.txt"

print("오늘 할 일을 입력하세요. (아무것도 입력하지 않고 Enter -> 끝)")
with open(FILE, "a", encoding="utf-8") as f:
  while True:
    task = input("할 일: ").strip()
    if task == "":
      break
    f.write(task + "\n")
    
with open(FILE, "r", encoding="utf-8") as f:
  lines = f.readlines()
  
print("\n=== 나의 할 일 목록 ====")
if len(lines) == 0:
  print("아직 저장된 할 일이 없습니다.")
for number, line in enumerate(lines, start=1):
  print(f"{number}. {line.strip()}")