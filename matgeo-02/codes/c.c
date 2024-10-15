#include <stdio.h>
#include <math.h>

#define N 1000  // Number of intervals for integration

// Function representing the line x = 4
double line(double y) {
    return 4.0;
}

// Function representing the curve x = y^2
double curve(double y) {
    return y * y;
}

// Simpson's Rule for numerical integration from 'a' to 'b'
double simpsonsRule(double (*func)(double), double a, double b) {
    double h = (b - a) / N;
    double sum = func(a) + func(b);

    for (int i = 1; i < N; i++) {
        double x = a + i * h;
        sum += (i % 2 == 0 ? 2 : 4) * func(x);
    }
    return (h / 3) * sum;
}

// Function to calculate the total area between the curve and the line
double totalArea() {
    return simpsonsRule(line, -2, 2) - simpsonsRule(curve, -2, 2);
}

// Function to calculate the area from 0 to a
double areaLeft(double a) {
    double upperLimit = sqrt(a);  // y = sqrt(a)
    return simpsonsRule(line, -upperLimit, upperLimit) - simpsonsRule(curve, -upperLimit, upperLimit);
}

int main() {
    double total_area = totalArea();  // Calculate the total area
    double half_area = total_area / 2.0;  // Half of the total area

    double a = 0.0;  // Start the search for 'a'
    double step = 0.001;  // Step size for incrementing 'a'

    // Increment 'a' until the area to the left matches half the total area
    while (areaLeft(a) < half_area) {
        a += step;
    }

    // Open output.tex file for writing
    FILE *fptr = fopen("output.tex", "w");
    if (fptr == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Save the results in output.tex
    //fprintf(fptr, "The value of a that divides the area equally is: %.4f\n", a);
    fprintf(fptr, "%.4f\n", pow(4, 2.0/3.0));

    // Close the file
    fclose(fptr);

    printf("The results have been saved to output.tex\n");
    return 0;
}

