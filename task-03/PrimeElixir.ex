defmodule PrimeNumbers do
  def is_prime(1), do: false
  def is_prime(n) when n > 1, do: is_prime(n, 2)

  defp is_prime(n, divisor) when divisor * divisor > n, do: true
  defp is_prime(n, divisor) when rem(n, divisor) == 0, do: false
  defp is_prime(n, divisor), do: is_prime(n, divisor + 1)

  def print_primes(from, to) when from <= to do
    if is_prime(from) do
      IO.puts(from)
    end
    print_primes(from + 1, to)
  end

  def print_primes(_from, _to), do: :ok
end
 age = IO.gets("enter the number :  ")
 n = String.strip(age)
 new_age = String.to_integer(n)
PrimeNumbers.print_primes(1, new_age)