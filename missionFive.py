import pandas as pd
excel_file_path = "C:/Users/alioz/OneDrive/Belgeler/datasets/miuul_gezinomi.xlsx"
df = pd.read_excel(excel_file_path)

agg_df = df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": "mean"}).sort_values(by="Price", ascending=False)
agg_df.head(50)

agg_df.reset_index(inplace=True)

agg_df.head(50)
