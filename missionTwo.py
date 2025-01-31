
import pandas as pd
excel_file_path = "C:/Users/alioz/OneDrive/Belgeler/datasets/miuul_gezinomi.xlsx"
df = pd.read_excel(excel_file_path)
df.info()


df["SaleCheckInDayDiff"]
bins = [-1, 7, 30 ,90, df["SaleCheckInDayDiff"].max()]
labels = ["Last Minuters", "Potantial Planners", "Planners", "Early Bookers"]
df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins, labels=labels)
df.head(50).to_excel("eb_score.xlsx", index=False)