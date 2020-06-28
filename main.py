import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix
unkown_iris = [[4.8,2.5,5.3,2.4]]
# i_d = svm.datasets.load_iris()

# print(i_d.data[0:5])
iris = pd.read_csv("iris.data")


X_train = [[5.0,3.6,1.4,0.2],
[4.4,2.9,1.4,0.2],
[7.7,2.6,6.9,2.3],
[5.0,3.4,1.5,0.2],
[4.6,3.4,1.4,0.3],
[5.2,2.7,3.9,1.4],
[7.7,3.8,6.7,2.2],
[4.9,3.1,1.5,0.1],
[5.9,3.0,4.2,1.5],
[6.0,2.2,4.0,1.0]]

X_test = [[5.6,2.9,3.6,1.3],
[6.9,3.2,5.7,2.3],
[6.5,3.0,5.5,1.8],
[5.4,3.9,1.7,0.4],
[6.1,2.9,4.7,1.4],
[6.7,3.1,4.4,1.4],
[6.0,2.2,5.0,1.5],
[5.0,2.0,3.5,1.0],
[5.6,2.8,4.9,2.0]]

y_train = [0,0,1,0,0,0,1,0,0,0]
y_test = [0,1,1,0,0,0,1,0,1]

svc = LinearSVC()
svc.fit(X_train, y_train)
y_pred = svc.predict(X_test)
iris_predict = svc.predict(unkown_iris)
ir = svc._predict_proba_lr(unkown_iris)
print("the flower is iris Virginica = {}".format(bool(iris_predict)))
print("the chances that ist not Virginica and that it is respectively are {}".format(ir))
# print(confusion_matrix(y_test, y_pred))

# iris.rename(columns={1:'sepal_length',
#                           2:'sepal_width',
#                           3:'petal_length',
#                           4:'petal_width' ,
#                           5:'species'}, 
#                  inplace=True)

# iris.groupby('species').agg(['mean', 'median'])

sns.set(style="ticks") 
plt.figure(figsize=(12,10))
plt.subplot(2,2,1)
sns.boxplot(x='species',y='sepal_length',data=iris)
plt.subplot(2,2,2)
sns.boxplot(x='species',y='sepal_width',data=iris)
plt.subplot(2,2,3)
sns.boxplot(x='species',y='petal_length',data=iris)
plt.subplot(2,2,4)
sns.boxplot(x='species',y='petal_width',data=iris)
plt.show()
