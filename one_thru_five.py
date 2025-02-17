from testing.utils import Evaluation, Helper


def euler_one(x: int) -> int:
    """
    Problem 1: Multiples of 3 or 5
    If we list all the natural numbers below 10 that are multiples of 3 or 5, 
    we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all
    the multiples of 3 or 5 below 1000. 

    Answer: 233,168

    Idea: Iterate thru all values between 0 and the max range, finding all
    multiples of 3 and 5

    Time:   0(n) -> based on x input
    Space:  O(1) -> no extra space used
    """

    ssum = 0

    # loop thru values in range 1000, seeing if value's remainder is 0 
    # when divided by 3 or 5 
    for x in range(x):
        if x % 3 == 0 or x % 5 == 0:
            ssum += x

    return ssum


@Evaluation.eval
def euler_two(x: int) -> int:
    """
    Problem 2: Even Fibonacci Numbers
    Each new term in the Fibonacci sequence is generated by adding the previous
    two terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    sum = 44

    By considering the terms in the Fibonacci sequence whose values do not 
    exceed four million, find the sum of the even-valued terms.

    Idea: Use bottom-up dynamic programming to solve this. Keep a previous and 
    current variable to track values in the sequence. if the value is even, 
    x % 2 == 0, add to the sum.

    Assumption: 1 <= x <= 4,000,000

    Time:   O(n) -> worst case, up to upper limit of x
    Space:  O(1) -> no space used
    """

    # BASE CASES: if x == 0 or 1
    if x < 2:
        return 0

    # create sum, prev, and curr variables
    ssum, prev, curr =  0, 1, 2
    

    # fionnaci call
    # NOTE: remove 2 from the loop since they're already accounted for
    for _ in range(x - 2):
        if curr % 2 == 0:
            ssum += curr

        prev, curr = curr, prev + curr

    # return sum
    return ssum

# print(euler_two(8))

def euler_three(x: int) -> int:
    """
    Problem 3: Largest Prime Factor
    
    The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime
    factor of the number 600851475143?

    Idea: Get list of prime numbers in the interval, if the number is a factor
    of input number, x -> x % i == 0, track as the max number, max(curr, prev) 

    Edge case: x = 0 or 1

    x = 4  | [2]          | ret = -1
    x = 12 | [2, 3, 4, 6] | ret = 3

    Time:   O(n^2)
        [I feel like this could be better]
    Space:  O(n) -> number of values for multis list
    """

    largest_factor = -1
    multis = []

    # EDGECASE  
    if x in [0, 1, 2]:
        return -1

    # get list of multiples 
    for num in range(x):
        if x % num == 0:
            multis.append(num)

    # check for the largest prime value in multiples list
    for num in multis:
        if Helper._is_prime(num):
            largest_factor = max(largest_factor, num)

    return largest_factor


def euler_four():
    """
    Problem 4: Largest Palindrome Product
    A palindromic number reads the same both ways. The largest palindrome made 
    from the product of two 2-digit numbers is 9009 = 91 x 99.

    Find the largest palindrome made from the product of two 3-digit numbers.

    Time:   O(n^2)
    Space:  O(n)
    """

    largest_palindrome = 0

    def palindrome(x):
        rev = int(str(x)[::-1])
        return x == rev

    for num1 in range(100, 1000):
        for num2 in range(100, 1000):
            prod = num1 * num2
            if palindrome(prod):
                largest_palindrome = max(largest_palindrome, prod)

    return largest_palindrome

# print(euler_four())


def euler_five():
    """
    Problem 5: Smallest Multiple

    2520 is the smallest number that can be divided by each of the numbers from
    1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible (divisible with 
    no remainder) by all of the numbers from 1 to 20?

    Time:   O(n log n)
    Space:  O(n)
    """

    pass