#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "libs/matfun.h"
#include "libs/geofun.h"

// Function to compute the area between the curve x = y^2 and the vertical line x = a
double area(double a) {
    return (2.0 / 3.0) * pow(a, 1.5);
}

// Function to find 'a' such that area from 0 to 'a' is half the area from 0 to 4
double findA(double total_area) {
    double low = 0.0, high = 4.0, mid;
    double half_area = total_area / 2.0;
    double tolerance = 1e-6;

    while ((high - low) > tolerance) {
        mid = (low + high) / 2.0;
        if (area(mid) < half_area) {
            low = mid;
        } else {
            high = mid;
        }
    }
    return (low + high) / 2.0;
}

// Function to write the result to a text file for Python plotting
void writeResultToFile(const char *filename, double a) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        perror("Error opening file");
        exit(EXIT_FAILURE);
    }
    fprintf(file, "Value of a: %lf\n", a);
    fclose(file);
}

int main() {
    // Calculate the total area between x = y^2 and x = 4
    double total_area = area(4.0);

    // Find the value of 'a' that divides the area into two equal parts
    double a = findA(total_area);

    // Write the value of 'a' to a text file
    writeResultToFile("result.txt", a);

    printf("The value of 'a' is: %lf\n", a);

    return 0;
}

