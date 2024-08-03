def is_prime(n):
    isPrime = True

    if n <= 1:
        isPrime = False
        return isPrime

    for i in range(n - 1, 1, -1):
        if(n % i == 0):
            isPrime = False
            return isPrime
    return isPrime

def print_prior_primes(n):
    for i in range(2, n):
        if is_prime(i):
            print(i, end=" ")
    print()

numb = int(input("Input the number to know if is Prime: \n"))
if is_prime(numb):
    print(f"{numb} is a prime number.")
else:
    print(f"{numb} is not a prime number.")
    print(f"The prime numbers before {numb} are:")
    print_prior_primes(numb)