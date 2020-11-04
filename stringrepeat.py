"""
Write a function called repeat_str which repeats 
the given string src exactly count times.


TEST:
test.describe("Example Tests")
test.assert_equals(repeat_str(4, 'a'), 'aaaa')
test.assert_equals(repeat_str(3, 'hello '), 'hello hello hello ')
test.assert_equals(repeat_str(2, 'abc'), 'abcabc')
"""

def repeat_str(repeat, string):
    return string * repeat
