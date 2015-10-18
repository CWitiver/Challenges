# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

pal_one, pal_two = [x for x in range(100, 1000)]
products = []
palins = []


def make_prods(products):
    for i in range(len(pal_one)):
        prod = pal_one[i] * pal_two[i]
        products.append(prod)
    return products


def palindrome(products):
    for i in range(1, len(products)):
        p = str(products[i])
        if p == p[::-1]:
            palins.append(p)
    return products

make_prods(products)
palindrome(products)
print(max(products))
print(max(palins))

