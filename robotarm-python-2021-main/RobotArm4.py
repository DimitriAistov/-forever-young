from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:

for A in range(1,4):
    robotArm.grab()
    for Right1 in range(1,3):
        robotArm.moveRight()
    robotArm.drop()
    for Left1 in range(1,3):
        robotArm.moveLeft()

for B in range(1,3):
    robotArm.moveRight()

for C in range(1,4):
    robotArm.grab()
    for Left2 in range(1,2):
        robotArm.moveLeft()
    robotArm.drop()
    for Right2 in range(1,2):
        robotArm.moveRight()




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
