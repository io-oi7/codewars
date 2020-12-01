"""
Given a Divisor and a Bound , Find the largest integer N , Such That , 
    N is divisible by divisor
    N is less than or equal to bound
    N is greater than 0.
The parameters (divisor, bound) passed to the function are only positive values .
It's guaranteed that a divisor is Found .

ex.
maxMultiple (2,7) ==> return (6)

TESTS:

Test.describe("Basic tests")
Test.assert_equals(max_multiple(2,7),6)
Test.assert_equals(max_multiple(3,10),9)
Test.assert_equals(max_multiple(7,17),14)
Test.assert_equals(max_multiple(10,50),50)
Test.assert_equals(max_multiple(37,200),185)
Test.assert_equals(max_multiple(7,100),98)
print("<COMPLETEDIN::>")
"""

def max_multiple(divisor, bound):
    return [i for i in range(divisor, bound+1, divisor)][-1]
        


print(max_multiple(2,7)) # 6
print(max_multiple(3,10)) # 9
print(max_multiple(7,17)) # 14
print(max_multiple(10,50)) # 50