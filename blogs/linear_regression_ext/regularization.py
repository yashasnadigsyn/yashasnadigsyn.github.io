import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression, Ridge

# 1. Create Synthetic Data (A simple Sine wave + Random Noise)
np.random.seed(42)
def true_fun(X):
    return np.cos(1.5 * np.pi * X)

n_samples = 30
X = np.sort(np.random.rand(n_samples))
y = true_fun(X) + np.random.randn(n_samples) * 0.1  # Adding the "Noise"

X_test = np.linspace(0, 1, 100)

# 2. Setup the Models
# We use a degree-15 polynomial. This gives the model 15 "weights" to play with.
# For 30 data points, 15 weights is plenty of room to overfit.
degree = 15

# Model A: Standard Linear Regression (No Regularization)
no_reg_model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
no_reg_model.fit(X[:, np.newaxis], y)

# Model B: Ridge Regression (L2 Regularization)
# alpha is the 'lambda' tuning knob from Bishop's book.
ridge_model = make_pipeline(PolynomialFeatures(degree), Ridge(alpha=0.1))
ridge_model.fit(X[:, np.newaxis], y)

# 3. Visualization
plt.figure(figsize=(12, 6))

# Plotting the Training Data
plt.scatter(X, y, color='navy', s=30, marker='o', label="Training Data (with noise)")
plt.plot(X_test, true_fun(X_test), color='green', label="True Function (The Truth)")

# Plotting the Overfitted Model
y_pred_no_reg = no_reg_model.predict(X_test[:, np.newaxis])
plt.plot(X_test, y_pred_no_reg, color='red', label=f"No Regularization (Weights exploded!)")

# Plotting the Regularized Model
y_pred_ridge = ridge_model.predict(X_test[:, np.newaxis])
plt.plot(X_test, y_pred_ridge, color='orange', label=f"Ridge Regularization (Alpha=0.1)")

plt.ylim(-2, 2)
plt.legend(loc="best")
plt.title(f"Polynomial Degree {degree}: The Battle against Overfitting")
plt.show()

# 4. Check the Weights (The "Skyrocketing" Proof)
print("--- Weight Comparison ---")
no_reg_weights = no_reg_model.steps[1][1].coef_
ridge_weights = ridge_model.steps[1][1].coef_

print(f"Max Weight (No Reg):    {np.max(np.abs(no_reg_weights)):.2f}")
print(f"Max Weight (With Ridge): {np.max(np.abs(ridge_weights)):.2f}")