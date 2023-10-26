#include <stdio.h>
#include <math.h>

float calculate_pi() {
    /*
    1/1 + 1/4 + 1/9 + 1/16 + 1/25 + ... = (pi^2)/6
    */
    float a = 0;
    for (int i = 1; i <= 100000000; i++) {
        a += 1 / pow(i, 2);
    }
    printf("%f\n", sqrt(a * 6));
}

int main() {
    calculate_pi();
    return 0;
}
