import matplotlib.pyplot as plt

# Define the coordinates of points A, B, and C
a, b, c = 1, 2, 3  # You can change these values as needed
A = (a, b + c)
B = (b, c + a)
C = (c, a + b)

# Extract x and y coordinates for plotting
x_coords = [A[0], B[0], C[0]]
y_coords = [A[1], B[1], C[1]]

# Plot the points A, B, C
plt.figure(figsize=(8, 6))
plt.plot(x_coords, y_coords, 'ro-', label='Line through A, B, C')
plt.scatter(*A, color='blue', label=f'A({A[0]}, {A[1]})')
plt.scatter(*B, color='green', label=f'B({B[0]}, {B[1]})')
plt.scatter(*C, color='purple', label=f'C({C[0]}, {C[1]})')

# Annotate the points
plt.text(A[0], A[1], 'A', fontsize=12, ha='right')
plt.text(B[0], B[1], 'B', fontsize=12, ha='right')
plt.text(C[0], C[1], 'C', fontsize=12, ha='right')

# Set labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Collinear Points A, B, C')
plt.grid(True)
plt.legend()
plt.show()
