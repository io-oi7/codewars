"""
Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.


~~~~~~~~~~~~~~~~~~~


Test.describe("Basic tests")
Test.assert_equals(basic_op('+', 4, 7), 11)
Test.assert_equals(basic_op('-', 15, 18), -3)
Test.assert_equals(basic_op('*', 5, 5), 25)
Test.assert_equals(basic_op('/', 49, 7), 7)

"""

def basic_op(operator, value1, value2):
    if operator == '+':
    	return value1 + value2
    elif operator == '-':
    	return value1 - value2
    elif operator == '*':
    	return value1 * value2
    elif operator == '/':
    	return value1 / value2
    else:
    	print('Invalid operator.')


if __name__ == '__main__':
	print(basic_op('+', 4, 7))
	print(basic_op('-', 15, 18))
	print(basic_op('*', 5, 5))
	print(basic_op('/', 49, 7))