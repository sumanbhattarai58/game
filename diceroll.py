
import random
a=input("do you want to roll the dice?")
if (a=="y"):
    dice=random.randint(1,6)
    print("you rolled :",dice)
elif (a=="n"):
    print("so you dont want to play")
else:
    print("you need to type y/n")
robot_roll=random.randint(1,6)
print("the robot rolled:",robot_roll)
if dice>robot_roll :
    print("you won the robot")
elif dice==robot_roll:
    print("you and robo got the same score. so play again")
else :
    print("you lost with the robot")
