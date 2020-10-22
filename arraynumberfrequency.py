"""
Complete the method which returns the number which is 
most frequent in the given input array. If there is a tie 
for most frequent number, return the largest number among them.

Note: no empty arrays will be given.


EX:

[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3


TESTS:

test.describe("Example Tests")
test.it("Example Test Case")
test.assert_equals(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]), 12)
test.assert_equals(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]), 10)
"""


def highest_rank(arr):
    return sorted(arr,key=lambda x: (arr.count(x),x))[-1]


print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]))
print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]))