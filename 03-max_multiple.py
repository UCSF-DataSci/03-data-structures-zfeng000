#!/usr/bin/env python3
"""
Maximum Product of 13 Adjacent Digits

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
What is the value of this product?

Your task:
Complete the find_greatest_product() function to solve the problem.

Hints:
- You can iterate through the string using a for loop and string slicing
- Keep track of the maximum product as you go through the loooong number
- (Optional) Convert characters to integers using int()
"""


THOUSAND_DIGIT_NUMBER = """
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
""".replace("\n", "")

def find_greatest_product(number_string, adjacent_digits=13):
    max_product = 0
    
    # loop through the number_string (the long string of 1000 digits, aka the THOUSAND_DIGIT_NUMBER)
    for i in range(len(number_string) - adjacent_digits + 1): # (len(number_string)-adjacent_digits+1) calculates how many 
        # valid slices (substrings) of 13 adjacent digits we can take from number_string; +1 because in Python slicing, the range is
        # inclusive of the start index but exclusive of the end index, so we need to +1 to capture the last valid slice.
        # range() creates a range of numbers from 0 to the total substring number
        current_slice = number_string[i:i + adjacent_digits]
    
    # calculate the product of these digits
    product = 1
    for digit in current_slice:
        product *= int(digit)

    # update max_product if new product is larger
    if product > max_product:
        max_product = product

    return max_product

if __name__ == "__main__":
    result = find_greatest_product(THOUSAND_DIGIT_NUMBER)
    print(f"The greatest product of 13 adjacent digits is: {result}")