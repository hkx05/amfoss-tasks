#include <bits/stdc++.h>
#include <iostream>
using namespace std;
 
// function to check if a given number is prime
bool isPrime(int n)
{
    // since 0 and 1 is not prime return false.
    if (n == 1 || n == 0)
        return false;
 
    // Run a loop from 2 to n-1
    for (int i = 2; i < n; i++) {
        // if the number is divisible by i, then n is not a
        // prime number.
        if (n % i == 0)
            return false;
    }
    // otherwise, n is prime number.
    return true;
}
 
// Driver code
int main()
{
    int N;
    cout<<"Enter the value of N : ";
    cin>>N;
    // check for every number from 1 to N
    for (int i = 1; i <= N; i++) {
        // check if current number is prime
        if (isPrime(i))
            cout << i << " ";
    }
 
    return 0;
}