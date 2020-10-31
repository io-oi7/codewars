"""
The cockroach is one of the fastest insects. 
Write a function which takes its speed in km 
per hour and returns it in cm per second, rounded 
down to the integer (= floored).


TEST:

test.describe("Basic Tests")
test.assert_equals(cockroach_speed(1.08),30)
test.assert_equals(cockroach_speed(1.09),30)
test.assert_equals(cockroach_speed(0),0)
"""

def cockroach_speed(s):
    return s // 0.036
