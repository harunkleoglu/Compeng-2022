import math
from random import random

# [1 escape1]

print("Which is better?")
print("\tA \\ or a /?")
print("/\\_/\\")
print(" . .")

# [2 escape2]
print("\"-\"-\"-\"-\"")
print("\\       \\")
print("/       /")
print("\\       \\")
print("/       /")
print("\\       \\")
print("\"-\"-\"-\"-\"")


# [3 receipt1]
def main():
    a = 38 + 40 + 30
    b = a * .08
    c = a * .15
    print("Subtotal: " + str(a))
    print("Tax: " + str(b))
    print("Tip: " + str(c))
    print("Total: " + str(a + b + c))


main()


# [4 receipt2]
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


# [5 parameter_mystery1]
# happy and pumpkin were orange
# orange and happy were pumpkin
# orange and sleepy were y
# pumpkin and x were green
# green and pumpkin were vampire

# [6 parameter_mystery2]
# drew  saw the felt
# sue  felt the saw
# sue  drew the b
# b  sue the a
# drew  felt the felt

# [7 range_of_numbers]
def range_of_numbers(a, b):
    if (a < b):
        for i in range(a, b + 1, 1):
            print(i, end=" ")
    if (b < a):
        for i in range(a, b - 1, -1):
            print(i, end=" ")
    if (a == b):
        print(a)


# [8 print_numbers1]
def print_numbers1():
    for i in range(1, 6):
        for j in range(0, i):
            print(i, end="")
        print()


# [9 print_numbers2]
def print_numbers2():
    for i in range(6, 1, -1):
        for j in range(1, i - 1):
            print(".", end="")
        for k in range(0, 7 - i):
            print(7 - i, end="")
        print()


# [10 print_numbers3]
def print_numbers3():
    for i in range(6, 1, -1):
        for j in range(1, i - 1):
            print(".", end="")
        print(7 - i, end="")
        for k in range(0, 6 - i):
            print(".", end="")
        print()


# [11 print_triangle]
def print_triangle():
    for i in range(0, 6):
        for j in range(0, i + 1):
            print("#", end="")
        print()


# [12 print_triangle2]
def print_triangle2():
    for i in range(6, 0, -1):
        for j in range(0, i):
            print("#", end="")
        print()


# [13 print_pyramid]
def print_pyramid():
    for i in range(6, 0, -1):
        for j in range(0, i):
            print(end=" ")
        for j in range(1, 2 * (7 - i)):
            print("*", end="")
        print()


# [14 print_wave]
def print_wave():
    for i in range(1, 5):
        print("v" * i)
        print("v" * i)

    print("v" * 5, end="")
    print()
    for i in range(4, 0, -1):
        print("v" * i)
        print("v" * i)


# [15 arrows]
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


# [16 towers]
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

# [17 five_to_five]
for i in range(-5, 6):
    print(i, end=" ")

# [18 squares]
for i in range(1, 6):
    print(i * i, end=" ")


# [19 fear_the_tree]
def main():
    print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
    print("|| FEAR THE TREE! ||")
    print("////////////////////")


main()


# [20 inches_to_centimeters]
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


# [21 loop_mystery_print1]

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

# [22 stars_print]

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

# [23 binary_to_decimal]

def binary_to_decimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


# [24 box_of_stars]

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


# [25 circle_area]
# IDE kullanırken math kütüphanesini import etmek gerekiyor
# ama codestepbystep'de herhangi bişey import etmeden yapılıyor.
# [import math]

def circle_area(radius):
    return float(math.pi * radius * radius)


# [26 coin_flip]
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


# [27 factorial]
# Recursion kullanarak yaptım, recursion kullanmadan da yapılabilir.

def factorials(n):
    if n == 1 or n == 0:
        return 1
    return n * factorials(n - 1)


def factorial(n):
    print("%d factorial = %d" % (n, factorials(n)))


# [28 print_last_digit]

def print_last_digit(number):
    print("Last digit of %d is %d" % (number, number % 10))


# [29 ascii_figure]

def ascii_figure():
    for i in range(16, -4, -4):
        for j in range(0, i):
            print("/", end="")

        for k in range(32 - (2 * i)):
            print("*", end="")

        for j in range(0, i):
            print("\\", end="")

        print()


# [30 biggest_and_smallest]
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


# [31 piglet] SJ

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


# [32 average_of_3]

def average_of_3(first, second, third):
    sum = first + second + third
    return sum / 3


# [33 blastoff]
# T-minus 5, 4, 3, 2, 1, Blastoff!

# [34 first_digit]
# IDE kullanırken math kütüphanesini import etmek gerekiyor
# ama codestepbystep'de herhangi bişey import etmeden yapılıyor.
# [import math]

def first_digit(number):
    if math.fabs(number) < 10:
        return number
    return int(math.fabs(first_digit(number / 10)))


# [35 is_all_vowels]

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


# [36 loop_squares]

for i in range(1, 11):
    print(i * i, end=" ")


# [37 loop_table]


# [38 random_walk]

def random_walk():
    maxpos = 0
    position = 0
    nextMove = random.randint(0, 1)
    print("position = %d" % position)

    while position != 3 and position != -3:
        if nextMove == 1:
            position -= 1

        if nextMove == 0:
            position += 1

        if position > maxpos:
            maxpos = position

        print("position = %d" % position)
        nextMove = random.randint(0, 1)

    print("max position = %d" % maxpos)


# [39 sum_to]

def sum_to(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


# [40 to_binary]

def to_binary(n):
    if n == 1:
        return "1"
    if n == 0:
        return "0"
    return to_binary(n // 2) + str(n % 2)

# [41 while_loops]

# 10
# zero
# infinity
# 3
# 5
# 7

# [42 while_mystery_1]

# 1 0
# 4 2
# 16 4
# 32 5
# 64 6

# [43 carbonated]

# say coke not pepsi or pop
# say soda not soda or pepsi
# say pepsi not koolaid or pop
# say say not pepsi or pepsi

# [44 print_numbers]

def print_numbers(max):
    for i in range(1, max + 1):
        print("[ %d ]" % i, end=" ")

# [45 print_number_square]

def print_number_square(min, max):
    difference = max-min+1
    start = min

    for i in range(difference):

        for j in range(difference):
            print(start, end="")
            start+=1
            if start == max+1:
                start = min

        start = start+1
        print()

# [46 armstrong_numbers] big brain code

def armstrong_numbers(n):
    for i in range(int(math.pow(10, n - 1)-1), int(math.pow(10, n))):
        number = str(i)
        sum = 0
        for j in number:
            sum += math.pow(int(j), n)
        if sum == i:
            print(i, end=" ")

# [47 count_factors]

def count_factors(n):
    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:  # a factor
            counter += 1
    return counter

# [48 days_in_month]

def days_in_month(month):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return months[month-1]

# [49 divisible_by_6 ]

number = int(input("Type a number: "))
if number % 2 == 0:
    if number % 3 == 0:
        print("Divisible by 6.")
else:
    print("Odd.")

# [50 fraction_sum]

def fraction_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum += (1/i)
    return sum

# [51 count_even_digits]

def count_even_digits(number, leng):
    num = str(number)
    counter = 0
    for i in num:
        if int(i) % 2 == 0:
            counter += 1
    return counter

# [52 expressions_mix1]

# 15.5
# 8.4
# -2
# 24
# 1.0
# False
# False
# False

# [53 factor_count]

def factor_count(n):
    counter = 0
    for i in range(1,n+1):
        if n % i == 0:
            counter +=1
    return counter

# [54 even_average]

def even_average():
    counter = 0
    sum = 0

    while 1 > 0:
        num = int(input("Integer? "))
        if num == 0: break

        if num % 2 == 0:
            sum += num
            counter += 1
    if float(sum / counter)>100:
        print("Average: %.2f" % float(sum / counter))
    else:
        print("Average: %.2f" % float(sum / counter))


even_average()

# [55 even_sum_max]

def even_sum():
    count = int(input("how many integers? "))
    evenSum = 0
    evenMax = 0

    for i in range(count):
        number = int(input("next integer? "))
        if number % 2 == 0:
            evenSum += number
            if number>evenMax:
                evenMax = number

    print("even sum = %d" % evenSum)
    print("even max = %d" % evenMax)

# [56 stanford_vs_cal]

def stanford_vs_cal():
    stanford = int(input("Stanford: How many points did they score? "))
    cal = int(input("Cal: How many points did they score? "))
    if cal > stanford:
        print("Cal won!")
    else:
        print("Stanford won!")


stanford_vs_cal()

# [57 compute_distance]

def compute_distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# [58 is_multiple]

def is_multiple(a, b):
    if a % b ==0: return True
    else: return False

# [59 is_prime_number]

def is_prime_number(n):
    if n == 1 or n == 0 or n < 0: return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# [60 triangle]

def triangle(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end="")
        for k in range(i):
            print("*",end="")
        print()

# [61 contains_twice]

def contains_twice(text, ch):
    counter = 0
    for i in text:
        if i == ch:
            counter+=1
    if counter>=2:
        return True
    else:
        return False

# [62 marshall_mathers]

# 10
# 25
# 2
# -1
# "Dog"
# "hers"
# "Pytho"
# "mathers"

# [63 name_game]

def name_game():
    inp = input("What is your name? ")
    name = inp.split()

    print(name[0] + ", " + name[0] + ", bo-B" + name[0][1:])
    print("Banana-fana" + " fo-F" + name[0][1:])
    print("Fee-fi-mo-M" + name[0][1:])
    print(name[0].upper() + "!")
    print()
    print(name[1] + ", " + name[1] + ", bo-B" + name[1][1:])
    print("Banana-fana" + " fo-F" + name[1][1:])
    print("Fee-fi-mo-M" + name[1][1:])
    print(name[1].upper() + "!")


name_game()

# [64 star_figures]

def DoubleLine():
    print("*****\n*****")

def Star():
    print(" * *\n"
          "  *\n"
          " * *")

def Line():
    print("  *\n"
          "  *\n"
          "  *")

def Empty():
    print()

def Main():
    DoubleLine()
    Star()
    Empty()
    DoubleLine()
    Star()
    DoubleLine()
    Empty()
    Line()
    DoubleLine()
    Star()

Main()

# [65 strange]

# Inside first function
# Inside third function
# Inside first function
# Inside second function
# Inside first function
# Inside second function
# Inside first function
# Inside third function
# Inside first function
# Inside second function
# Inside first function
# Inside first function
