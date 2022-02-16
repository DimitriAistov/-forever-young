from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:

for A in range(1,8):
    robotArm.moveRight()

for B in range(1,9):
    robotArm.grab()
    for Right in range(1,2):
        robotArm.moveRight()
    robotArm.drop()
    for Left in range(1,3):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
