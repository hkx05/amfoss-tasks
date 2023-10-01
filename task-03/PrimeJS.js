function isPrime( n)
{
      if(n == 1 || n == 0) return false;
      for(var i = 2; i < n; i++)
      {
        if(n % i == 0) return false;
      }
      return true;
}

var N = prompt("Please enter an integer:");
  for(var i = 1; i <= N; i++)
  {
      if(isPrime(i)) {
        console.log( i );
      }
}
