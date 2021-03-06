"""
Write a function named setAlarm which receives two parameters. 
The first parameter, employed, is true whenever you are employed 
and the second parameter, vacation is true whenever you are on vacation.

The function should return true if you are employed and not on 
vacation (because these are the circumstances under which you need 
to set an alarm). It should return false otherwise. Examples:

setalarm(true, true) -> false
setalarm(false, true) -> false
setalarm(false, false) -> false
setalarm(true, false) -> true


TEST:

Test.describe("set_alarm")

Test.it("returns correct result for all input values")
Test.assert_equals(set_alarm(True, True), False, "Fails when input is True, True")
Test.assert_equals(set_alarm(False, True), False, "Fails when input is False, True")
Test.assert_equals(set_alarm(False, False), False, "Fails when input is False, False")
Test.assert_equals(set_alarm(True, False), True, "Fails when input is True, False")

"""

def set_alarm(employed, vacation):
    if employed == True and vacation == False:
        return True
    else:
        return False