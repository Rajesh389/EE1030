#include <stdio.h>
#include <math.h>

// Function to calculate the next x value
float x_n(float x, float h) {
    return x + h;
}

// Function to calculate the first y value (y_1) using the first derivative
float y_1(float y_0, float dy, float h) {
    return h * dy + y_0; // dy is the first derivative of y at x=0
}

// Function to calculate subsequent y values using the finite difference method
float y_n(float y_1, float y_0, float h, float x_0) {
    return y_1 * (2 - h * x_0) + y_0 * (1 + h * x_0 - h * h * x_0) + h * h * x_0;
}
