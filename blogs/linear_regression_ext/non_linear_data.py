import numpy as np
import matplotlib.pyplot as plt

# 1. Generate 10 points with a gentle curve (less U-shaped)
# We use x from -2 to 8 to show just the beginning of the curve's turn
np.random.seed(42)
x = np.linspace(-2, 8, 10)
# Relationship: y = 0.7 * x^2 + noise
y = 0.7 * x**2 + np.random.normal(0, 3, 10)

# 2. Calculate the linear best fit line (y = mx + c)
slope, intercept = np.polyfit(x, y, 1)
y_fit = slope * x + intercept

# 3. Visualization setup
# Using a clean style for a modern look
plt.style.use('seaborn-v0_8-muted')
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the data points (Purple)
ax.scatter(x, y, color='#9B59B6', label='Data Points ($n=10$)', s=120, 
           edgecolors='black', alpha=0.9, zorder=3)

# Plot the linear best fit line (Dotted-Dashed, Green)
ax.plot(x, y_fit, color='#27AE60', linestyle='-.', linewidth=2.5, 
        label='Linear Best Fit', zorder=2)

# Styling and Labels
ax.set_title('Gentle Curved Data with Linear Best Fit', fontsize=16, pad=20, weight='bold')
ax.set_xlabel('$x$ Values', fontsize=12)
ax.set_ylabel('$y$ Values', fontsize=12)

# Aesthetic cleanup (Removing top/right spines)
ax.grid(True, linestyle='--', alpha=0.4)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add legend
ax.legend(frameon=True, facecolor='white', framealpha=1)

# Save the visualization
plt.tight_layout()
plt.savefig('gentle_curve_plot.png', dpi=300)