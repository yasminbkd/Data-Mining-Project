#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC 
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
# we creat a function that containe all the work we do in machine learning so we can use it in main 
def machinelearning(path):
     df = pd.read_csv(path)
     #Data Preparation : we prepare the data and choose the column we need in labels
     df_model=df[['Rating','Company Name', 'Location', 'Size', 'Founded', 'Type of ownership',
             'Industry', 'Sector', 'Revenue', 'Min_S', 'Max_S',
             'Country', 'age_company', 'python', 'java', 'machine learning', 'aws',
             'Job', 'Seniority']]

     labels = df['avg_salary'].astype(int)
     features =pd.get_dummies(df_model).astype(int)

     X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2,random_state=10)
     #Data modeling : 
     knn = KNeighborsClassifier()
     tree = DecisionTreeClassifier()
     svm = SVC()
     log = LogisticRegression()
     naive = GaussianNB()


     knn.fit(X_train, y_train)
     tree.fit(X_train, y_train)
     log.fit(X_train, y_train)
     naive.fit(X_train, y_train)
     svm.fit(X_train, y_train)



     knn.score(X_test, y_test)
     tree.score(X_test, y_test)
     log.score(X_test, y_test)
     naive.score(X_test, y_test)
     svm.score(X_test, y_test)


     tree_preds = tree.predict(X_test)
     
     accuracy_score(tree_preds, y_test),
     precision_score(tree_preds, y_test,average='micro')
     recall_score(tree_preds, y_test,average='micro')
     f1_score(tree_preds, y_test,average='micro')

     liste = []
     for i in [knn,tree,log,svm,naive]:
        preds=i.predict(X_test)
        liste.append(([i], round(accuracy_score(preds, y_test), 3),"accuracy_score",
          round(precision_score(preds, y_test,average='micro'),3),"precision_score",
          round(recall_score(preds, y_test,average='micro'),3),"recall_score",
          round(f1_score(preds, y_test,average='micro'),3),"f1_score"))
        liste
     dfres = pd.DataFrame(liste).transpose()
     return pd.DataFrame(dfres)




