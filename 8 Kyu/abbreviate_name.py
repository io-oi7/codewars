"""
Write a function to convert a name into initials. 
This kata strictly takes two words with one space 
in between them.

The output should be two capital letters with a 
dot separating them.

It should look like this:

    Sam Harris => S.H
    Patrick Feeney => P.F


TESTS:
test.assert_equals(abbrev_name("Sam Harris"), "S.H");
test.assert_equals(abbrev_name("Patrick Feenan"), "P.F");
test.assert_equals(abbrev_name("Evan Cole"), "E.C");
test.assert_equals(abbrev_name("P Favuzzi"), "P.F");
test.assert_equals(abbrev_name("David Mendieta"), "D.M");
"""

def abbrev_name(name):
    return f"{name.split(' ')[0][0].upper()}.{name.split(' ')[1][0].upper()}"

print(abbrev_name("Sam Harris"))
print(abbrev_name("Patrick Feenan"))