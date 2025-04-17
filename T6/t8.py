def find_primes(n):
    primes = []
    for num in range(2, n+1):
        is_prime = True
        for p in primes:
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

n = int(input("Enter n: "))
print("Primes ≤ n:", find_primes(n))