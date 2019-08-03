import numpy as np
import pandas as pd
import warnings
from sklearn.metrics import r2_score

# 去掉warning
warnings.filterwarnings('ignore')
# 匯入dataset
dataset = pd.read_csv("2330.csv", encoding='big5', low_memory=False)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)  # 統一先用0.3

# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(np.reshape(y_train, (-1, 1)))


# Fitting SVR to the dataset
from sklearn.svm import SVR
regressor = SVR(kernel='rbf')
regressor.fit(X_train, y_train)

# Predicting a new result
y_pred = regressor.predict(X_test)  # 不確定是要用X, X_train還是X_test
y_pred = sc_y.inverse_transform(y_pred)
print("R2-square = ", r2_score(y_test, y_pred))


def MAPE(true, pred):
    diff = np.abs(np.array(true) - np.array(pred))
    return np.mean(diff / true)


print("MAPE = ", MAPE(y_test, y_pred))