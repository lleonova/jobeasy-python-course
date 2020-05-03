# WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1, then enter a character and save it in the variable char_1.
# Write function counter, which will count how many times your character is included in your string

string_1 = "thank you for participating in our Python Class"
char_1 = "i"

def counter(string, char):
    count = string.count(char)
    return count

#   number = 0
#   for character in string:
#      if character == char:
#           number += 1
#   return (number)

char_in_string = counter(string_1, char_1)
print(char_in_string)

# Enter a random number and save it in variable number_1. Then create a function number_multiplication
# that will multiply all the digits together and return the result.

number_1 = 1497465498
def number_multiplication(number):
    result = 1
    string_1 = str(number)
    for char in string_1:
        result *= int(char)
    return result

print(number_multiplication(number_1))


# Enter a random number and save it in variable number_2. Then create function number_reverse which will return
# a number with digits of number_1 in reverse order

number_2 = 7765

def number_reverse(number):
    string_5 = str(number)[::-1]
    result = int(string_5)
    return result

print (number_reverse(number_2))