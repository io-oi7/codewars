"""
Write function parse_float which takes a string/list 
and returns a number or 'none' if conversion is not possible.


TEST:

test.describe("Example Tests")

ts = (
    ("1.0", 1.0),
    ("a", None),
    ("234.0234", 234.0234)
)

for t in ts:
    test.assert_equals(parse_float(t[0]), t[1])
"""

def parse_float(string):
    try:
        return float(string)
    except:
        return None