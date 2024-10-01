#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "libs/matfun.h"
#include "libs/geofun.h"

int main() {
    // Declare variables for a, b, c
    float a, b, c;
    
    // Prompt the user for input
    printf("Enter value for a: ");
    scanf("%f", &a);
    
    printf("Enter value for b: ");
    scanf("%f", &b);
    
    printf("Enter value for c: ");
    scanf("%f", &c);
    
    // Open the file values.dat for writing
    FILE *file = fopen("values.dat", "w");
    
    // Check if the file opened successfully
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1; // Exit with an error code
    }
    
    // Calculate the coordinates of points A, B, and C
    float A_x = a;
    float A_y = b + c;
    float B_x = b;
    float B_y = c + a;
    float C_x = c;
    float C_y = a + b;
    
    // Write the coordinates to the file
    fprintf(file, "A: (%.2f, %.2f)\n", A_x, A_y);
    fprintf(file, "B: (%.2f, %.2f)\n", B_x, B_y);
    fprintf(file, "C: (%.2f, %.2f)\n", C_x, C_y);
    
    // Close the file
    fclose(file);
    
    printf("Coordinates have been saved to values.dat\n");
    
    return 0; // Exit successfully
}
