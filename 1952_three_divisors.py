class Solution:
    def is_prime(n):
        # We know 1 is not a prime number
        if n == 1:
            return False

        i = 2
        # This will loop from 2 to int(sqrt(x))
        while i*i <= n:
            # Check if i divides x without leaving a remainder
            if n % i == 0:
                # This means that n has a factor in between 2 and sqrt(n)
                # So it is not a prime number
                return False
            i += 1
            
        # If we did not find any factor in the above loop,
        # then n is a prime number
        return True

    def isThree(self, n: int) -> bool:
        check = n**0.5
        if check.is_integer():
            if Solution.is_prime(check):
                return True
            else:
                return False
        else:
            return False
