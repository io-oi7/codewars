"""
Return the length of the given month in the given year.
Your code must be shorter than 90 characters.


TESTS:
test.assert_equals(last_day(2020,11), 30)
test.assert_equals(last_day(1945,5), 31)
test.assert_equals(last_day(2000,2), 29)
test.assert_equals(last_day(1900,2), 28)
"""
from calendar import monthrange

def last_day(y, m):
    return monthrange(y, m)[1]


print(last_day(1900,2)) # -> 28