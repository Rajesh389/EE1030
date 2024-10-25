import numpy as np
import matplotlib.pyplot as plt

# Read the value of 'a' from the text file
with open("result.txt", "r") as file:
    line = file.readline()
    a = float(line.split(":")[1].strip())

# Generate points for the curve x = y^2
y = np.linspace(-2, 2, 400)
x = y**2

# Plot the curve x = y^2
plt.plot(x, y, label=r"$x = y^2$", color="blue")

# Plot the line x = 4
plt.axvline(x=4, color="green", linestyle="--", label="x = 4")

# Plot the line x = a
plt.axvline(x=a, color="red", linestyle="-.", label=f"x = {a:.4f}")

# Add labels and legend
plt.xlabel("x")
plt.ylabel("y")
plt.title("Area Division of Curve $x = y^2$")
plt.legend()

# Show the plot
plt.grid(True)
plt.show()

