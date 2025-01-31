
import pandas as pd
excel_file_path = "C:/Users/alioz/OneDrive/Belgeler/datasets/miuul_gezinomi.xlsx"
df = pd.read_excel(excel_file_path)

# Genel bilgilere bakalım.
print(df.head())
print("-----------------------------------------")
print(df.shape)
print("-----------------------------------------")
print(df.info())
print("-----------------------------------------")


# Kaç unique sınıf var?
print(df["SaleCityName"].nunique())
print(df["SaleCityName"].value_counts())

# Kaç unique konsept vardır?
print(df["ConceptName"].nunique())

# Hangi konsept için kaç satış yapılmış?
print(df["ConceptName"].value_counts())

# Şehirlere göre satışlardan toplam kazanç nedir?
df.groupby("SaleCityName").agg({"Price": "sum"})

# Konseptlere göre satışlardan toplam ne kadar kazanılmış?
df.groupby("ConceptName").agg({"Price": "sum"})

# Şehirlere göre fiyat ortalamaları nedir?
df.groupby("SaleCityName").agg({"Price": "mean"})
"""Ya da df.groupnu(by=["SaleCityName"]).agg({"Price": "mean"})"""

# Konseptlere göre fiyat ortalamaları nedir?
df.groupby("ConceptName").agg({"Price": "mean"})

# Şehir konsept kırılımında fiyat ortalamaları nedir?
df.groupby(["SaleCityName", "ConceptName"]).agg({"Price": "mean"})
