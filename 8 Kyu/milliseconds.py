"""
Clock shows 'h' hours, 'm' minutes and 's' 
seconds after midnight.

Your task is to make 'Past' function which 
returns time converted to milliseconds.


Example:
past(0, 1, 1) == 61000


TEST:
test.assert_equals(past(0,1,1),61000)
test.assert_equals(past(1,1,1),3661000)
test.assert_equals(past(0,0,0),0)
test.assert_equals(past(1,0,1),3601000)
test.assert_equals(past(1,0,0),3600000)
"""

def past(h, m, s):
    return ((s * 1000) + (m * 60000) + (h * 3600000))

print(past(0,1,1)) # -> 61000
print(past(1,1,1)) # -> 3661000
print(past(0,0,0)) # -> 0
print(past(1,0,1)) # -> 3601000
print(past(1,0,0)) # -> 3600000