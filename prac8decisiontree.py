#for building the model
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn .model_selection import train_test_split#split the data into training and testing
from sklearn import metrics#for accuarcy
#for plotting the tree
from matplotlib import pyplot as plt
from sklearn import tree

col_names=['Reservation','Raining','BadService','Satur','Result']
hoteldata=pd.read_csv("dtree.csv",header=None,names=col_names)#pd will read the file on the behalf of panda
feature_cols=['Reservation','Raining','BadService','Satur']
X=hoteldata[feature_cols]#Feature Columns
y=hoteldata.Result#Target Variable

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=1)#variables used for training and testing
#0.3 indicates 30% of data will be used for testing
#Random State is to check and validate the data when running the code
#multiple times.Setting random_state a fixed value will guarantee that
#same sequence of random
print(hoteldata)
print("x train data: ", X_train)
print("y train data: ", y_train)
print("x test data: ", X_test)
print("y test data: ", y_test)
clf=DecisionTreeClassifier(criterion="entropy",max_depth=5)
clf=clf.fit(X_train,y_train)
#Predict the response for test dataset
y_pred=clf.predict(X_test)
print("ytest = ",X_test)
print("ypred = ",y_pred)
#accuracy of the model
print("Accuracy:",metrics.accuracy_score(y_test,y_pred))
fig=plt.figure(figsize=(25,20))
t=tree.plot_tree(clf,
                 feature_names=feature_cols,
                 class_names=['Leave','Wait'],
                 filled=True)
fig.savefig("decision_tree.png")
