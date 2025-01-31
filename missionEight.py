import pandas as pd
excel_file_path = "C:/Users/alioz/OneDrive/Belgeler/datasets/miuul_gezinomi.xlsx"
df = pd.read_excel(excel_file_path)

agg_df = df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": "mean"}).sort_values(by="Price", ascending=False)
agg_df.head(50)

agg_df.reset_index(inplace=True)
agg_df.head(50)


agg_df["sales_level_based"] = agg_df[["SaleCityName", "ConceptName", "Seasons"]].agg(lambda x: "_".join(x).upper(), axis=1)
agg_df.head(50)

agg_df["SEGMENT"] =pd.qcut(agg_df["Price"],4,labels=["D","C","B","A"])
agg_df.head(50)
agg_df.groupby("SEGMENT").agg({"Price": ["mean", "max", "sum"]})

agg_df.sort_values(by="Price")

new_user = ("ANTALYA_HERŞEY_DAHİL_HIGH")
agg_df[agg_df["sales_level_based"] == new_user]