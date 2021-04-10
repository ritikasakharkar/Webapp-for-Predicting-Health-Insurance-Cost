# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataset = pd.read_csv('insurance.csv')

X = dataset.iloc[:, :5]

#Converting words to integer values
def convert_to_int(word):
    word_dict = {'female':1, 'male':0, 'yes':1, 'no':0}
    return word_dict[word]

X['sex'] = X['sex'].apply(lambda x : convert_to_int(x)) 
X['smoker'] = X['smoker'].apply(lambda x : convert_to_int(x))
X['bmi'] = X['sex'] + X['bmi'] + X['smoker']
X = X.drop([1, 4])
y = dataset.iloc[:, -1]

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with training data
regressor.fit(X, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2,3,4]]))