from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# Create some example data
np.random.seed(42)
x = np.random.rand(10) * 10
y = 3 * x + np.random.normal(0, 3, 10)
data = pd.DataFrame({'X': x, 'Y': y})

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    data[['X']], data['Y'], test_size=0.2, random_state=42)

# Print each part
print("📘 X_train (features for training):")
print(X_train)
print("\n📘 X_test (features for testing):")
print(X_test)
print("\n🎯 y_train (targets for training):")
print(y_train)
print("\n🎯 y_test (targets for testing):")
print(y_test)
