#1. A function that takes two integers and computes product through addition
def multiply(a,b):
    if b == 0:
        return 0
    elif b > 0:
        return a + multiply(a, b-1)
    else:
        return -multiply(a, -b) # For the negative case of b


#2. Recursive function for computing the result of an exponent equation
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)


#3. Recursive function printing number from n to 0
def countdown(n):
    if n < 0:
        return
    print(n)
    countdown(n-1)


#4. Recursive function printing numbers from 0 to n
def countup(n, i =0):
    if i > n:
        return
    print(i)
    countup(n, i+1)


#5. Recursive function that outputs a string input in reverse
def reverse_string(s):
    if len(s) == 0:
        return ''
    else:
        return s[-1] + reverse_string(s[:-1])


#6. Recursive function that checks whether a number is a prime number
def prime(n, divisor=None):
    if n<2:
        return False
    if divisor is None:
        divisor = n-1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return prime(n, divisor - 1)


#7. Fibonacci sequence
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
 print( multiply(2, -4))
print( power(2, 1))
print( countdown(5))
print( countup(5))
print(reverse_string("Cool"))
print( prime(5))
print( fibonacci(10))




