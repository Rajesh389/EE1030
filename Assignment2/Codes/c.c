#include <stdio.h>
#include <math.h>

// Function to calculate the area of the triangle formed by three points
double calculate_area(int x1, int y1, int x2, int y2, int x3, int y3) {
    return 0.5 * fabs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2));
}

int main() {
    // Coordinates of the points A, B, C
    int a, b, c;
    printf("Enter the values of a, b, and c: ");
    scanf("%d %d %d", &a, &b, &c);

    // Coordinates of points A, B, and C
    int x1 = a, y1 = b + c;
    int x2 = b, y2 = c + a;
    int x3 = c, y3 = a + b;

    // Calculate the area
    double area = calculate_area(x1, y1, x2, y2, x3, y3);

    // Check if the points are collinear
    if (area == 0) {
        printf("The points A(%d, %d), B(%d, %d), and C(%d, %d) are collinear.\n", x1, y1, x2, y2, x3, y3);
    } else {
        printf("The points A(%d, %d), B(%d, %d), and C(%d, %d) are not collinear.\n", x1, y1, x2, y2, x3, y3);
    }

    return 0;
}

