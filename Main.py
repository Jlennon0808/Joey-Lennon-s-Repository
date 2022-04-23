"""
Simple Math Test For First Integration Project
"""
__author__ = "Joey Lennon"

import math


def print_goodbye():
    """
The purpose of this function is to print a goodbye message after the user has
finished the test.
    """
    print("Congrats you have finished my simple math quiz!")

#Credit to Andrew Krupp for the 'get_int_answer' function
def get_int_answer(prompt):
    """
The purpose of this function is to make sure that the user of the program
is properly entering a whole integer.
    """
    input_is_happening = True
    while input_is_happening:
        try:
            answer = int(input(prompt))
            input_is_happening = False
        except:
            print("Please enter a whole number.")
            input_is_happening = True
    return answer


def main():
    """
    The Purpose of this function is to run the whole program
    """
    x = 1
    name = input("Please Enter Your Name: ")
    print("Welcome", name + ", This is my simple math quiz.")
    if get_int_answer("Please enter a whole number for the question; What is"
                      " 1*1: ") == 1 * 1:
        print("Correct!")
    else:
        print("Incorrect")
    if get_int_answer("What is 14+27: ") == 14 + 27:
        print("Correct!")
    else:
        print("Incorrect")
    if get_int_answer("Please enter a whole number for the question; What is "
                      "52-16: ") == 52 - 16:
        print("Nice Job!")
    else:
        print("Incorrect")
    if get_int_answer("Please enter a whole number for the question; What is"
                      " 64/4: ") == 64 / 4:
        print("That's Right!")
    else:
        print("Incorrect")
    if get_int_answer("Please enter a whole number for the question; What is"
                      " 4**3: ") == 4 ** 3:
        print("Correct!")
    else:
        print("Incorrect")
    if get_int_answer("Please enter a whole number for the question; What is"
                      " 200//10: ") == 200 // 10:
        print("Correct!")
    else:
        print("Incorrect")
    if get_int_answer("Please enter a whole number for the question; What is "
                      "the remainder of 16/6: ") == 16 % 6:
        print("That's Correct!")
    else:
        print("Incorrect")
    if get_int_answer("Please enter a whole number for the question; What is "
                      "14*3: ") == 14 * 3:
        print("Correct!")
    else:
        print("Incorrect")
    if get_int_answer("Please enter a whole number for the question; What is"
                      " 45*16: ") == 45 * 16:
        print("Correct!")
    else:
        print("Incorrect")
    if get_int_answer("Please enter a whole number for the question; What is "
                      "520+740: ") == 520 + 740:
        print("Correct!")
    else:
        print("Incorrect")
    print("Now the question will reappear if you get the answer incorrect.")
    while x < 2:
        if get_int_answer("Please enter a whole number for the question; What"
                          " is 16+2: ") != 16 + 2:
            print("Incorrect, Try Again!")
        elif get_int_answer("Please enter a whole number for the question;"
                            " What is 16+2: ") == 16 + 2:
            print("Correct!")
            x = 3
    print("You will now only get three tries on this next question.")
    for i in range(3):
        if get_int_answer("Please enter a whole number for the question; What"
                          " is 15*3: ") != 15 * 3:
            print("Please enter a whole number for the question; Incorrect,"
                  " Try Again!")
        elif get_int_answer("What is 15*3: ") == 15 * 3:
            print("Correct!")
            break
    print("Find the zeros for the quadratic equation x**2+12x+32: ")
    # I added a quadratic problem in order to recieve two answers from the
    # user, so I could show some boolean logic in the program.
    zero1 = int(input("1st Zero: "))
    zero2 = int(input("2nd Zero: "))
    if zero1 == -8 or zero1 == -4 and zero2 == -4 or zero2 == -8:
        print("Correct!")
    elif not zero1 == -8 or zero1 == -4 and zero2 == -4 or zero2 == -8:
        print("Incorrect!")
    print_goodbye()


if __name__ == "__main__":
    main()
