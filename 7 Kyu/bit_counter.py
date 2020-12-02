"""
In this Kata you need to write the method SharedBits that returns true if 2 integers 
share at least two '1' bits. For simplicity assume that all numbers are positive

For example int seven = 7; //0111 int ten = 10; 
//1010 int fifteen = 15; //1111 
SharedBits(seven, ten); //false 
SharedBits(seven, fifteen); //true 
SharedBits(ten, fifteen); //true

explained:
    seven and ten share only a single '1' (at index 3)
    seven and fifteen share 3 bits (at indexes 1, 2, and 3)
    ten and fifteen share 2 bits (at indexes 0 and 2)

TESTS:

Test.assert_equals(shared_bits(1, 2), False)
Test.assert_equals(shared_bits(16, 8), False)
Test.assert_equals(shared_bits(1, 1), False)
Test.assert_equals(shared_bits(2, 3), False)
Test.assert_equals(shared_bits(7, 10), False)
Test.assert_equals(shared_bits(43, 77), True)
Test.assert_equals(shared_bits(7, 15), True)
Test.assert_equals(shared_bits(23, 7), True)
"""

def shared_bits(a, b):
    return True if format(a & b, 'b').count('1') >= 2 else False
    

print(shared_bits(1, 2))
print(shared_bits(16, 8))
print(shared_bits(1, 1))
print(shared_bits(2, 3))
print(shared_bits(7, 10))
print(shared_bits(43, 77))
print(shared_bits(7, 15))
print(shared_bits(23, 7))