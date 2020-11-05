"""
Given 2 strings, a and b, return a string of 
the form short+long+short, with the shorter 
string on the outside and the longer string 
on the inside. The strings will not be the 
same length, but they may be empty ( length 0 ).

solution("1", "22") # returns "1221"
solution("22", "1") # returns "1221"


TEST:
BASIC_TESTS = (
    (('45', '1'), '1451'),
    (('13', '200'), '1320013'),
    (('Soon', 'Me'), 'MeSoonMe'),
    (('U', 'False'), 'UFalseU')
)

test.describe('Basic Tests')
for pair, result in BASIC_TESTS:
    test.it("'{}', '{}'".format(*pair))
    test.assert_equals(solution(*pair), result)
"""

def solution(a, b):
    return a + b + a if len(a) < len(b) else b + a + b