import numpy as np
import matplotlib.pyplot as plt

# Function to read the value from output.txt
def read_value_from_file(filename):
    with open(filename, 'r') as file:
        value = float(file.readline().strip())
    return value

# Function to plot the area between the curve x = y^2 and the line x = 4
def plot_area(a_value):
    y = np.linspace(-2.5, 2.5, 400)  # y-values from -2.5 to 2.5
    curve = y**2  # x = y^2
    line = np.full_like(y, 4)  # Line at x = 4

    # Create a mask for the area to fill
    x_fill = np.where((curve >= 0) & (curve <= 4))  # Indices where the area exists

    plt.figure(figsize=(8, 6))
    plt.plot(curve, y, label=r'$x = y^2$', color='blue')  # Curve
    plt.plot(line, y, label=r'$x = 4$', color='orange')  # Line
    plt.axvline(x=a_value, color='green', linestyle='--', label=f'$x = {a_value:.4f}$')  # Line x = a

    # Fill the area between the curve and the line
    plt.fill_betweenx(y[x_fill], curve[x_fill], line[x_fill], where=(line[x_fill] >= curve[x_fill]), color='lightgrey', alpha=0.5)

    plt.xlim(0, 5)
    plt.ylim(-2.5, 2.5)
    plt.title('Area between the Curve and the Line')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.legend()
    plt.grid()
    plt.show()
    plt.savefig('/home/rajesh/EE1030/matgeo-02/fig')

# Main execution
if __name__ == "__main__":
    a_value = read_value_from_file('output.txt')
    plot_area(a_value)

