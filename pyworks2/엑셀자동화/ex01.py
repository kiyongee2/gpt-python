from openpyxl import Workbook, load_workbook

# 1. 새 엑셀 파일 만들고 쓰기
wb = Workbook()
ws = wb.active
ws.title = "출석부"

ws["A1"] = "이름"
ws["B1"] = "출석일수"
ws.append(["김민준", 5])
ws.append(["이서연", 4])
ws.append(["박지훈", 5])
wb.save("출석부.xlsx")    # 파일로 저장

# 2. 저장한 파일 다시 열어 읽기
wb = load_workbook("출석부.xlsx")
ws = wb["출석부"]
print(ws["A2"].value, ws.cell(row=2, column=2).value)

for row in ws.iter_rows(min_row=2, values_only=True):
  print(row)
print("마지막 행 번호:", ws.max_row)