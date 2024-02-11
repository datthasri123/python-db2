import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import PyQt5

# Generate synthetic data
np.random.seed(42)
X1 = 2 * np.random.rand(100, 1)
X2 = 3 * np.random.rand(100, 1)
Y = 4 + 3 * X1 + 2 * X2 + np.random.randn(100, 1)

# Create a design matrix X with X1 and X2
X = np.c_[X1, X2]

# Fit linear regression model
model = LinearRegression()
model.fit(X, Y)

# Get the coefficients
b0 = model.intercept_[0]
b1, b2 = model.coef_[0]

# Print the coefficients
print(f"b0 (intercept): {b0}")
print(f"b1 (coefficient for X1): {b1}")
print(f"b2 (coefficient for X2): {b2}")

# Plot the data points and the fitted plane
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X1, X2, Y, color='blue', label='Data points')
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('Y')

# Create a meshgrid for the plane
x1_plane, x2_plane = np.meshgrid(np.linspace(min(X1), max(X1), 100), np.linspace(min(X2), max(X2), 100))
y_plane = b0 + b1 * x1_plane + b2 * x2_plane

# Plot the fitted plane
ax.plot_surface(x1_plane, x2_plane, y_plane, color='r', alpha=0.5, label='Fitted Plane')

plt.title('Multiple Linear Regression')
plt.legend()
plt.show()
