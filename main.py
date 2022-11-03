import random
upperbound=input("type a number: ")

if upperbound.isdigit():
    upperbound=int(upperbound)
    if upperbound <=0:
        print("please enter a number larger than zero")
        quit()
else:
    print("please enter a number ")
    quit()


random_number=random.randint(0,upperbound)
guesses=0

while True:
    guesses +=1
    guess_num=input("Guess a number")
    if guess_num.isdigit():
        guess_num = int(guess_num)

    else:
        print("please enter a number ")
        continue

    if guess_num==random_number:
        print("you are right!!")
        break
    else:
        if guess_num > random_number:
            print("you were above the number")
        else:
            print("you were below the number")
print("you got it in " +str(guesses) +" guesses")