from math import sqrt

class Robot:
    def __init__(self):
        self.position = [0,0]

my_robot = Robot()

directions = ["UP", "DOWN", "LEFT", "RIGHT"]

for i in directions:
    movement = input(f"{i}:")
    if i == "UP":
        my_robot.position[1] += int(movement)
    elif i == "DOWN":
        my_robot.position[1] -= int(movement)
    elif i == "LEFT":
        my_robot.position[0] -= int(movement)
    else:
        my_robot.position[0] += int(movement)


print(round(sqrt(my_robot.position[0] ** 2 + my_robot.position[1] ** 2)))