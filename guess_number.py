import random
actual = random.randint(1,100)
while True:
    guess =int(input("guess the random number:"))
    if guess<actual:
        print("your number is less than actual number")
    elif guess>actual:
        print("your number is higher")
    else:
        print("congratulations, you guessed it")
        break
    



