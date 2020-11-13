"""
You are creating an "Escape the room" game. 
The first step is to create a hash table called 
rooms that contains all of the rooms of the 
game. There should be at least 3 rooms inside 
it, each being a hash table with at least three 
properties (e.g. name, description, completed).


"""

rooms = {
    'dungeon1': {'name': 'dungeon', 'description': 'Dark, creepy', 'completed': 'no'}, 
    'dungeon2': {'name': 'tower', 'description': 'Tall, windy', 'completed': 'no'}, 
    'dungeon3': {'name': 'keep', 'description': 'Posh, regal', 'completed': 'yes'}}

print(rooms)