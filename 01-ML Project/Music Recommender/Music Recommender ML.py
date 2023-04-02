# 1. import data 
# 2. Clean Duplicate data
# 3. Split the data into Training /Teat sets
# 4. Create a Module 
# 5. Train the Module
# 6. Make Predicitions
# 7. Evaluate and Improve


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib
from sklearn import tree


from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

music_data=pd.read_csv("C:/Users/moham/Downloads/music.csv")
X=music_data.drop(columns=['genre'])
Y=music_data['genre']
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)

model=DecisionTreeClassifier()
model.fit(X_train,Y_train)

# tree.export_graphviz(model,out_file='music-recommender.dot',feature_names=['age','gender'],class_names=sorted(Y.unique()),label='all',rounded=True,filled=True)

# model=joblib.load ('music-recommender.joblib')
# predicition=model.predict([[21,1]])
# predicition
# predictions=model.predict(X_test)
# predictions
# score=accuracy_score(Y_test,predictions)
# score
