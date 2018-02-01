from Tile import Tile
from landmark import *

#1
#Subclass to represent a specific tile type. This is the starting tile for the game.
#This piece has a straight road and a city cap and a grassy area either side of
#There 1 tile of this type
class IntialTile(Tile):
    def __init__(self):
        city1 = City()
        road1 = Road()
        grass1 = Grass()
        id = "00"
        Tile.__init__(self, id, city1, road1, road1, grass)

        
    def getTile(self):
        Tile.getTile(self)


#2
#Subclass to represent a specific tile type, a city
#City tiles are entirely city pieces
#There 1 tile of this type (which is crested)
class CityTile(Tile):
    def __init__(self):
        city1 = City()
        id = "03"
        Tile.__init__(self, id, city1, city1, city1, city1)

        
    def getTile(self):
        Tile.getTile(self)

#3
#Subclass to represent a specific tile type, a city cap 
#City cap tiles have one side as a city pieces, and the rest grass
#There are 5 tiles of this type
class CityCapTile(Tile):
    def __init__(self):
        city1 = City()
        grass1 = Grass()
        id = "21"
        Tile.__init__(self, id, city1, grass1, grass1, grass1)

        
    def getTile(self):
        Tile.getTile(self)


#4
#Subclass to represent a specific tile type, a city cap with a road bending to the left
#It has a city cap on one side, and an L road leading to the left
#There are 3 tiles of this type
class CapLeftBend(Tile):
    def __init__(self):
        city1 = City()
        road1 = Road()
        grass1 = Grass()
        id = "19"
        Tile.__init__(self, id, city1, road1, grass1, road1)

        
    def getTile(self):
        Tile.getTile(self)


#5
#Subclass to represent a specific tile type, a city cap with a road bending to the left
#It has a city cap on one side, and an L road leading to the right
#There are 3 tiles of this type
class CapRightBend(Tile):
    def __init__(self):
        city1 = City()
        road1 = Road()
        grass1 = Grass()
        id = "23"
        Tile.__init__(self, id, city1, grass1, road1, road1)

        
    def getTile(self):
        Tile.getTile(self)


#6
#Identical to the InitialTile class
#There are 3 tiles of this type
class CapStraightRoad(Tile):
    def __init__(self):
        city1 = City()
        road1 = Road()
        grass1 = Grass()
        id = "00"
        Tile.__init__(self, id, city1, road1, road1, grass1)

        
    def getTile(self):
        Tile.getTile(self)
    
#7
#Subclass to represent a specific tile type, a city cap with a T-junction opposite it
#It has a city cap on one side, and an T-junction
#There are 3 tiles of this type
class CapTJunction(Tile):
    def __init__(self):
        city1 = City()
        road1 = Road()
        id = "20"
        Tile.__init__(self, id, city1, road1, road1, road1)

        
    def getTile(self):
        Tile.getTile(self)

#8
#Subclass to represent a specific tile type, 2 city caps opposite each other
#It has 2 city cap parallel to each other
#There are 3 tiles of this type
class OppositeCaps(Tile):
    def __init__(self):
        city1 = City()
        city2 = City()
        grass1 = Grass()
        id = "22"
        Tile.__init__(self, id, grass1, city1, city2, grass1)

        
    def getTile(self):
        Tile.getTile(self)
        
#9        
#Subclass to represent a specific tile type, 2 city caps adjacent to each other
#It has 2 city cap perpendicular to each other
#There are 2 tiles of this type
class AdjacentCaps(Tile):
    def __init__(self):
        city1 = City()
        city2 = City()
        grass1 = Grass()
        id = "03"
        Tile.__init__(self, id, city1, grass1, city2, grass1)

        
    def getTile(self):
        Tile.getTile(self)
        
#10
#Subclass to represent a specific tile type, one city cap that encompasses 2 sides 
#It has 1 city cap, over on the north and west sides, with the rest being grass
#There are 3 tiles of this type
class DiagonalCap(Tile):
    def __init__(self):
        city1 = City()
        grass1 = Grass()
        id = "13"
        Tile.__init__(self, id, city1, city1, grass1, grass1)

        
    def getTile(self):
        Tile.getTile(self)

#11
#Same as DiagonalCap but has a crest
#There are 2 tiles of this type
class DiagonalCapCrest(Tile):
    def __init__(self):
        city1 = City(True)
        grass1 = Grass()
        id = "14"
        Tile.__init__(self, id, city1, city1, grass1, grass1)

        
    def getTile(self):
        Tile.getTile(self)

#12
#Subclass to represent a specific tile type, one city cap that encompasses 2 sides, with a road on the remaining side
#It has 1 city cap, over on the north and west sides, with the rest being grass
#There are 3 tiles of this type
class DiagonalRoad(Tile):
    def __init__(self):
        city1 = City()
        road1 = Road()
        id = "12"
        Tile.__init__(self, id, city1, city1, road1, road1)

        
    def getTile(self):
        Tile.getTile(self)

#13
#Same as DiagonalRoad but has a crest
#There are 2 tiles of this type
class DiagonalRoadCrest(Tile):
    def __init__(self):
        city1 = City(True)
        road1 = Road()
        id = "17"
        Tile.__init__(self, id, city1, city1, road1, road1)
    
    def getTile(self):
        Tile.getTile(self)

#14
#Subclass to represent a specific tile type, one city cap that encompasses 3 sides, with grass on the remaining side
#It has 1 city cap, over on the north, west and east sides, with the rest being grass
#There are 3 tiles of this type
class ThreeSidedCap(Tile):
    def __init__(self):
        city1 = City()
        grass1 = Grass()
        id = "07"
        Tile.__init__(self, id, city1, city1, city1, grass1)

        
    def getTile(self):
        Tile.getTile(self)

#15
#Same as ThreeSidedCap but has a crest
#There is 1 tile of this type
class ThreeSidedCapCrest(Tile):
    def __init__(self):
        city1 = City(True)
        grass1 = Grass()
        ID = "08"
        Tile.__init__(self, ID, city1, city1, city1, grass1)

        
    def getTile(self):
        Tile.getTile(self)

#16
#Same as ThreeSidedCap but has a road space instead of a None space
#There is 1 tile of this type
class ThreeSidedCapRoad(Tile):
    def __init__(self):
        city1 = City()
        road1 = Road(True)
        id = "05"
        Tile.__init__(self, id, city1, city1, city1, road1)

        
    def getTile(self):
        Tile.getTile(self)

#17
#Same as ThreeSidedCapRoad but has a crest
#There are 2 tile of this type
class ThreeSidedCapRoadCrest(Tile):
    def __init__(self):
        city1 = City(True)
        road1 = Road(True)
        id = "04"
        Tile.__init__(self, id, city1, city1, city1, city1)

        
    def getTile(self):
        Tile.getTile(self)

#18
#Subclass to represent the Monastery tile
#It has a monastery tile in the center of the piece, and nothing else
#There are 4 tiles of this type
class Monastery(Tile):
    def __init__(self):
        grass1 = Grass()
        id = "01"
        Tile.__init__(self, id, grass1, grass1, grass1, grass1)

        
    def getTile(self):
        Tile.getTile(self)

#19
#Same as Monastery but has a road leading up to it
#There are 2 tile of this type
class MonasteryRoad(Tile):
    def __init__(self):
        road1 = Road()
        grass1 = Grass()
        id = "02"
        Tile.__init__(self, id, grass1, grass1, grass1, road1)

        
    def getTile(self):
        Tile.getTile(self)

#20
#Subclass to represent a specific tile type, a town with 4 roads leading out from it
#It has a 4-way crossroad with a town at its center
#There is 1 tiles of this type
class FourWayCrossroad(Tile):
    def __init__(self):
        road1 = Road(True)
        road2 = Road(True)
        road3 = Road(True)
        road4 = Road(True)
        id = "15"
        Tile.__init__(self, id, road1, road2, road3, road4)

        
    def getTile(self):
        Tile.getTile(self)

#21
#Same as 4WayCrossroad but doesn't have the northern road
#There are 4 tile of this type
class TownTJunction(Tile):
    def __init__(self):
        grass1 = Grass()
        road2 = Road(True)
        road3 = Road(True)
        road4 = Road(True)
        id = "16"
        Tile.__init__(self, id, grass1, road2, road3, road4)

        
    def getTile(self):
        Tile.getTile(self)

#22
#Subclass to represent a specific tile type, a tile with a straight road
#It has a road connecting 2 side parallel to each other
#There are 8 tiles of this type
class StraightRoad(Tile):
    def __init__(self):
        road1 = Road(True)
        grass1 = Grass()
        grass2 = Grass()
        id = "18"
        Tile.__init__(self, id, road1, grass1, grass2, road1)

        
    def getTile(self):
        Tile.getTile(self)

#23
#Subclass to represent a specific tile type, a tile with an L road
#It has a road connecting 2 sides perpendicular to each other
#There are 9 tiles of this type
class LRoad(Tile):
    def __init__(self):
        road1 = Road(True)
        grass1 = Grass()
        id = "09"
        Tile.__init__(self, id, grass1, road1, grass1, road1)

        
    def getTile(self):
        Tile.getTile(self)

#24
#Subclass to represent a specific tile type, a city cone
#It has 1 city area connecting 2 parallel sides, with the rest grass
#There is 1 tile of this type
class CityCone(Tile):
    def __init__(self):
        city1 = City()
        grass1 = Grass()
        grass2 = Grass()
        id = "11"
        Tile.__init__(self, id, grass1, city1, city1, grass1)

        
    def getTile(self):
        Tile.getTile(self)

#25
#Same as CityCone but with a crest
#There are 2 tiles of this type
class CityConeCrest(Tile):
    def __init__(self):
        city1 = City(True)
        grass1 = Grass()
        grass2 = Grass()
        id = "06"
        Tile.__init__(self, id, grass1, city1, city1, grass2)

        
    def getTile(self):
        Tile.getTile(self)
        
class TemplateTile(Tile):
    def __init__(self):
        Tile.__init__(self, None, top, right, left, bottom)

        
    def getTile(self):
        Tile.getTile(self)