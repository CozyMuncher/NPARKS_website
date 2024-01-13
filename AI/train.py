import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

# Loading the data
data = pd.read_csv('training_data.csv', header=None)  # Replace with the correct path

# Splitting the data into features and target
X = data.iloc[:, :-1]  # All rows, all columns except the last
y = data.iloc[:, -1]   # All rows, just the last column

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Optionally: Evaluate the model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f'Model accuracy: {accuracy}')

# Save the model
joblib.dump(model, 'trained_model.joblib')
