# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 13:08:43 2022

@author: h_yes
"""

import pandas as pd
import numpy as np



df = pd.DataFrame([["red", "L", 5.0, "class1"],
                  ["blue", "XL", 2.0, "class2"],
                  ["black", "M", 3.0, "class1"]])
df.columns = ["color", "size", "age", "classlabel"]
print(df)
print(df.dtypes)




#aralarında sıra bağlantısı varsa manuel olarak map edebiliriz
size_mapping = {"XL":3, "L":2, "M":1}
df["size"] = df["size"].map(size_mapping)
print(df)





# sıra bağlantısı varsa enumerate sayesinde otomatik olarak değer de türetebiliriz
class_mapping = {label: idx for idx, label in enumerate(np.unique(df["classlabel"]))}
print(class_mapping)

df["classlabel"] = df["classlabel"].map(class_mapping)
print(df)




# bir üst kodda enumerate ile yaptığımızı LabelEncoder ile de elde edebiliriz
from sklearn.preprocessing import LabelEncoder
class_le = LabelEncoder()

#donen degerleri goruntuleme
y= class_le.fit_transform(df["classlabel"].values)
print(y)

#donen degerlerle dataframe'deki kategorik verileri degistirme
df["classlabel"]= class_le.fit_transform(df["classlabel"].values)
print(df)





#belirli sutunlarla islem yapma ornegi
X = df[["color","size", "age"]].values
color_le = LabelEncoder()
X[:,0] = color_le.fit_transform(X[:,0])
print(X)



from sklearn.preprocessing import OneHotEncoder

color_ohe=OneHotEncoder()

# https://www.w3schools.com/python/numpy/numpy_array_reshape.asp
# https://saturncloud.io/blog/understanding-the-differences-between-numpy-reshape1-1-and-reshape1-1/
# tek sutunlu arraye donusturur
X[:,0].reshape(-1,1)

color_ohe_data = color_ohe.fit_transform(X[:,0].reshape(-1,1)).toarray()
print(color_ohe_data)

from sklearn.compose import ColumnTransformer

c_transf = ColumnTransformer([
    ("onehot", OneHotEncoder(), [0]),
    ("nothing", "passthrough", [1,2])
])

print(X)

c_transf.fit_transform(X).astype(float)



pd.get_dummies(df[["color", "size", "age"]])

# drop_first parametresi, kodladığınız kategorik değişkenin ilk kategorisini bırakmak isteyip istemediğinizi belirtir.
# Varsayılan olarak, bu drop_first = False olarak ayarlanmıştır. Bu, get_dummies'in girdi kategorik değişkeninin her seviyesi için bir kukla değişken oluşturmasına neden olacaktır.
# drop_first = True olarak ayarlarsanız, ilk kategoriyi düşürecektir. Yani K kategoriniz varsa, yalnızca K - 1 kukla değişken üretecektir.
pd.get_dummies(df[["color", "size", "age"]], drop_first = True)

color_ohe=OneHotEncoder(categories="auto", drop="first")
c_transf = ColumnTransformer([
    ("onehot", color_ohe, [0]),
    ("nothing", "passthrough", [1,2])
])
c_transf.fit_transform(X).astype(float)



