class Character:
    name = ""
    current_position = []

    def __init__(self, character_name):
        self.name = character_name

    def enter_map(self, map):
        self.current_position = map.starting_position
    
        



