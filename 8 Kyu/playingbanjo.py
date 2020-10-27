"""
Create a function which answers the question "Are you playing 
banjo?".  If your name starts with the letter "R" or lower case 
"r", you are playing banjo!

The function takes a name as its only argument, and returns 
one of the following strings:

name + " plays banjo" 
name + " does not play banjo"


TEST:

test.assert_equals(areYouPlayingBanjo("martin"), "martin does not play banjo");
test.assert_equals(areYouPlayingBanjo("Rikke"), "Rikke plays banjo");
"""

def areYouPlayingBanjo(name):
    return name + ' plays banjo' if name[0].lower() == 'r' else name + ' does not play banjo'

print(areYouPlayingBanjo("martin")) # -> ' does not play banjo'
print(areYouPlayingBanjo("Rikke")) # -> ' plays banjo'