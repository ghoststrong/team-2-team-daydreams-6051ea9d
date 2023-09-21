from levelup.position import Position

class GameStatus:
    
    def __init__(self, characterName, coordinates, moveCount):
        self.characterName = characterName
        self.currentPosition = Position(coordinates)
        self.moveCount = moveCount

    def toString(self):
        return ("("+ str(self.moveCount) +") "+
            self.characterName+" is currently at position ["+ 
            self.currentPosition.coordinates[0]+ ","+ self.currentPosition.coordinates[1]+ "]" )