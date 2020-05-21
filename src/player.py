# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self):
        self.current_room = 'outside'
        self.inventory = []

    def change_room(self, new_room):
        self.current_room = new_room

    def pick_up(self, item):
        self.inventory.append(item)
    
