
import numpy as np
import matplotlib.pyplot as plt

# Input number of data points
n = int(input("Enter number of points (minimum 5): "))

x_pts = []
y_pts = []

print("Enter points as x y:")
for i in range(n):
    x, y = map(float, input(f"Point {i+1}: ").split())
    x_pts.append(x)
    y_pts.append(y)

x_target = float(input("\nEnter x to interpolate: "))


# Lagrange Interpolation Function
def lagrange(x, x_pts, y_pts):
    result = 0.0

    for i in range(len(x_pts)):
        L = 1.0

        for j in range(len(x_pts)):
            if i != j:
                L *= (x - x_pts[j]) / (x_pts[i] - x_pts[j])

        result += y_pts[i] * L

    return result


# Polynomial orders
orders = [2, 3, 4, 5]

for order in orders:

    if n < order:
        print(f"\nNot enough points for {order-1}th order polynomial.")
        continue

    # Select points for current order
    x_data = x_pts[:order]
    y_data = y_pts[:order]

    # Calculate interpolated value
    result = lagrange(x_target, x_data, y_data)

    print(f"\n{'='*50}")
    print(f"{order-1}th Order Lagrange Polynomial")
    print(f"{'='*50}")

    # Print polynomial equation using polynomial coefficients
    coefficients = np.polynomial.polynomial.polyfit(
        x_data, y_data, order - 1
    )

    equation = f"P(x) = {coefficients[0]:.6f}"

    for i in range(1, order):
        if abs(coefficients[i]) > 1e-10:
            sign = "+" if coefficients[i] >= 0 else "-"
            equation += f" {sign} {abs(coefficients[i]):.6f}x"
            if i > 1:
                equation += f"^{i}"

    print("Polynomial:", equation)
    print(f"Interpolated Value P({x_target}) = {result:.6f}")

    # Generate smooth curve
    x_curve = np.linspace(min(x_data), max(x_data), 200)
    y_curve = [lagrange(x, x_data, y_data) for x in x_curve]

    # Plot each order separately
    plt.figure(figsize=(7, 5))

    plt.plot(x_curve, y_curve, label=f"{order-1}th Order Polynomial")
    plt.scatter(x_data, y_data, color="red", label="Given Points")
    plt.scatter(x_target, result, color="green",
                label="Interpolated Point")

    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.title(f"{order-1}th Order Lagrange Interpolation")
    plt.legend()
    plt.grid(True)
    plt.show()
