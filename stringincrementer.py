"""
Your job is to write a function which increments a string, to create a new string.

    If the string already ends with a number, the number should be incremented by 1.
    If the string does not end with a number. the number 1 should be appended to the new string.


Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.


Test.assert_equals(increment_string("foo"), "foo1")
Test.assert_equals(increment_string("foobar001"), "foobar002")
Test.assert_equals(increment_string("foobar1"), "foobar2")
Test.assert_equals(increment_string("foobar00"), "foobar01")
Test.assert_equals(increment_string("foobar99"), "foobar100")
Test.assert_equals(increment_string("foobar099"), "foobar100")
Test.assert_equals(increment_string(""), "1")

"""
import re

def increment_string(s):
    string, num, n = '', '', 0
    if s:
        string, num = [*re.match(r'^(.*?)(\d*)$', s).groups()]
        n = int(num) if num else 0
    return string + str(n + 1).rjust(len(num), '0')


print(increment_string(''))
print(increment_string('foobar'))
print(increment_string('foobar1'))
print(increment_string('foobar001'))
print(increment_string("foobar099"))
print(increment_string("foobar00"))
print(increment_string("foobar99"))
print(increment_string("foobar099"))