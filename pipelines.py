import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load your data
df = pd.read_csv(r"C:\Users\acer\python workspace\authors_listing.csv")

# Input and Output
X = df[["daily_read"]]
y = df["percentage"]

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the pipeline
pipe = Pipeline([
    ('scaler', StandardScaler()),         # Step 1: Scale the input
    ('model', LinearRegression())         # Step 2: Fit linear regression
])

# Fit the pipeline to training data
pipe.fit(X_train, y_train)

# Predict using the pipeline
y_pred = pipe.predict(X_test)

# Print results
print("Predicted values:", y_pred[:5])
print("R² score:", r2_score(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
# Old method (no scaling)
lm = LinearRegression()
lm.fit(X, y)
print("Raw model coef:", lm.coef_)
print("Raw model intercept:", lm.intercept_)

# New pipeline method (with scaling)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LinearRegression())
])
pipe.fit(X, y)
print("Pipeline model coef:", pipe.named_steps['model'].coef_)
print("Pipeline model intercept:", pipe.named_steps['model'].intercept_)
