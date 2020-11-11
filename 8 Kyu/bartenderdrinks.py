"""
Write a function getDrinkByProfession/get_drink_by_profession() that receives as input parameter a string, and produces outputs according to the following table:

Input -> Output
"Jabroni" -> "Patron Tequila"
"School Counselor" -> "Anything with Alcohol"
 "Programmer" -> "Hipster Craft Beer"
 "Bike Gang Member" -> "Moonshine" 
 "Politician" -> "Your tax dollars" 
 "Rapper" -> "Cristal" 
 *anything else* -> "Beer" 

Note: anything else is the default case: if the input to the function is not any of the values in the table, then the return value should be "Beer."

Make sure you cover the cases where certain words do not show up with correct capitalization. For example, getDrinkByProfession("pOLitiCIaN") should still return "Your tax dollars".


TESTS:
test.assert_equals(get_drink_by_profession("jabrOni"), "Patron Tequila", "'Jabroni' should map to 'Patron Tequila'")
test.assert_equals(get_drink_by_profession("scHOOl counselor"), "Anything with Alcohol", "'School Counselor' should map to 'Anything with alcohol'")
test.assert_equals(get_drink_by_profession("prOgramMer"), "Hipster Craft Beer", "'Programmer' should map to 'Hipster Craft Beer'")
test.assert_equals(get_drink_by_profession("bike ganG member"), "Moonshine", "'Bike Gang Member' should map to 'Moonshine'")
test.assert_equals(get_drink_by_profession("poLiTiCian"), "Your tax dollars", "'Politician' should map to 'Your tax dollars'")
test.assert_equals(get_drink_by_profession("rapper"), "Cristal", "'Rapper' should map to 'Cristal'")
test.assert_equals(get_drink_by_profession("pundit"), "Beer", "'Pundit' should map to 'Beer'")
test.assert_equals(get_drink_by_profession("Pug"), "Beer", "'Pug' should map to 'Beer'")
"""


def get_drink_by_profession(param):
    if param.lower() == "jabroni":
        return "Patron Tequila"
    elif param.lower() == "school counselor":
        return "Anything with Alcohol"
    elif param.lower() == "programmer":
        return "Hipster Craft Beer"
    elif param.lower() == "bike gang member":
        return "Moonshine"
    elif param.lower() == "politician":
        return "Your tax dollars"
    elif param.lower() == "rapper":
        return "Cristal"
    else:
        return "Beer"