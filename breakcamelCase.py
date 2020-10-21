"""
Complete the solution so that the function will 
break up camel casing, using a space between words.

ex.
solution("camelCasing")  ==  "camel Casing"

TEST:

Test.assert_equals(solution("helloWorld"), "hello World")
Test.assert_equals(solution("camelCase"), "camel Case")
Test.assert_equals(solution("breakCamelCase"), "break Camel Case")
"""

s = "breakCamelCase"

def solution(s):
    my_list = []
    for i in s:
        if i.islower():
            my_list.append(i)
        else:
            my_list.append(' ')
            my_list.append(i)
    return ''.join(my_list)

for i in ["helloWorld", "camelCase", "breakCamelCase"]:
    print(solution(i))