import numpy as np # linear algebra
import pandas as pd # data processing, XLSX file I/O (e.g. pd.read_csv)
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split

#Veri setinin yüklenmesi
data = pd.read_excel('veri.xlsx')

print(data)

#default 0,1 aralığına çevirir
scaler = RobustScaler()
#scaler = MinMaxScaler(feature_range=(0, 100))

data_minmax = scaler.fit_transform(data)

print(data_minmax)

data_inverse = scaler.inverse_transform(data_minmax)

print(data_inverse)



# data = pd.read_excel('Gunluk-NASDAQ.xlsx')
# print(data)
# close = data.values[:,4].tolist()
# print(close)
# close = np.array(close).reshape(-1,1)
# print(close)


# # #https://www.kaggle.com/discussions/general/374163
# train_data, test_data = train_test_split(close, test_size=0.2, shuffle = False)
# print(test_data)

# scaler = MinMaxScaler()
# #Fit the MinMaxScaler to the training data and transform it
# train_data_minmax = scaler.fit_transform(train_data)
# # Transform the test data using the MinMaxScaler that was fit to the training data
# test_data_minmax = scaler.transform(test_data)

# print("test_data_minmax")
# print(test_data_minmax)

# # Now you can use the transformed data to fit a model
# # model.fit(train_data_minmax, y_train)

# # # # # And evaluate the model on the transformed test data
# # model.score(X_test_scaled, y_test)

# # # test_data_inverse = scaler.inverse_transform(test_data_minmax)

# # # print("test_data_inverse")
# # # print(test_data_inverse)


