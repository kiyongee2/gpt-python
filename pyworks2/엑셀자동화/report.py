import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.chart import BarChart, Reference

df = pd.read_excel("직원명단.xlsx")
df["입사일"] = pd.to_datetime(df["입사일"]).dt.date     # 날짜만 남기기

# 1. 부서별 요약표 만들기
summary = df.groupby("부서")["월급"].agg(["count", "sum", "mean"]).reset_index()
summary.columns = ["부서", "인원", "월급합계", "평균월급"]
summary["평균월급"] = summary["평균월급"].astype(int)

# 2. 요약 시트 + 부서별 시트로 나눠 한 파일에 저장
with pd.ExcelWriter("직원현황_보고서.xlsx") as writer:
    summary.to_excel(writer, sheet_name="요약", index=False)
    for name, group in df.groupby("부서"):              # 부서마다 반복
        group.to_excel(writer, sheet_name=name, index=False)

# 3. 서식 꾸미기 (openpyxl)
wb = load_workbook("직원현황_보고서.xlsx")
for ws in wb.worksheets:                               # 모든 시트에 반복
    for cell in ws[1]:                                 # 1행(제목 행)
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor="2F6FED")
        cell.alignment = Alignment(horizontal="center")
    for col in ws.columns:
        longest = max(len(str(cell.value)) for cell in col)   # 가장 긴 글자 수
        ws.column_dimensions[col[0].column_letter].width = longest + 6
        for cell in col[1:]:
            if type(cell.value) == int:                 # 숫자면 천 단위 쉼표
                cell.number_format = "#,##0"

# 4. 요약 시트에 막대 차트 넣기
ws = wb["요약"]
chart = BarChart()
chart.title = "부서별 평균 월급"
data = Reference(ws, min_col=4, min_row=1, max_row=ws.max_row)   # 평균월급 열
cats = Reference(ws, min_col=1, min_row=2, max_row=ws.max_row)   # 부서 이름
chart.add_data(data, titles_from_data=True)
chart.set_categories(cats)
ws.add_chart(chart, "F2")

wb.save("직원현황_보고서.xlsx")
print("보고서 완성! 시트 목록:", wb.sheetnames)