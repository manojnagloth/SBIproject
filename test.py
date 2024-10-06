def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers_up_to_100():
    """Print all prime numbers up to 100."""
    primes = []
    for num in range(101):
        if is_prime(num):
            primes.append(num)
    return primes

# Call the function and print the result
print(prime_numbers_up_to_100())
