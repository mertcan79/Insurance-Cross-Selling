import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV,RandomizedSearchCV
from sklearn.metrics import recall_score,precision_score,f1_score,accuracy_score, confusion_matrix, classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('data/test.csv')

df.drop(columns = 'id', inplace = True)
df['Gender'] = df['Gender'].map({'Female':1, 'Male':0})

df['Vehicle_Damage'] = df['Vehicle_Damage'].map({'Yes':1, 'No':0})

df['Vehicle_Age'] = df['Vehicle_Age'].map({'1-2 Year':1, '< 1 Year':0, '> 2 Years': 2})

X = df.drop(columns = [ 'Driving_License','Response', 'Region_Code', 'Policy_Sales_Channel', 'Gender', 'Vintage'])
y = df['Response']

import imblearn
from imblearn.over_sampling import SMOTE

sm = SMOTE(random_state = 42)

X_train_sm, y_train_sm = sm.fit_sample(X, y)

df_smote = pd.concat([X_train_sm, y_train_sm], axis = 1)

modelSMOTERF = RandomForestClassifier()

modelSMOTERF.fit(X_train_sm, y_train_sm)

y_pred_SMOTE_RF = modelSMOTERF.predict(X_test)

y_pred_SMOTE_RF.to_csv("predictions.csv")