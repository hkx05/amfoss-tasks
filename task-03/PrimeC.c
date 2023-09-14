#include <stdbool.h>
#include <stdio.h>

// Function to check if a given number is prime
bool isPrime(int n)
{
    // Since 0 and 1 are not prime, return false.
    if (n == 1 || n == 0)
        return false;

    // Run a loop from 2 to n-1
    for (int i = 2; i < n; i++) {
        // If the number is divisible by i, then n is not a prime number.
        if (n % i == 0)
            return false;
    }
    // Otherwise, n is a prime number.
    return true;
}

int main()
{
    int N;

    printf("Enter the value of N: ");
    scanf("%d", &N);

    // Check for every number from 1 to N
    for (int i = 1; i <= N; i++) {
        // Check if the current number is prime
        if (isPrime(i))
            printf("%d ", i);
    }

    return 0;
}
