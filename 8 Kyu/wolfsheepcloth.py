"""
Warn the sheep in front of the wolf that it is 
about to be eaten. Remember that you are standing 
at the front of the queue which is at the end of the array:

[sheep, sheep, sheep, sheep, sheep, wolf, sheep, sheep]      
(YOU ARE HERE AT THE FRONT OF THE QUEUE)

If the wolf is the closest animal to you, return "Pls 
go away and stop eating my sheep". Otherwise, return 
"Oi! Sheep number N! You are about to be eaten by a wolf!" 
where N is the sheep's position in the queue.


TEST:

test.assert_equals(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']), 'Oi! Sheep number 2! You are about to be eaten by a wolf!')
test.assert_equals(warn_the_sheep(['sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']), 'Oi! Sheep number 5! You are about to be eaten by a wolf!')
test.assert_equals(warn_the_sheep(['wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']), 'Oi! Sheep number 6! You are about to be eaten by a wolf!')
test.assert_equals(warn_the_sheep(['sheep', 'wolf', 'sheep']), 'Oi! Sheep number 1! You are about to be eaten by a wolf!')
test.assert_equals(warn_the_sheep(['sheep', 'sheep', 'wolf']), 'Pls go away and stop eating my sheep')
"""


def warn_the_sheep(queue):
    if queue[-1] == 'wolf':
        return 'Pls go away and stop eating my sheep'
    else:
        return 'Oi! Sheep number {}! You are about to be eaten by a wolf!'.format((len(queue) - queue.index('wolf')) - 1)


# Results: Sheep 2, 5, 6, 1, queue[-1]
print(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']))
print(warn_the_sheep(['sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']))
print(warn_the_sheep(['wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']))
print(warn_the_sheep(['sheep', 'wolf', 'sheep']))
print(warn_the_sheep(['sheep', 'sheep', 'wolf']))
