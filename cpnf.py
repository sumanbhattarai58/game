import pandas as pd

# Step 1: Create a simple dataset
data = {
    'Car Brand': ['Toyota', 'Ford', 'BMW', 'Toyota', 'BMW'],
    'Price': [20000, 25000, 55000, 21000, 53000]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Step 2: Convert 'Car Brand' to dummy variables
dummies = pd.get_dummies(df['Car Brand'])

print("\nDummy Variables:")
print(dummies)

# Step 3: Add the dummy variables back to the original DataFrame (optional)
df_with_dummies = pd.concat([df, dummies],axis=1)

print("\nDataFrame with Dummy Variables:")
print(df_with_dummies)

# Step 4: Optionally, you can drop the original 'Car Brand' column if you want
df_final = df_with_dummies.drop('Car Brand', axis=1)

print("\nFinal DataFrame (without 'Car Brand'):")
print(df_final)
