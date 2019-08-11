# Support Vector Machine (SVM)

# Importing the libraries
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('financial_pred_C5_all.csv', encoding='big5', low_memory=False)
X = dataset.iloc[:, 1:10].values
y = dataset.iloc[:, 11].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting SVM to the Training set
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

print("預測正確率 = ", (41+1441+53+41+108)/(41+13+5+12+8+508+1441+967+875+590+4+37+53+38+17+14+36+35+41+29+64+72+62+92+108))