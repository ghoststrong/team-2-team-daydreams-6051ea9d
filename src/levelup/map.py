from levelup.position import Position

class GameMap():
    #starting_position = Position(0, 0) # we want this to be random in the future
    starting_position = Position([0,0])
    positions = []
    size = [10,10]
    def __init__(self):
       self.numPositions = 100
       self.create_positions()
    def create_positions(self) -> None:
        temp_pos = []
        for x in range(self.size[0]):
            y_range = []
            for y in range(self.size[1]):
                #new_pos = Position(x, y)
                coords = [x, y]
                new_pos = Position(coords)
                y_range.append(new_pos)
            temp_pos.append(y_range)
            self.positions = temp_pos
       #self.map_size = 10 # had to think of this in map size
    def getPositions():
        pass
    def calculatePosition(startingPostion, direction):
        pass
    def getTotalPositions():
        pass
    # adding display so I can visually see a map we can comment out the print
    """def display_map(self, character_name):
        for y in range(self.map_size -1, -1, -1):
            row = []
            for x in range(self.map_size):
                if character_name.x == x and character_name.y == y:
                    row.append('X')
                else:
                    row.append('.')
            print(' '.join(row))"""
