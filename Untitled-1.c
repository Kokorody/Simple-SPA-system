#include <stdio.h>
#include <string.h>

// Function to calculate net price based on package, duration, and membership
float calculate_price(char package_type, float duration, char is_member[]) {
    float discount = 0, price = 0;

    if (package_type == 'A' && duration == 1) {
        price = 31;
        if (strcmp(is_member, "Yes") == 0)
            discount = 0.05;
    } else if (package_type == 'A' && duration > 1) {
        price = 31 * duration;
    } else if (package_type == 'B' && duration < 1) {
        price = 21;
    } else if (package_type == 'C' && duration == 2) {
        price = 95;
        if (strcmp(is_member, "Yes") == 0)
            discount = 0.1;
    } else if (package_type == 'C' && duration < 2) {
        price = 85;
    } else if (package_type == 'C' && duration > 2) {
        price = 95 + 42 * (duration - 2);
    }

    float net_price = is_member[0] == 'Y' ? price - (price * discount) : price;
    return net_price;
}

// Function to generate receipt
void generate_receipt(char name[], char package_type, float duration, char is_member[], float net_price) {
    printf("\n--------------------- Receipt ---------------------\n");
    printf("Customer Name: %s\n", name);
    printf("Package Type: %c\n", package_type);
    printf("Treatment Duration: %.2f hour(s)\n", duration);
    printf("Membership: %s\n", is_member);
    printf("Net Price (USD): %.2f\n", net_price);
    printf("--------------------------------------------------\n\n");
}

int main() {
    char name[100];
    char package;
    float duration;
    char membership[3];

    printf("Enter your name: ");
    scanf("%s", name);
    printf("Enter the type of package (A, B, or C): ");
    scanf(" %c", &package);
    printf("Enter the treatment duration in hours: ");
    scanf("%f", &duration);
    printf("Are you a member? (Yes or No): ");
    scanf("%s", membership);

    char valid_packages[] = {'A', 'B', 'C'};
    int valid_package = 0;
    for (int i = 0; i < sizeof(valid_packages) / sizeof(valid_packages[0]); i++) {
        if (package == valid_packages[i]) {
            valid_package = 1;
            break;
        }
    }

    if (valid_package) {
        float net_price = calculate_price(package, duration, membership);
        if (net_price != 0) {
            generate_receipt(name, package, duration, membership, net_price);
        } else {
            printf("Invalid Honeybliss Spa Package\n");
        }
    } else {
        printf("Invalid Honeybliss Spa Package\n");
    }

    return 0;
}