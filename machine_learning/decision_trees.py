import numpy as np 
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import metrics
#you are a medical researcher compiling data for study
#you need to build a model to find out which drug best suit the future patient
path= 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/drug200.csv'
my_data = pd.read_csv(path)
print(my_data.head())
print(my_data.info())
#output shows 4 out of 6 features(columns) shows categorical dataset so need to change to numerical dataset
#for this use of labelencoder
label_encoder=LabelEncoder()
my_data['Sex']=label_encoder.fit_transform(my_data['Sex'])
my_data['BP']=label_encoder.fit_transform(my_data['BP'])
my_data['Cholesterol']=label_encoder.fit_transform(my_data['Cholesterol'])
print(my_data.head())
print(my_data.isnull().sum())
#map the target variable to a numerical value to evaluate the coreration
drug_map ={'drugA':0,'drugB':1,'drugC':2,'drugX':'3','drugY':'4'}
my_data['Drug_num']=my_data["Drug"].map(drug_map) #works same as labelencoder
#print(my_data.head())
correlation_matrix = my_data.corr(numeric_only=True) 
print(correlation_matrix)
print(my_data.drop('Drug',axis=1).corr()['Drug_num'])
#drops the Drug column(categorical data), axis=1 means column wise
category_counts = my_data['Drug'].value_counts()
people_counts=my_data["Sex"].value_counts()
print(category_counts)
print(people_counts)
plt.bar(category_counts.index, category_counts.values, color='red') 
#.index is the label for each bar(like drugA,drugB...)
#.values is the height of each bar
plt.xlabel('Drug')
plt.ylabel('Count')
plt.title('Category Distribution')
plt.xticks(rotation=45)  # Rotate labels for better readability if needed
plt.show()
#modelling with decision tree classifier
#split the dataset into training and testing subsets.for this,first separate the target variable from input variable
y=my_data['Drug']
#X=my_data['BP','Cholesterol','Sex'] or
X=my_data.drop(['Drug','Drug_num'],axis=1)
X_trainset, X_testset, y_trainset, ytestset=train_test_split(X,y,test_size=0.3,random_state=32)
#now define the decision tree classifier
drugtree=DecisionTreeClassifier(criterion="entropy",max_depth=4)
drugtree.fit(X_trainset,y_trainset)
drugtree_predictions = drugtree.predict(X_testset)
print("Decision Trees's Accuracy: ", metrics.accuracy_score(ytestset, drugtree_predictions))
plot_tree(drugtree)
plt.show()
#now check the target variable using your own inputs
input_data={'Age':[25,35] ,'Sex':[1,0],'BP':[0,1],'Cholesterol':[1,0],'Na_to_K':[11.3,15.2]}
input_data_frame=pd.DataFrame(input_data)
prediction = drugtree.predict(input_data_frame)
for i, pred in enumerate(prediction):
    print(f"Prediction for input {i}: {pred}")