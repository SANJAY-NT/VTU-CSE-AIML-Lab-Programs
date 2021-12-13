#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 12:16:16 2021

@author: Sanjay NT
"""

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,confusion_matrix
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt 

iris=datasets.load_iris()
print("Iris Data set loaded...")

x_train,x_test,y_train,y_test = train_test_split(iris.data,iris.target,test_size=0.3,random_state=1809)
print("Dataset is split into trainingand testing...")
print("Size of training data and itslabel",x_train.shape,y_train.shape )
print("Size of testing data and its label",x_test.shape,y_test.shape)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(x_train)

x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

error_rate = []# Will take some time
for i in range(1,40):
 
 knn = KNeighborsClassifier(n_neighbors=i)
 knn.fit(x_train,y_train)
 pred_i = knn.predict(x_test)
 error_rate.append(np.mean(pred_i != y_test))
 
plt.figure(figsize=(12,6))
plt.plot(range(1,40),error_rate,color='blue', linestyle='dashed', marker='o',markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')

for i in range(len(iris.target_names)): #classes
    print("Label",i,"-",str(iris.target_names[i]))
    
    classifier = KNeighborsClassifier(n_neighbors =5)
    classifier.fit(x_train,y_train)
    y_pred=classifier.predict(x_test)
    
print("Results of Classification using K-nn with K=5")

    
print("Classification Accuracy:",classifier.score(x_test,y_test))

print('Confusion Matrix')
print(confusion_matrix(y_test,y_pred))
print('Accuracy Metrics')
print(classification_report(y_test,y_pred))



