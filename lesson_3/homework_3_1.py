# Input two numbers. If the first one is greater than the second, save first number in result_1,
# otherwise save the second number to the result_1 variable.

first_number = input("First number:")
second_number = input("Second number:")
if first_number > second_number:
    result_1 = first_number
else:
    result_1 = second_number
print(result_1)


# Input a number that is under 20 in number_1 variable. If this number is 20 or
# # higher save “Too high” text to result_2, otherwise save “Thank you”.

number_1 = float(input("Give me any number under 20"))
if number_1 >= 20:
    result_2 = "Too high"
else:
    result_2 = "Thank you"
print(result_2)


# Input your first name and last name in first_name and last_name variables. If the length of your first name is under
# five characters, join them together (without a space) and save it to result_3 variable in upper case. If the length
# of the first name is five or more characters, save their first name in lower case in result_3 variable.

first_name = input("Yor First Name is")
last_name = input("Your Last Name is")
if len(first_name) < 5:
    result_3 = first_name + last_name
    result_3 = result_3.upper()
else:
    result_3 = first_name.lower()
print(result_3)


# Input a number between 10 and 20 (inclusive) and save number to number_2 variable
# If they enter a number within this range, save a message “Thank you” to result_4, otherwise a
# message “Incorrect answer” to result_4.

number_2 = float(input("Please enter a number between 10 and 20"))
result_4 = "Incorrect answer"
if number_2 >= 10:
    if number_2 <=20:
        result_4 = "Thank you"
print(result_4)


# Input your age. If you are 18 or over, save the message “You can vote” in result_5,
# if you are aged 17, save the message “You can learn to drive” in result_5 variable,
# if you are 16, save the message “You can buy a lottery ticket” in result_5,
# if you are under 16, save the message “You can go Trick-or-Treating” in result_5 variable.

age = float(input("Please enter your age"))
if age >= 18:
    result_5 = "You can vote"
elif age >= 17:
    result_5 = "You can learn to drive"
elif age >= 16:
    result_5 = "You can buy a lottery ticket"
else:
    result_5 = "You can go Trick-or-Treating"
print(result_5)


# Input a number between 1 and 12, save this value to month variable. Find which month is it.
# (January, February, March, April, May, June, Jule, August, September, October, November, December)
# Write answer in result_decade in lower case

month = int(input("Please enter the the month's number"))

if month == 1:
    result_month = "January"
elif month == 2:
    result_month = "February"
elif month == 3:
    result_month = "March"
elif month == 4:
    result_month = "April"
elif month == 5:
    result_month = "May"
elif month == 6:
    result_month = "June"
elif month == 7:
    result_month = "July"
elif month == 8:
    result_month = "August"
elif month == 9:
    result_month = "September"
elif month == 10:
    result_month = "October"
elif month == 11:
    result_month = "November"
elif month == 12:
    result_month = "December"
else:
    result_month = "Invalid month number"
print(result_month)
