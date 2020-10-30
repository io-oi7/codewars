"""
checkAlive/CheckAlive/check_alive should return 
true if the player's health is greater than 0 or 
false if it is 0 or below.

The function receives one parameter health which 
will always be a whole number between -10 and 10.


TEST:

Test.assert_equals(check_alive(-2), False)
Test.assert_equals(check_alive(0), False)
Test.assert_equals(check_alive(1), True)
Test.assert_equals(check_alive(3), True)
"""


def check_alive(health):
    return True if health > 0 else False
