# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 12:30:24 2022

@author: h_yes
"""

import pandas as pd
import numpy as np

data = np.array([[1,2,3,4],[5,6,7,np.nan], [9,10,np.nan,11]])

#sutunlara isim verir
df = pd.DataFrame(data, columns = ["A", "B", "C", "D"])

#dataframe yazdırır
print(df)

#bos ise True doluysa False yazdırır
print(df.isnull())

#hangi sutunden kac adet nan degeri varsa yazdırır
print(df.isnull().sum())

# default 0. 0 and 'index'removes ROWS that contains NULL values. 1 and 'columns' removes COLUMNS that contains NULL values
#nan deger iceren satırları kaldırır. Diğer ifadeyle nan deger icermeyen satırları bırakır
print(df.dropna(axis=0))

#nan deger iceren sutunları kaldırır. Diğer ifadeyle nan deger icermeyen sutunları bırakır
print(df.dropna(axis=1))

# how= 'all' 'any'	Optional, default 'any'. Specifies whether to remove the row or column when ALL values are NULL, or if ANY value is NULL.
print(df.dropna(how = "all"))

# Specifies the number of NOT NULL values required to keep the row.
# Satırı tutmak için gereken NOT NULL değerlerinin sayısını belirtir.
print(df.dropna(thresh = 4))

# NULL değerlerin nerede aranacağını belirtir. Aranılan sutunde nan deger iceren satırı kaldırır
print(df.dropna(subset= ["D"]))

# kaldırma islemini df'e atamadıgımız icin df etkilenmedi yukarıdaki islemlerden
print(df)

#eksik verileri  doldurmak icin gerekli kutuphane
# https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html
from sklearn.impute import SimpleImputer 

#strategy = default "mean". Other strategies "median" , “most_frequent” , “constant”. If “constant”, then replace missing values with fill_value. Can be used with strings or numeric data.
imp_mean = SimpleImputer(missing_values=np.nan, strategy="mean")

imp_mean = imp_mean.fit(df.values)
imputed_data = imp_mean.transform(df.values)

print(imputed_data)

#simple imputer alternatifi
print(df.fillna(df.mean()))

df.fillna(method='ffill', inplace=True)



















