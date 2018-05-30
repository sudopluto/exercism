# Globals for the bearings
# Change the values as you see fit
EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3


class Robot(object):

    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.x = x
        self.y = y
        self.coordinates = (x , y)
    
    def turn_left(self):
        self.bearing = (self.bearing + 1) % 4
    
    def turn_right(self):
        self.bearing = (self.bearing - 1) % 4
    
    def advance(self):
        if self.bearing == EAST:
            self.x += 1
        elif self.bearing == NORTH:
            self.y += 1 
        elif self.bearing == WEST:
            self.x -= 1
        else:
            self.y -= 1
        self.coordinates = (self.x , self.y)

    def simulate(self, command_str):
        command_mapping = {
            'L' : self.turn_left,
            'R' : self.turn_right,
            'A' : self.advance
        }
        for command in command_str:
            command_mapping[command]()
    


