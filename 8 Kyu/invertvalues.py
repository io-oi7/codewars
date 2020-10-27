"""
Given a set of numbers, return the additive inverse of each. 
Each positive becomes negatives, and the negatives become positives.

ex:

invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []


TEST:

Test.it("Basic Tests")
Test.assert_equals(invert([1,2,3,4,5]),[-1,-2,-3,-4,-5])
Test.assert_equals(invert([1,-2,3,-4,5]), [-1,2,-3,4,-5])
Test.assert_equals(invert([]), [])
"""

def invert(lst):
    return [-i for i in lst]

print(invert([1,2,3,4,5])) # -> [-1,-2,-3,-4,-5]
