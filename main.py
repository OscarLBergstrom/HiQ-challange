import sys
import re
from robot import Robot

robot = Robot()

# Prints the grid with the direction of the robot.
def print_grid(robot):
    for y in range(4, -1, -1):
        line = ""
        for x in range(5):
            if((x, y) == robot.position):
                if(robot.direction[2] == "NORTH"):
                    line += "^"
                elif(robot.direction[2] == "EAST"):
                    line += ">"
                elif(robot.direction[2] == "SOUTH"):
                    line += "V"
                elif(robot.direction[2] == "WEST"):
                    line += "<"
            else:
                line += "."
        print(line)
    print("")


for line in sys.stdin:

    # PLACE
    match = re.match('PLACE,([0-4]),([0-4]),(NORTH|EAST|SOUTH|WEST)', line)
    if(match):
        x, y, f = match.groups()
        x, y = int(x), int(y)
        robot.place(x, y, f)

    # MOVE
    elif(re.match('MOVE', line)):
        robot.move()
    # LEFT
    elif(re.match('LEFT', line)):
        robot.turn("LEFT")
    # RIGHT    
    elif(re.match('RIGHT', line)):
        robot.turn("RIGHT")
    # REPORT
    elif(re.match('REPORT', line)):
        robot.report()
    
    print_grid(robot)