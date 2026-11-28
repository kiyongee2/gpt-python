import pandas as pd

df = pd.read_excel("직원명단.xlsx")

summary = df.groupby("부서")["월급"].agg(["count", "sum", "mean"]).reset_index()
summary.columns = ["부서", "인원", "월급합계", "평균월급"]

# 한 파일 안에 "요약" 시트 + 부서별 시트 저장
with pd.ExcelWriter("직원현황.xlsx") as writer:
  summary.to_excel(writer, sheet_name="요약", index=False)
  for name, group in df.groupby("부서"):  #부서 수만큼 반복
    group.to_excel(writer, sheet_name=name, index=False)
    
print(summary)