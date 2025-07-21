#..............................................SNAKE, WATER, GUN GAME..............................................#
import random

k = random.choice(["snake", "water", "gun"])
l = input("Your Turn (snake / water / gun): ")
a = k.lower()
b = l.lower()

if b not in ["snake", "water", "gun"]:
    print("Invalid Input")
elif a == "snake" and b == "water":
    print("Computer Enters:", a)
    print("You Entered:", b)
    print("Computer won, You lose")
elif a == "snake" and b == "gun":
    print("Computer Enters:", a)
    print("You Entered:", b)
    print("You won, Computer lose")
elif a == "water" and b == "gun":
    print("Computer Enters:", a)
    print("You Entered:", b)
    print("Computer won, You lose")
elif a == "water" and b == "snake":
    print("Computer Enters:", a)
    print("You Entered:", b)
    print("You won, Computer lose")
elif a == "gun" and b == "snake":
    print("Computer Enters:", a)
    print("You Entered:", b)
    print("Computer won, You lose")
elif a == "gun" and b == "water":
    print("Computer Enters:", a)
    print("You Entered:", b)
    print("You won, Computer lose")
elif a == b:
    print("Computer Enters:", a)
    print("You Entered:", b)
    print("Match Draw")
