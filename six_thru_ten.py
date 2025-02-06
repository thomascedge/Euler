from testing.utils import Evaluation, Helper


def euler_six():
    """
    Problem 6: Sum Square Difference

    The sum of the squares of the first ten natural numbers is, 
    1^2 + 2^2 + 3^2 + ... + 10^2 = 385. The square of the sum of the first ten 
    natural numbers is, (1 + 2 + 3 + ... + 10)^2 = 55^2 = 3025. Hence the 
    difference between the sum of the squares of the first ten natural numbers and 
    the square of the sum is 3025 - 385 = 2640. Find the difference between the sum 
    of the squares of the first one hundred natural numbers and the square of the 
    sum.

    Time:   O(n)
    Space:  O(1)
    """

    sum_of_squares = square_of_sums = 0

    for num in range(1, 101):
        sum_of_squares += num * num
        square_of_sums += num

    square_of_sums *= square_of_sums

    return square_of_sums - sum_of_squares


def euler_seven():
    """
    Problem 7: 10001st Prime

    By listing the first six prime numbers: 2, 3, 5, 7, and 11, we can see that 
    the 6th prime is 13. What is the 10001st prime number?

    Time:   O(n)
    Space:  O(1)
    """

    iteration = 0
    num = 1

    while iteration != 10001:
        if Helper._is_prime_bool(num):
            iteration += 1

        num += 1

    return num


def euler_eight(string):
    """
    Problem 8: Largest Product in a Series

    The four adjacent digits in the 1000-digit number that have the greatest 
    product are 9 x 9 x 8 x 9 = 5832.

            73167176531330624919225119674426574742355349194934
            96983520312774506326239578318016984801869478851843
            85861560789112949495459501737958331952853208805511
            12540698747158523863050715693290963295227443043557
            66896648950445244523161731856403098711121722383113
            62229893423380308135336276614282806444486645238749
            30358907296290491560440772390713810515859307960866
            70172427121883998797908792274921901699720888093776
            65727333001053367881220235421809751254540594752243
            52584907711670556013604839586446706324415722155397
            53697817977846174064955149290862569321978468622482
            83972241375657056057490261407972968652414535100474
            82166370484403199890008895243450658541227588666881
            16427171479924442928230863465674813919123162824586
            17866458359124566529476545682848912883142607690042
            24219022671055626321111109370544217506941658960408
            07198403850962455444362981230987879927244284909188
            84580156166097919133875499200524063689912560717606
            05886116467109405077541002256983155200055935729725
            71636269561882670428252483600823257530420752963450

    Find the thirteen adjacent digits in the 1000-digit number that have the 
    greatest product. What is the value of this product?

    Time:   O(n)
    Space:  O(1)
    """
    
    # create left and right pointers
    l, r = 0, 13
    LEN = len(string)
    coords = [0, 0]
    max_prod = -1
    

    # loop thru number, placing right at 13th index
    while r != LEN:
        last_l = l
        prod = 1
        # get product of all values
        while l != r:
            # use while l < r to convert each value to an int
            prod *= int(string[l])
            l += 1
            
        # calculate max product
        max_prod = max(max_prod, prod)
        
        # save last-l position and revert once done
        l = last_l
        l += 1
        r += 1
        
    return max_prod

def euler_nine():
    """
    Problem 9: Special Pythagorean Triplet

    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a^2 + b^2 = c^2. For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2. There exists 
    exactly one Pythagorean triplet for which a + b + c = 1000. Find the product 
    abc.

    Time:   O(n^2)
    Space:  O(1)
    """

    """
    c > b > a
    
    1000 = a + b + c
    c = 1000 - a - b

    1000 - a - b > b
    1000 - a > 2b
    500 - a/2 > b -> upper limit for b
    """

    for a in range(1, 1000):
        for b in range(a, 500 - a // 2):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                return (a*b*c, a, b, c)

def euler_ten():
    """
    Problem 10: Summation of Primes

    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the 
    primes below two million.

    Time:   
    Space:  
    """
    ssum = 0
    
    for i in range(1, 2000000):
        ssum += i if Helper._is_prime(i) else 0
    
    return ssum



# print(euler_six())

# print(euler_seven())

# val = "".join("""
# 73167176531330624919225119674426574742355349194934
# 96983520312774506326239578318016984801869478851843
# 85861560789112949495459501737958331952853208805511
# 12540698747158523863050715693290963295227443043557
# 66896648950445244523161731856403098711121722383113
# 62229893423380308135336276614282806444486645238749
# 30358907296290491560440772390713810515859307960866
# 70172427121883998797908792274921901699720888093776
# 65727333001053367881220235421809751254540594752243
# 52584907711670556013604839586446706324415722155397
# 53697817977846174064955149290862569321978468622482
# 83972241375657056057490261407972968652414535100474
# 82166370484403199890008895243450658541227588666881
# 16427171479924442928230863465674813919123162824586
# 17866458359124566529476545682848912883142607690042
# 24219022671055626321111109370544217506941658960408
# 07198403850962455444362981230987879927244284909188
# 84580156166097919133875499200524063689912560717606
# 05886116467109405077541002256983155200055935729725
# 71636269561882670428252483600823257530420752963450
# """.strip().split())
# print(euler_eight(val))

# print(euler_nine())

# print(euler_ten())