class Robot:

    def __init__(self, x=None, y=None, direction='NONE'):
        self.position = (x, y)
        self.set_robot_dir(direction)
        self.all_directions = ["NORTH", "EAST", "SOUTH", "WEST"]

    # Maps all directions to a vector and string for future use. 
    def set_robot_dir(self, f):
        direction_map = {
            "NORTH": (0, 1, "NORTH"),
            "EAST": (1, 0, "EAST"),
            "SOUTH": (0, -1, "SOUTH"),
            "WEST": (-1, 0, "WEST"),
            "NONE": (0, 0, "NONE")
        }

        self.direction = direction_map.get(f, (0, 0, "NONE"))
    
    # Checks if both x and y is within the bounds of the table.
    # RETURNS TRUE if x and y is within the bounds. 
    def inside_table(self, x, y):
        if (x > 4 or x < 0) or (y > 4 or y < 0):
            return False
        return True

    # Places the robot on coordinates x,y. Sets the direction to f. 
    def place(self, x, y, f):
        if(self.inside_table(x, y)):
            self.position = (x, y)
            self.set_robot_dir(f)

    # Moves the robot 1 unit in the direction the robot is facing. 
    # Does not move the robot if the move is out of bounds.
    def move(self):
        if(self.position[0] == None or self.position[1] == None):
            return
        x, y = self.position[0] + self.direction[0], self.position[1] + self.direction[1]
        if(self.inside_table(x, y)):
            self.position = (x, y)

    # Turns the robot 90 degrees to either left or right.
    # Does not turn the robot if the direction is NONE
    def turn(self, rot):

        if(self.direction == (0, 0, "NONE")):
            return

        # Takes the index value for the current direction in all_directions
        direction_index = self.all_directions.index(self.direction[2])
        
        if(rot == "LEFT"):
            turn = -1
        elif(rot == "RIGHT"):
            turn = 1 
        
        # Sets the direction to either the left or the right through the turn variable. Modulo of inorder to fix under and overflow.
        self.set_robot_dir(self.all_directions[(direction_index + turn) % len(self.all_directions)])
    
    # Prints out the location and direction of the robot
    def report(self):
        print("POSITION IN (X, Y):", self.position)
        print("FACING DIRECTION:", self.direction[2])
