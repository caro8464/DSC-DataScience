import math
# 1. Exercise:
#   Attributes:
    #   Age: up to 30, 31..40, over 40
    #   Income: low, medium, high
    #   Student: yes, no
    #   Credit_rating: fair, excellent
    # Target concept:
    #   Buys_Computer: yes, no

# set 20: 8 no, 12 yes -> -(0.4* log2(0.4) + 0.6 * log2(0.6)) = 0,97095
EntropyComplete =-(8/20)*math.log((8/20),2)-(12/20)*math.log((12/20),2)
print("Complete",EntropyComplete,"\n") #20/20
EntropyStudentY = -((8/9)*math.log((8/9),2)+(1/9)*math.log((1/9),2))
print(EntropyStudentY,"\n") #9/20
EntropyStudentN = -((4/11)*math.log((4/11),2)+(7/11)*math.log((7/11),2))
print(EntropyStudentN,"\n") #11/20
student = EntropyComplete -(((9/20)*EntropyStudentY+(11/20)*EntropyStudentN))
print("Student Gain: ", student ,"\n")

EntropyIncomeL =-(4/7)*math.log((4/7),2)-(3/7)*math.log((3/7),2)
print(EntropyIncomeL,"\n") #7/20
EntropyIncomeM =-(5/8)*math.log((5/8),2)-(3/8)*math.log((3/8),2)
print(EntropyIncomeM,"\n") #8/20
EntropyIncomeH =-(3/5)*math.log((3/5),2)-(2/5)*math.log((2/5),2)
print(EntropyIncomeH,"\n") #5/20
income = EntropyComplete - ((7/20)* EntropyIncomeL + (8/20) * EntropyIncomeM + (5/20) * EntropyIncomeH)
print("Income Gain: ",income ,"\n")
EntropyCreditF =-(7/10)*math.log((7/10),2)-(3/10)*math.log((3/10),2)
print(EntropyCreditF,"\n")
EntropyCreditE =-(5/10)*math.log((5/10),2)-(5/10)*math.log((5/10),2)
print(EntropyCreditE,"\n")
credit = EntropyComplete - ((10/20) * EntropyCreditF + (10/20) * EntropyCreditE)
print("Credit Rating: ",credit ,"\n")

EntropyAgeL =-(2/8)*math.log((2/8),2)-(6/8)*math.log((6/8),2)
print(EntropyAgeL,"\n") #7/20
# EntropyAgeM =-(6/6)*math.log((6/6),2)-(0/6)*math.log((0/6),2) # 0
EntropyAgeM = 0
# print(EntropyAgeM,"\n") #8/20
EntropyAgeH =-(4/6)*math.log((4/6),2)-(2/6)*math.log((2/6),2)
print(EntropyAgeH,"\n") #5/20
age = EntropyComplete - ((8/20)* EntropyAgeL + 0 + (6/20) * EntropyAgeH)

print("Age Rating: ",age ,"\n")

print("daher wird die oberste verzweigung 'Age' sein")

#             AGE
#            / | \
#           /  |  \
#          /   |   \
#         /    |    \
#      <=30  31..40  >40

# 2. Exercise
from sklearn.datasets import load_iris
from sklearn import tree
import pandas as pd
df = pd.read_csv("./buy_computer.csv", sep=';')
data_df = df.loc[:,df.columns != 'buy']
target_df = df.loc[:,df.columns == 'buy']
data_df.age[data_df.age == '<=30'] = 1
data_df.age[data_df.age == '31..40'] = 2
data_df.age[data_df.age == '>40'] = 3
data_df.income[data_df.income == 'low'] = 1
data_df.income[data_df.income == 'medium'] = 2
data_df.income[data_df.income == 'high'] = 3
data_df.credit_rating[data_df.credit_rating == 'fair'] = 1
data_df.credit_rating[data_df.credit_rating == 'excellent'] = 2
X = data_df.values.tolist()
y = target_df.values.tolist()

tree_clf = tree.DecisionTreeClassifier(criterion="entropy", max_depth=10, random_state=0)
tree_clf.fit(X, y)

fn=['age','income','student','credit_rating']
cn=["didn't buy", 'bought a PC']


tree.export_graphviz(tree_clf,
                      out_file="tree.dot",
                      feature_names = fn, 
                      class_names=cn,
                      filled = True)


# the decision tree made with python SciKit Learn is Binary and as such it looks different but the values seem to be the same