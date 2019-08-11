import pandas as pd

traindf = pd.read_csv("financial_train.csv", encoding='big5', low_memory=False)
testdf = pd.read_csv("financial_test.csv", encoding='big5', low_memory=False)

X_train = traindf.iloc[:, 2:10].values
y_train = traindf.iloc[:, 11].values
X_test = testdf.iloc[:, 2:10].values
y_test = testdf.iloc[:, 11].values


from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.svm import SVC
classifier = SVC(kernel='rbf', random_state=0)  # , decision_function_shape='ovo'
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)
print(y_pred)
# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

print("預測正確率 = ", (104+521+88+92+102)/(104+155+110+118+85+74+521+346+339+257+16+162+88+99+42+11+128+93+92+37+35+180+115+149+102))
