# Name:Joey Lennon
# Description of Program: Math Test
import math


def printgoodbye():
    print("Congrats you have finished my simple math quiz!")


x = 1
name = input("Enter Name: ")
print("Welcome", name + ", This is my simple math quiz.")
answer1 = int(input("What is 1*1: "))
if answer1 == 1 * 1:
    print("Correct!")
else:
    print("Incorrect")
answer2 = int(input("What is 14+27: "))
if answer2 == 14 + 27:
    print("Correct!")
else:
    print("Incorrect")
answer3 = int(input("What is 52-16: "))
if answer3 == 52 - 16:
    print("Nice Job!")
else:
    print("Incorrect")
answer4 = int(input("What is 64/4: "))
if answer4 == 64 / 4:
    print("That's Right!")
else:
    print("Incorrect")
answer5 = int(input("What is 4**3: "))
if answer5 == 4 ** 3:
    print("Correct!")
else:
    print("Incorrect")
answer6 = int(input("What is 200//10: "))
if answer6 == 200 // 10:
    print("Correct!")
else:
    print("Incorrect")
answer7 = int(input("What is the remainder of 16/6: "))
if answer7 == 16 % 6:
    print("That's Correct!")
else:
    print("Incorrect")
answer8 = int(input("What is 14*3: "))
if answer8 == 14 * 3:
    print("Correct!")
else:
    print("Incorrect")
answer9 = int(input("What is 45*16: "))
if answer9 == 45 * 16:
    print("Correct!")
else:
    print("Incorrect")
answer10 = int(input("What is 520+740: "))
if answer10 == 520 + 740:
    print("Correct!")
else:
    print("Incorrect")
print("Now the answer will reappear if you get the answer incorrect.")
while x < 2:
    answer11 = int(input("What is 16+2: "))
    if answer11 != 16 + 2:
        print("Incorrect, Try Again!")
    elif answer11 == 16 + 2:
        print("Correct!")
        x = 3
print("You will now only get three tries on this next question.")
for i in range(3):
    answer12 = int(input("What is 15*3: "))
    if answer12 != 15 * 3:
        print("Incorrect, Try Again!")
    elif answer12 == 15 * 3:
        print("Correct!")
        break
print("Find the zeros for the quadratic equation x**2+12x+32: ")
zero1 = int(input("1st Zero: "))
zero2 = int(input("2nd Zero: "))
if zero1 == -8 or zero1 == -4 and zero2 == -4 or zero2 == -8:
    print("Correct!")
elif not zero1 == -8 or zero1 == -4 and zero2 == -4 or zero2 == -8:
    print("Incorrect!")
printgoodbye()
