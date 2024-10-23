#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
double integrand(double y, double a) {
    return a - y * y;
}

double integrate(double a, double upper_limit, int n) {
    double h = (2 * upper_limit) / n;  
    double sum = 0.5 * (integrand(-upper_limit, a) + integrand(upper_limit, a));

    for (int i = 1; i < n; i++) {
        double y = -upper_limit + i * h;
        sum += integrand(y, a);
    }
    return sum * h;
}

double find_a(double total_area) {
    double low = 0, high = 4, mid;
    double half_area = total_area / 2;
    while (high - low > 1e-6) {
        mid = (low + high) / 2;
        double area = integrate(mid, sqrt(mid), 1000);  

        if (area < half_area) {
            low = mid;
        } else {
            high = mid;
        }
    }
    return mid;
}

int main() {
    // Open output.txt to write the result
    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    double total_area = integrate(4, 2, 1000);  
    double a = find_a(total_area);

    fprintf(file, "The value of a is: %.6f\n", a);
    fclose(file);

    return 0;
}

