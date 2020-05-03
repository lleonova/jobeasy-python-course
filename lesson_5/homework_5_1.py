# FOR LOOPS EXERCISES

# Enter your name, save it in name variable and create function print_name_three_times which returns
# value that is equal to your name three times

name_1 = "Luda"

def print_name_three_times(name):
    return name * 3

print_name_three_time = print_name_three_times(name_1)
print(print_name_three_time)


# Modify your previous program so that it will enter your name (save it in variable  name_2) and a number
# (save in variable number) and then display their name that number of times. Each time add your name to result
# variable

name_2 = "Lyudmila"
number_1 = 8

def print_name_number_times(number, name):
    return name * number

print_name = print_name_number_times(name_2, number_1)
print(print_name)


# Enter a random string, which includes only digits. Write function sum_digits which find a sum of digits in this string

string_number_1 = "192939495969798909"

def sum_digits(string_val):
    result = 0
    for char in string_val:
        result += int(char)
    return result

sum_of_digits = sum_digits(string_number_1)
print(sum_of_digits)

# Create function which sums up all even numbers between 2 and 100 (include 100)

def sum_even_numbers():
    result = 0
    for num in range(2, 101, 2):
        result += num
    return (result)

print(sum_even_numbers())
