from room import Room
from player import Player
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


# Link rooms together

room['outside'].n_to = 'foyer'
room['foyer'].s_to = 'outside'
room['foyer'].n_to = 'overlook'
room['foyer'].e_to = 'narrow'
room['overlook'].s_to = 'foyer'
room['narrow'].w_to = 'foyer'
room['narrow'].n_to = 'treasure'
room['treasure'].s_to = 'narrow'

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = Player()
print(f"\n \nYou are in the {room[new_player.current_room].name}")
print(room[new_player.current_room].description)
direction = (input("[N] North  [S] South  [E] East  [W] West  [Q] Quit Game\n")).upper()

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

while not direction == 'Q':
    
    if direction == 'N':
        if room[new_player.current_room].n_to is not None:
            new_player.change_room(room[new_player.current_room].n_to)
        else:
            print('There is nowhere to go in that direction.')

    if direction == 'S':
        if room[new_player.current_room].s_to is not None:
            new_player.change_room(room[new_player.current_room].s_to)
        else:
            print('There is nowhere to go in that direction.')

    if direction == 'E':
        if room[new_player.current_room].e_to is not None:
            new_player.change_room(room[new_player.current_room].e_to)
        else:
            print('There is nowhere to go in that direction.')

    if direction == 'W':
        if room[new_player.current_room].w_to is not None:
            new_player.change_room(room[new_player.current_room].w_to)
        else:
            print('There is nowhere to go in that direction.')

    if direction == 'IDDQD':
        print("\nWe don't allow cheating here!")
        quit()

    if direction == 'IDKFA':
        print("\nInfinite ammo... but still no gun, you really thought this through.")
        
    
    print(f"\n \nYou are in the {room[new_player.current_room].name}")
    print(room[new_player.current_room].description)
    direction = (input("[N] North  [S] South  [E] East  [W] West  [Q] Quit Game\n")).upper()
