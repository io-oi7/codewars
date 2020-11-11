"""
Complete the solution so that it reverses 
all of the words within the string passed in. 


TESTS:
test.assert_equals(reverseWords("hello world!"), "world! hello")
"""

def reverseWords(s):
    return " ".join(s.split()[::-1])