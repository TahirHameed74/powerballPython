import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

from sklearn.metrics import mean_squared_error

def get_sec(time_str):
    """Get Seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


dataset = pd.read_csv('data.csv')
dataset.plot(x='Time', y ='N3', style='o') 
plt.xlabel('Time')  
plt.ylabel('N3')  
plt.show()

X = []
for i in dataset['Time']:
	X.append(get_sec(i))

X = np.asarray(X).reshape(-1,1)


y = dataset['N3'].values.reshape(-1,1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, y_train) #training the algorithm



y_pred = regressor.predict(X_test)

df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})

print()
print('mean square error:')
print(mean_squared_error(y_test, y_pred))

print()
print(df)

