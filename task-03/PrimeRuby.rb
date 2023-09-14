def is_prime(num)
    return false if num <= 1
  
    (2..Math.sqrt(num)).each do |i|
      return false if num % i == 0
    end
  
    true
  end
  
  def print_primes_up_to_n(n)
    (2..n).each do |i|
      puts i if is_prime(i)
    end
  end
  
  print "Enter the value of N: "
  n = gets.chomp.to_i
  
  if n < 1
    puts "Invalid input. Please enter a positive integer."
  else
    puts "Prime numbers from 1 to #{n}:"
    print_primes_up_to_n(n)
  end