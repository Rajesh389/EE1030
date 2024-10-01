# Code by GVV Sharma
# September 12, 2023
# Revised July 21, 2024
# Released under GNU GPL

import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as LA

# Define the coordinates of points A, B, and C
a, b, c = 1, 2, 3  # You can change these values as needed

# Given points
A = np.array([a, b + c])
B = np.array([b, c + a])
C = np.array([c, a + b])

# Print the rank of the matrix formed by vectors B-A and C-A
print("Rank of the matrix formed by vectors B-A and C-A:", LA.matrix_rank(np.column_stack((B - A, C - A))))

# Generate line points
def line_gen(P1, P2, num_points=10):
    """Generate points on the line segment between P1 and P2."""
    return np.array([P1 + (P2 - P1) * t for t in np.linspace(0, 1, num_points)]).T

# Generate points for lines AB and BC
x_AB = line_gen(A, B)
x_BC = line_gen(B, C)

# Plotting all lines
plt.plot(x_AB[0, :], x_AB[1, :], label='$AB$', color='blue')
plt.plot(x_BC[0, :], x_BC[1, :], label='$BC$', color='green')

# Scatter plot of the points
tri_coords = np.array([A, B, C])
plt.scatter(tri_coords[:, 0], tri_coords[:, 1], color='red')

# Labeling the coordinates
vert_labels = ['A', 'B', 'C']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({tri_coords[i, 0]}, {tri_coords[i, 1]})',
                 (tri_coords[i, 0], tri_coords[i, 1]),
                 textcoords="offset points",
                 xytext=(0, 10),
                 ha='center')

# Set labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Collinear Points A, B, C')
plt.grid(True)
plt.legend()
plt.savefig('Figure_1.jpg')
plt.show()

