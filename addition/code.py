#include <stdio.h>

void solve(double h, double y[], double dy[], int steps) {
    double x = 0.0;

    // Initial conditions
    y[0] = 0.0;  // Example: y(0) = 0
    dy[0] = 1.0; // Example: y'(0) = 1

    for (int i = 1; i <= steps; i++) {
        // Compute the second derivative ddy
        double ddy = x * x * dy[i - 1] + x * y[i - 1];

        // Update y and dy using finite difference
        y[i] = y[i - 1] + h * dy[i - 1];
        dy[i] = dy[i - 1] + h * ddy;

        // Increment x
        x += h;
    }
}
