"""
Write a function that produces an array with the numbers 0 to N-1 in it.


TEST:

@test.it("Basic Tests")
def basic_tests():
    test.assert_equals(arr(4), [0,1,2,3])
    test.assert_equals(arr(0), [])
    test.assert_equals(arr(), [])
"""

def arr(n=0): 
    return list(range(n))