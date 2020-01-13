# Write a program that prints the numbers from 1 to 100. You can use Python's range() to quickly make a list of numbers.
def one_to_onehundred():
    for number in range(1,101):
        print(number)


# For multiples of five (5, 10, 15, etc.) print "Chicken" instead of the number

# For the multiples of seven (7, 14, 21, etc.) print "Monkey".

# For numbers which are multiples of both five and seven print "ChickenMonkey".

# To determine if a number can be evenly divided by 5 or 7, use the Python modulo operator.

def chickenMonkey():
    for n in range(1,101):
        if (n % 5 == 0) & (n % 7 ==0):
            print("ChickenMonkey")
        elif n % 5 == 0:
            print("Chicken")
        elif n % 7 == 0:
            print("Monkey")
        else:
            print(n)

chickenMonkey()