from room import Room
from player import Player
from item import Item
from random import randrange

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

loot_table = [
    Item("Rusty Greatsword","Probably no good for combat, but a blacksmith may pay you well for the steel.",5),
    Item("Pouch of Gold Coins","Worth its weight in gold (mostly).",20),
    Item("(Magic?) Wand","Could be worth more than your wildest dreams... but probably just a stick.", 0),
    Item("Jeweled Amulet","Worth a lot of money, but completely useless.", 50)
]
# Link rooms together

room['outside'].n_to = 'foyer'
room['foyer'].s_to = 'outside'
room['foyer'].n_to = 'overlook'
room['foyer'].e_to = 'narrow'
room['overlook'].s_to = 'foyer'
room['narrow'].w_to = 'foyer'
room['narrow'].n_to = 'treasure'
room['treasure'].s_to = 'narrow'

for k, v in room.items():
    loot = randrange(0,10)
    if loot < 4:
        room[k].contents.append(loot_table[loot])

for k, v in room.items():
    print(room[k].contents)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = Player()
# print(f"\n \nYou are in the {room[new_player.current_room].name}")
# print(room[new_player.current_room].description)
# direction = (input("[N]orth  [S]outh  [E]ast  [W]est  [I]nventory  [Q]uit Game\n")).upper()

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there. (n, s, e, w)
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

direction = ''

while True:
    
    if direction == 'Q':
        quit()

    if direction == 'N':
        if room[new_player.current_room].n_to is not None:
            new_player.change_room(room[new_player.current_room].n_to)
        else:
            print('\n\nThere is nowhere to go in that direction.')

    if direction == 'S':
        if room[new_player.current_room].s_to is not None:
            new_player.change_room(room[new_player.current_room].s_to)
        else:
            print('\n\nThere is nowhere to go in that direction.')

    if direction == 'E':
        if room[new_player.current_room].e_to is not None:
            new_player.change_room(room[new_player.current_room].e_to)
        else:
            print('\n\nThere is nowhere to go in that direction.')

    if direction == 'W':
        if room[new_player.current_room].w_to is not None:
            new_player.change_room(room[new_player.current_room].w_to)
        else:
            print('\n\nThere is nowhere to go in that direction.')

    if direction == "I":
        carried = [f"{i.name}: {i.description}" for i in new_player.inventory]
        for i in carried:
            print(i)
        drop_item = input('Would you like to drop an item? [Y]es [N]o \n').upper()
        if drop_item == "Y":
            inventory = [i for i in new_player.inventory]
            question = f"Which item would you like to drop?"
            for x in range(len(inventory)):
                question = question + (f"[{x+1}]: {inventory[x].name}")
            dropped_item = int(input(question))
            if dropped_item < len(inventory) and dropped_item >= 0:
                room[new_player.current_room].contents.append(new_player.inventory[dropped_item - 1])
                new_player.inventory.pop(dropped_item - 1)

                carried = [i.name for i in new_player.inventory]
                print(f"you are now carrying: {carried}")

    if direction == 'IDDQD':
        print("\nWrong game, You are dead.")
        quit()

    if direction == 'IDKFA':
        print("\nInfinite ammo... but no gun, you really thought this through.")
        

    print(f"\n \nYou are in the {room[new_player.current_room].name}")
    print(room[new_player.current_room].description)
    if len(room[new_player.current_room].contents) > 0:
        
        move_item = input(f"Something catches your eye, it appears to be a {room[new_player.current_room].contents[0].name} would you like to take this item? [Y]es or [N]o\n").upper()
        if move_item == "Y":
            new_player.pick_up(room[new_player.current_room].contents[0])
            room[new_player.current_room].contents = []
            carried = [i.name for i in new_player.inventory]
            print(f"you are now carrying: {carried}")
        else: 
            continue

    direction = (input("[N]orth  [S]outh  [E]ast  [W]est  [I]nventory  [Q]uit Game\n")).upper()
