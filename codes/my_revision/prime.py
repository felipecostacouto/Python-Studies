def is_prime(n):
    isPrime = True

    if n <= 1:
        isPrime = False
        return isPrime
# if a number has a factor larger than its square root, it must also have a corresponding factor smaller than the square root.
#Thus, if N has a factor larger than its square root, it must have a corresponding factor smaller than the square root. 
# This means we only need to check for factors up to the square root,
#  because any factor larger than the square root will already have been accounted for by a smaller factor.
    for i in range(2, int(n ** 0.5) + 1):
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