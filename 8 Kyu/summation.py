"""
Write a program that finds the summation of every 
number from 1 to num. The number will always be a 
positive integer greater than 0.

summation(2) -> 3
1 + 2

summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8


TEST:

@test.describe('Basic tests')
def basic_tssts():
    test.assert_equals(summation(1), 1)
    test.assert_equals(summation(8), 36)
    test.assert_equals(summation(22), 253)
    test.assert_equals(summation(100), 5050)
    test.assert_equals(summation(213), 22791)
"""

def summation(num):
    return sum([i+1 for i in range(num)])
    
