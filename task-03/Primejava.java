import java.io.*;
import java.util.Scanner;
class GFG
{
     static boolean isPrime(int n){
          if(n==1||n==0)return false;
   
          for(int i=2; i<n; i++)
          {
                if(n%i==0)return false;
          }
          return true;
    }
    public static void main (String[] args)
    {
        int N;
        System.out.println("Enter the integer: ");
        Scanner s = new Scanner(System.in);
        N = s.nextInt();
        for(int i=1; i<=N; i++)
        {
            if(isPrime(i)) 
            {
                System.out.print(i + " ");
            }
        }
 
    }
}
