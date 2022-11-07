import random

x= random.randint(1,10)
print(x)

for i in range(1,4):
    try:
        y = int(input("Can you please guess the integer between 1 and 10 ("+str(i)+" guess) : "))
        if y < x:
            print("Your guess is low")
        elif y > x:
            print("Your guess is high")
        else:
            print("you guessed it right")
            print("You guessed the number in attempt : ",i)
            break
    except NameError:
        print("It is not a valid number")
        print(NameError)
    except ValueError:
        print("It is not a valid number")
        print(ValueError)

print("*****************************")
if y!=x: print("Sorry the number is : ",x)

