import numpy as np
from numpy import *
from sklearn import datasets
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
import warnings
warnings.filterwarnings("ignore")

iris=datasets.load_iris()#iris dataset 5cols
x,y=iris.data[:,1:3],iris.target#first paramete for row, and second for col,here : in row is for all row
m1=LogisticRegression(random_state=1)
m2=RandomForestClassifier(random_state=1)
m3=GaussianNB()
m4=DecisionTreeClassifier()

labels=['Logistic Regression','Random Forest', 'Naive Bayes', 'Decision Tree']
for m, label in zip([m1,m2,m3,m4],labels):
    scores=model_selection.cross_val_score(m,x,y,cv=5,scoring='accuracy')
    print("Accuracy: %0.2f [%s]" %(scores.mean(), label))
voting_clf_hard=VotingClassifier(estimators=[(labels[0],m1),
                                             (labels[1],m2),
                                             (labels[2],m3),
                                             (labels[3],m4)],
                                 voting='hard')
scores1=model_selection.cross_val_score(voting_clf_hard,x,y,cv=5,scoring='accuracy')
print("Accuracy of combined Model Using Hard Voting: %0.2f"  %(scores1.mean()))
