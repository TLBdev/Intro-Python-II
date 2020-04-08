# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self):
        self.current_room = 'outside'

    def change_room(self, new_room):
        self.current_room = new_room
