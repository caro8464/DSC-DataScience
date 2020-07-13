import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn import datasets
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix


unkown_iris = [[4.8,2.5,5.3,2.4]]
# i_d = svm.datasets.load_iris()

iris = datasets.load_iris()
iris_data = iris.data
iris_labels = iris.target

np.random.seed(42)
indices = np.random.permutation(len(iris_data))
training_samples = 28

X_train = iris_data[indices[:-training_samples]]
y_train = iris_labels[indices[:-training_samples]]

X_test = iris_data[indices[-training_samples:]]
y_test = iris_labels[indices[-training_samples:]]

# print(i_d.data[0:5])

svc = LinearSVC()
svc.fit(X_train, y_train)
y_pred = svc.predict(X_test)
iris_predict = svc.predict(unkown_iris)
ir = svc._predict_proba_lr(unkown_iris)
print("the flower is iris Virginica = {}".format(bool(iris_predict)))
print("the chances that ist not Virginica and that it is respectively are {}".format(ir))


df = sns.load_dataset('iris')


sns.set(style="ticks") 
plt.figure(figsize=(12,10))
plt.subplot(2,2,1)
sns.boxplot(x=df["species"], y=df["sepal_length"],data=df)
plt.subplot(2,2,2)
sns.boxplot(x=df["species"], y=df["sepal_width"],data=df)
plt.subplot(2,2,3)
sns.boxplot(x=df["species"], y=df["petal_length"],data=df)
plt.subplot(2,2,4)
sns.boxplot(x=df["species"], y=df["petal_width"],data=df)
plt.show()
