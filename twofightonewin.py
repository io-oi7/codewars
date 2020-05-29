"""
Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.

Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0. You can mutate the Fighter objects.


test.describe("Example test cases")
test.assert_equals(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew"), "Lew")
test.assert_equals(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Harry"),"Harry")
test.assert_equals(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry"),"Harald")
test.assert_equals(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harald"),"Harald")
test.assert_equals(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry"), "Harald")
test.assert_equals(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Harald"),"Harald")

"""

from math import ceil


class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})".format(
    	self.name, self.health, self.damage_per_attack)
    __repr__=__str__


def declare_winner(fighter1, fighter2, first_attacker):
    rounds1 = ceil(float(fighter1.health)/fighter2.damage_per_attack)
    rounds2 = ceil(float(fighter2.health)/fighter1.damage_per_attack)
    if rounds1 == rounds2:
        return first_attacker
    else:
        return fighter1.name if (rounds1 > rounds2) else fighter2.name