# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:13:20 2022

@author: h_yes
"""


import pandas as pd
import numpy as np
import scipy.stats as stats

# Veri setinin yüklenmesi
ekmek_dataset = pd.read_csv('ekmek.csv')

#tarih, urun, adet sırasıla 0,1,2 indeksinde olduğu icin adet 2. indekste
ekmek_adet = ekmek_dataset.values[:,2].tolist()

# print(type(ekmek_adet))

# zscores_ekmek = stats.zscore(ekmek_adet)

# print(zscores_ekmek[:10])



# ekmek_dataset['zscore_Ekmek'] = stats.zscore(ekmek_adet)
# print(ekmek_dataset)
# print(len(ekmek_dataset))

# # #sapan veriler elde edilir
# # # https://www.w3schools.com/python/gloss_python_regex_metacharacters.asp
# # # | veya  gibi çalışan bir metkarakter
# ekmek_dataset_outliers = ekmek_dataset[(ekmek_dataset.zscore_Ekmek<-3) | (ekmek_dataset.zscore_Ekmek>3)]
# print(ekmek_dataset_outliers)
# print(len(ekmek_dataset_outliers))


# # #sapan veriler cıkarilir.
# # # ~ is bitwise negation operator.
# ekmek_dataset_after_outliers_remove = ekmek_dataset[~((ekmek_dataset.zscore_Ekmek<-3) | (ekmek_dataset.zscore_Ekmek>3))]

# # #bir ust satırdaki kodla aynı isi yapmakta
# # ekmek_dataset_after_outliers_remove = ekmek_dataset[(ekmek_dataset.zscore_Ekmek>-3)]
# # ekmek_dataset_after_outliers_remove = ekmek_dataset[(ekmek_dataset.zscore_Ekmek<3)]
# print(ekmek_dataset_after_outliers_remove)
# print(len(ekmek_dataset_after_outliers_remove))



# outliers bulma islemini manuel yapma
threshold = 3
outlier = []
mean = np.mean(ekmek_adet)
std = np.std(ekmek_adet)

for i in ekmek_adet:
 	z = (i-mean)/std
 	if z > threshold or z < -1*threshold: 
          outlier.append(i)
print(len(outlier))
print('outlier in dataset is', outlier)



# #manuel hesaplama
toplam = 0
sayac=0
for i in ekmek_adet:
    toplam = toplam +i
    sayac=sayac+1

print("toplam = ",toplam)

mean = toplam/sayac

print("ort = ", mean)

#standart sapma bulunması
aratoplam = 0
aratoplam_list = [(i-mean)**2 for i in ekmek_adet ]
aratoplam = sum(aratoplam_list)

ss = (aratoplam/(sayac-1))**0.5

print("ss = ", ss)


zscores = [(x - mean) / ss for x in ekmek_adet]

print(zscores[:10])







