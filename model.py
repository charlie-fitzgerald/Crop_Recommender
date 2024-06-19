import pandas as pd
import joblib
import numpy as np
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.svm import SVC
import seaborn as sns

# create data frame from csv file
df = pd.read_csv("Crop_Recommendation.csv")

# Creating the independent and dependent variables
X = df.drop(columns=['Crop']).values
y = df['Crop']

# split data into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# creating confusion matrix
# clf = SVC(random_state=0)
#
# clf.fit(X_train, y_train)
#
# SVC(random_state=0)
#
# ConfusionMatrixDisplay.from_estimator(clf, X_test, y_test, xticks_rotation='vertical')
#
# plt.show()


# creating machine learning model using Decision Tree and training data
# model = DecisionTreeClassifier()
# model.fit(X_train, y_train)
#
# saving model
# joblib.dump(model, 'crop-recommender.model')
#
model = joblib.load('crop-recommender.model')

predictions = model.predict(X_test)


# testing the accuracy of the model
score = accuracy_score(y_test, predictions)
print(score)

#
# # histogram
# df.hist(xlabelsize=2)
# plt.show()
#
# # scatter matrix
# scatter_matrix(df)
# plt.show()

# correlogram. https://seaborn.pydata.org/generated/seaborn.pairplot.html#seaborn.pairplot
# sns.pairplot(df, hue="Crop")
# plt.show()
