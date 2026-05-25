import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Set random seed for reproducibility
np.random.seed(42)

# 1. Generate synthetic data: y = x^2 + noise
x = np.linspace(-5, 5, 40)
y = x**2 + np.random.normal(0, 2, size=x.shape)

# Create the figure with two subplots
fig = plt.figure(figsize=(14, 6))

# --- Subplot 1: Original 1D Input Space ---
ax1 = fig.add_subplot(1, 2, 1)
ax1.scatter(x, y, color='blue', label='Data points (y ≈ x²)')

# Fit a simple linear model (y = mx + c) to show it fails
model_linear = LinearRegression()
model_linear.fit(x.reshape(-1, 1), y)
x_line = np.linspace(-6, 6, 100)
y_line = model_linear.predict(x_line.reshape(-1, 1))

ax1.plot(x_line, y_line, color='red', linestyle='--', label='Linear Fit (Flat Line)')
ax1.set_title('1. Original Space', fontsize=12)
ax1.set_xlabel('Input x')
ax1.set_ylabel('Target y')
ax1.legend()
ax1.grid(True, alpha=0.3)

# --- Subplot 2: Lifted Feature Space (2D Input) ---
ax2 = fig.add_subplot(1, 2, 2, projection='3d')

# Features: x1 = x, x2 = x^2
x1 = x
x2 = x**2

# Scatter plot in 3D: (x, x^2, y)
ax2.scatter(x1, x2, y, color='blue', s=30, label='Lifted points')

# Create a plane to show the linear fit in feature space
# In the space (x, x^2), the relationship y = x^2 is a flat plane: y = 0*x + 1*(x^2)
X1_surf, X2_surf = np.meshgrid(np.linspace(-6, 6, 10), np.linspace(0, 30, 10))
Y_surf = X2_surf  # The equation of the hyperplane

ax2.plot_surface(X1_surf, X2_surf, Y_surf, alpha=0.2, color='green')
ax2.set_title('2. Feature Space', fontsize=12)
ax2.set_xlabel('Feature 1: x')
ax2.set_ylabel('Feature 2: x²')
ax2.set_zlabel('Target y')

# Adjust viewing angle for better intuition
ax2.view_init(elev=20, azim=-60)

plt.tight_layout()
plt.show()