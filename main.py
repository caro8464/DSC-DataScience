
# # https://www.python-course.eu/k_nearest_neighbor_classifier.php
# # Before we actually start with writing a nearest neighbor classifier, we need to think about the data, i.e. the learnset. We will use the "iris" dataset provided by the datasets of the sklearn module.
#
# The data set consists of 50 samples from each of three species of Iris
#
# Iris setosa,
# Iris virginica and
# Iris versicolor.
#
# Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres.

import numpy as np
from math import sqrt
from sklearn import datasets

from collections import Counter

iris = datasets.load_iris()
iris_data = iris.data
iris_labels = iris.target
print("data: {}, {}, {}".format(iris_data[0], iris_data[42], iris_data[99]))
print("labels: {}, {}, {}".format(iris_labels[0], iris_labels[42], iris_labels[99]))
iris_data[1:10]

print("For a good learnset we need to split the previous data randomly")

iris_labels


np.random.seed(1337)
indices = np.random.permutation(len(iris_data))
training_samples = 20

learnset_data = iris_data[indices[:-training_samples]]
learnset_labels = iris_labels[indices[:-training_samples]]

testset_data = iris_data[indices[-training_samples:]]
testset_labels = iris_labels[indices[-training_samples:]]

print(learnset_data[:6], learnset_labels[:6])
print(testset_data[:6], testset_labels[:6])

# the Euclidean distance is ideal to determine the "closeness" in category:

def calc_euclidean_distance(instance1, instance2):
    # just in case, if the instances are lists or tuples:
    instance1 = np.array(instance1) 
    instance2 = np.array(instance2)
    
    return np.linalg.norm(instance1 - instance2)

print("\n")
print("vertical should be 2: %d" % calc_euclidean_distance([3, 1], [3, 3]))
print("horizontal should be 2: %d" % calc_euclidean_distance([3, 1], [1, 1]))
print("diagonal should be {}: {}".format(sqrt(2),calc_euclidean_distance([1, 1], [2, 2])))
print("\n")
print(calc_euclidean_distance(learnset_data[3], learnset_data[-10]))
print("\n")

def get_neighbors(training_set, labels, test_data, amount, distance_func=calc_euclidean_distance):
    
    # get_neighbors calculates a list of the 'amount' nearest neighbors
    # of an instance 'test_data'.
    # The list contains tuples with (index, distance, label)
    # index    is the index from the training_set, 
    # distance     is the distance between the test_data and the 
    #          instance training_set[index]
    # distance_function is a reference to a function used to calculate the distances
    
    distances = []
    for index in range(len(training_set)):
        distance = distance_func(test_data, training_set[index])
        distances.append((training_set[index], distance, labels[index]))
    distances.sort(key=lambda x: x[1])
    neighbors = distances[:amount]
    return neighbors

# We will test the function with our iris samples:

for i in range(10):
    neighbors = get_neighbors(learnset_data, 
                                learnset_labels, 
                                testset_data[i], 
                                3, 
                                distance_func=calc_euclidean_distance)
    print(testset_data[i], testset_labels[i])

####### Voting for a Single Result ########


def vote_for_probability(neighbors):
    class_counter = Counter()
    for neighbor in neighbors:
        class_counter[neighbor[2]] += 1
    _labels, votes = zip(*class_counter.most_common())
    winner = class_counter.most_common(1)[0][0]
    votes4winner = class_counter.most_common(1)[0][1]
    return {"label":winner, "confidence":100 * (votes4winner/sum(votes))}

# now categorize our flower of the forest

iris_to_test = [4.8,2.5,5.3,2.4]
neighbors = get_neighbors(learnset_data, 
                            learnset_labels, 
                            iris_to_test, 
                            5, 
                            distance_func=calc_euclidean_distance)
prediction = vote_for_probability(neighbors)
print("\npredicted label: {}\nconfidence: {}%\ndata: {}".format(prediction.get("label", "not found"), prediction.get("confidence", "not found"),iris_to_test))

