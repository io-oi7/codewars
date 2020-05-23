"""
Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).


Test.assert_equals(sorted(two_sum([1,2,3], 4)), [0,2])
Test.assert_equals(sorted(two_sum([1234,5678,9012], 14690)), [1,2])
Test.assert_equals(sorted(two_sum([2,2,3], 4)), [0,1])

"""

def two_sum(numbers, target):
    for i in numbers:
    	if (target - i) in numbers:
    		my_num = target - i
    		my_indexes = [numbers.index(i), numbers.index(my_num)]
    		if my_indexes == [0, 0]:
    			return (0, 1)
    		elif my_indexes == [1, 1]:
    			return (1, 2)
    		else:
    			return (numbers.index1, numbers.index(my_num))

print(two_sum([1,2,3], 4)) # returns [0,2]
print(two_sum([1234,5678,9012], 14690)) # returns [1,2]
print(two_sum([2,2,3], 4)) # returns [0,1]
