import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read the value of 'a' from output.txt
try:
    with open('output.txt', 'r') as file:
        line = file.readline()
        a = float(line.split()[-1])  # Extract the value of 'a' from the line
except FileNotFoundError:
    print("Error: 'output.txt' not found. Ensure the C code generated the file.")
    exit()
except ValueError:
    print("Error: Couldn't read a valid number from 'output.txt'.")
    exit()

# Step 2: Define the range for y and corresponding x values
y = np.linspace(-2, 2, 1000)  # y values from -2 to 2
x_y2 = y ** 2  # Corresponding x = y^2 values

# Step 3: Create the plot
plt.figure(figsize=(8, 6))

# Plot the curve x = y^2
plt.plot(x_y2, y, label=r'$x = y^2$', color='blue')

# Plot the vertical line x = 4
plt.axvline(4, color='green', linestyle='--', label=r'$x = 4$')

# Plot the dividing line x = a
plt.axvline(a, color='red', linestyle='-.', label=f'$x = {a:.2f}$')

# Step 4: Shade the two areas with proper boolean masks
mask1 = x_y2 <= a  # Boolean mask for Area 1 (from curve to x = a)
mask2 = x_y2 >= a  # Boolean mask for Area 2 (from x = a to 4)

# Use fill_betweenx with matching mask sizes
plt.fill_betweenx(y, x_y2, a, where=mask1, color='skyblue', alpha=0.5, label='Area 1')
plt.fill_betweenx(y, a, 4, where=mask2, color='lightgreen', alpha=0.5, label='Area 2')

# Add labels, title, and legend
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Plot of Curves and Area Division')
plt.legend(loc='best')

# Display grid for better visualization
plt.grid(True)

# Step 5: Show the plot
plt.show()
plt.savefig('/home/rajesh/EE1030/matgeo-02/fig/fig.png')
