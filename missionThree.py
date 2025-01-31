import pandas as pd
excel_file_path = "C:/Users/alioz/OneDrive/Belgeler/datasets/miuul_gezinomi.xlsx"
df = pd.read_excel(excel_file_path)

df["SaleCheckInDayDiff"]
bins = [-1, 7, 30 ,90, df["SaleCheckInDayDiff"].max()]
labels = ["Last Minuters", "Potantial Planners", "Planners", "Early Bookers"]
df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins, labels=labels)

df.groupby(["SaleCityName", "ConceptName", "EB_Score"]).agg({"Price": "mean"})

df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": "mean"})

df.groupby(["SaleCityName", "ConceptName", "CInDay"]).agg({"Price": "mean"})
