# 1
import math
from random import random

print("Which is better?")
print("\tA \\ or a /?")
print("/\\_/\\")
print(" . .")

# 2
print("\"-\"-\"-\"-\"")
print("\\       \\")
print("/       /")
print("\\       \\")
print("/       /")
print("\\       \\")
print("\"-\"-\"-\"-\"")


# 3
def main():
    a = 38 + 40 + 30
    b = a * .08
    c = a * .15
    print("Subtotal: " + str(a))
    print("Tax: " + str(b))
    print("Tip: " + str(c))
    print("Total: " + str(a + b + c))


main()


# 4
def main():
    # Calculate total owed, assuming 8% tax / 15% tip
    subtotal = int(input("What was the meal cost? $"))
    tax = subtotal * .08
    tip = subtotal * .15
    total = subtotal + tax + tip

    print("Subtotal:", subtotal)
    print("Tax:", tax)
    print("Tip:", tip)
    print("Total:", total)


main()


# 5
# happy and pumpkin were orange
# orange and happy were pumpkin
# orange and sleepy were y
# pumpkin and x were green
# green and pumpkin were vampire

# 6
# drew  saw the felt
# sue  felt the saw
# sue  drew the b
# b  sue the a
# drew  felt the felt

# 7
def range_of_numbers(a, b):
    if (a < b):
        for i in range(a, b + 1, 1):
            print(i, end=" ")
    if (b < a):
        for i in range(a, b - 1, -1):
            print(i, end=" ")
    if (a == b):
        print(a)


# 8
def print_numbers1():
    for i in range(1, 6):
        for j in range(0, i):
            print(i, end="")
        print()


# 9
def print_numbers2():
    for i in range(6, 1, -1):
        for j in range(1, i - 1):
            print(".", end="")
        for k in range(0, 7 - i):
            print(7 - i, end="")
        print()


# 10
def print_numbers3():
    for i in range(6, 1, -1):
        for j in range(1, i - 1):
            print(".", end="")
        print(7 - i, end="")
        for k in range(0, 6 - i):
            print(".", end="")
        print()


# 11
def print_triangle():
    for i in range(0, 6):
        for j in range(0, i + 1):
            print("#", end="")
        print()


# 12
def print_triangle2():
    for i in range(6, 0, -1):
        for j in range(0, i):
            print("#", end="")
        print()


# 13
def print_pyramid():
    for i in range(6, 0, -1):
        for j in range(0, i):
            print(end=" ")
        for j in range(1, 2 * (7 - i)):
            print("*", end="")
        print()


# 14
def print_wave():
    for i in range(1, 5):
        print("v" * i)
        print("v" * i)

    print("v" * 5, end="")
    print()
    for i in range(4, 0, -1):
        print("v" * i)
        print("v" * i)


# 15
def main():
    arrowTop()
    arrowMid()
    empty()
    arrowTop()
    arrowMid()
    empty()
    lines()
    lines()
    arrowTop()
    arrowMid()
    empty()
    print("\\  /")
    print(" \\/")
    arrowTop()
    arrowMid()
    empty()


def arrowTop():
    print(" /\\")


def arrowMid():
    print("/  \\")


def lines():
    print(" ||")


def empty():
    print()


main()


# 16
def main():
    towerTop()
    lines()
    towerStruct()
    lines()
    empty()
    towerTop()
    lines()
    towerStruct()
    empty()
    towerTop()
    towerStruct()


def towerTop():
    print("  *")
    print(" ***")
    print("*****")


def towerStruct():
    print(" ###")
    print(" ###")


def empty():
    print()


def lines():
    print("-----")
    print("-----")


main()

# 17
for i in range(-5, 6):
    print(i, end=" ")

# 18
for i in range(1, 6):
    print(i * i, end=" ")


# 19
def main():
    print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
    print("|| FEAR THE TREE! ||")
    print("////////////////////")


main()


# 20
def main():
    print("This program converts feet and inches to centimeters.")
    feet = int(input("Enter number of feet: "))
    inch = int(input("Enter number of inches: "))
    print("%d ft %d in = %.2f cm" % (feet, inch, float(converter(feet, inch))))


def converter(feet, inch):
    feet += inch / 12
    cm = feet * 30.48
    return float(cm)


main()


# -21-

#         *
#        ***
#       *****
#      *******
#     *********
#    ***********
#   *************
#  ***************
# *****************
# *******************

# -22-

# A)

# **********
# **********
# **********
# **********
# **********

# B)

# *
# **
# ***
# ****
# *****

# C)

# 1
# 22
# 333
# 4444
# 55555

# -23-

def binary_to_decimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


# -24-

def box_of_stars(width, height):
    for i in range(width):
        print("*", end="")
    print()
    for i in range(height - 2):
        print("*", end="")
        print(" " * (width - 2), end="")
        print("*", end="")
        print()

    for i in range(width):
        print("*", end="")
    print()


# -25-
# IDE kullanırken math kütüphanesini import etmek gerekiyor
# ama codestepbystep'de herhangi bişey import etmeden yapılıyor.
# [import math]

def circle_area(radius):
    return float(math.pi * radius * radius)


# -26-
# IDE kullanırken random kütüphanesini import etmek gerekiyor
# ama codestepbystep'de herhangi bişey import etmeden yapılıyor.
# [import random]

def coin_flip(k, characterSide):
    rowCounter = 0
    coinSides = ['H', 'T']
    if (characterSide == 'H' or characterSide == 'T') and (k >= 0):
        while rowCounter != k:
            side = random.randint(0, 1)

            print(coinSides[side], end=" ")

            if characterSide == coinSides[side]:
                rowCounter += 1
            else:
                rowCounter = 0

        print()
        print("You got %s %d times in a row!" % (characterSide, k))
    else:
        print("ERROR!")


# -27-
# Recursion kullanarak yaptım, recursion kullanmadan da yapılabilir.

def factorials(n):
    if n == 1 or n == 0:
        return 1
    return n * factorials(n - 1)


def factorial(n):
    print("%d factorial = %d" % (n, factorials(n)))


# -28-

def print_last_digit(number):
    print("Last digit of %d is %d" % (number, number % 10))


# -29-

def ascii_figure():
    for i in range(16, -4, -4):
        for j in range(0, i):
            print("/", end="")

        for k in range(32 - (2 * i)):
            print("*", end="")

        for j in range(0, i):
            print("\\", end="")

        print()


# -30-
# IDE kullanırken random kütüphanesini import etmek gerekiyor
# ama codestepbystep'de herhangi bişey import etmeden yapılıyor.
# [import random]

count = int(input("How many numbers? "))
if count > 0:
    # Boş bir array tanımlamak için burada list = [] kullandım
    list = []
    for i in range(count):
        num = int(input("Next number? "))
        list.append(num)

    list.sort()
    print("Biggest = %d" % list[count - 1])
    print("Smallest = %d" % list[0])


# -31- SJ

def piglet_game():
    score = 0
    rolled = random.randint(1, 10)
    print("Welcome to Piglet!")
    print("You rolled a %d" % rolled)

    if rolled == 1:
        print("You got %d points." % score)
        SystemExit

    answer = input("Roll again? ")
    score += rolled
    while answer == "y" or answer == "yes":
        rolled = random.randint(1, 10)
        score += rolled
        print("You rolled a %d" % rolled)
        if rolled == 1:
            score = 0
            break
        else:
            answer = input("Roll again? ")
    print("You got %d points." % score)


piglet_game()


# -32-

def average_of_3(first, second, third):
    sum = first + second + third
    return sum / 3


# -33-
# T-minus 5, 4, 3, 2, 1, Blastoff!

# -34-
# IDE kullanırken math kütüphanesini import etmek gerekiyor
# ama codestepbystep'de herhangi bişey import etmeden yapılıyor.
# [import math]

def first_digit(number):
    if math.fabs(number) < 10:
        return number
    return int(math.fabs(first_digit(number / 10)))


# -35-

def is_all_vowels(text):
    text = text.lower()
    checkAll = True
    vowels = ["a", "e", "i", "o", "u"]

    for i in text:
        if i in vowels:
            checkAll = True
        else:
            checkAll = False
            break

    return checkAll


# -36-

for i in range(1, 11):
    print(i * i, end=" ")
