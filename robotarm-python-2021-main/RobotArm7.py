from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')
# Jouw python instructies zet je vanaf hier:

for A in range(1,10):
    robotArm.moveRight()

for B in range(1,6):
    for C in range(1,7):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    for D in range(1,3):
        robotArm.moveLeft()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
