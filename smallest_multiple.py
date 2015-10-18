# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

n = 1


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def least_common_m(x, y):
    m = x * y / gcd(x, y)
    return m

for i in range(1, 21):
     n = least_common_m(n, i)

print(n)

