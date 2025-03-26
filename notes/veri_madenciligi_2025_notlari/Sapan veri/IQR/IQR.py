import pandas as pd
import numpy as np
import scipy.stats as stats

# Veri setinin yüklenmesi
ekmek_dataset = pd.read_csv('ekmek.csv')

print(ekmek_dataset)
ekmek_dataset.columns = ["tarih", "urun", "adet"]


print(ekmek_dataset)
print(len(ekmek_dataset))


Q1 = ekmek_dataset.adet.quantile(0.25)
Q3 = ekmek_dataset.adet.quantile(0.75)
IQR = Q3-Q1


outliers = ekmek_dataset[(ekmek_dataset.adet<(Q1-1.5*IQR)) | (ekmek_dataset.adet>(Q3+1.5*IQR))]
print(outliers)
print(len(outliers))

df_final = ekmek_dataset[~((ekmek_dataset.adet<(Q1-1.5*IQR)) | (ekmek_dataset.adet>(Q3+1.5*IQR)))]
print(df_final)
print(len(df_final))