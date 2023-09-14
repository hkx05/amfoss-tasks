package main

// fmt package provides the function to print anything
import "fmt"

func initializeArray(primeArray []bool, N int) {
   // initializing the array with true
   for i := 0; i < N; i++ {
      primeArray[i] = true
   }
}
func printPrimeNumbersBeforeN(N int) {
   primeArray := make([]bool, N+1)
   initializeArray(primeArray, N+1)
   
   // running the for loop from 1 to under root N
      for i := 2; i*i <= N; i++ {
         if primeArray[i] {

            // This for loop is running from the square of upper
            // loop index until N and traversing over the multiple of i
            // by increasing the j index by i
            for j := i * i; j <= N; j = j + i {
               primeArray[j] = false
            }
         }
      }

      // printing the prime number by checking the status of primeArray status
      for i := 2; i <= N; i++ {
         if primeArray[i] {
            fmt.Println(i)
         }
      }
   }
   func main() {
      //declaring the variable N till which we have to find the Prime Numbers 
      var N int
    
      fmt.Println("Enter the value of N.")

   // Taking the input of N from the user
   fmt.Scanln(&N)
   fmt.Println()

   // calling the function to find and print the prime numbers
   printPrimeNumbersBeforeN(N)
}