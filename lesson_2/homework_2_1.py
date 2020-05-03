# Create three strings using three different methods. Save your result to result_string_1, result_string_2,
# result_string_3 variables

result_string_1 = 'abc'
result_string_2 = "abc"
result_string_3 = '''abc'''
print(type(result_string_1 ))
print(type(result_string_2 ))
print(type(result_string_3 ))


# Enter a string with your name using console and save the result to result_name variable
print("Please enter your name:")
result_name = input()
print("I\'ve got: " + result_name  )

# Enter your first and  last name. Join them together with a space in
# between. Save a result in a variable result_full_name and
# save the length of the whole name in result_full_name_length variable.

first_name = input("Please enter your First Name:")
last_name = input("Please enter your Last Name:")
result_full_name = first_name + ' ' + last_name
print("Your Full Name is: " + result_full_name )
result_full_name_length = len(result_full_name )
print("Your Full Name has " + str(result_full_name_length) + " characters")
print(result_full_name_length )

# Enter the capital city of California State in lower case. Change the case to title case.
# Save the result in result_ca_capital variable

result_ca_capital = 'Sacramento'.lower()
print(result_ca_capital )
result_ca_capital1 = 'sacramento'.capitalize()
print(result_ca_capital1 )

# Enter the name of our planet. Change the case to upper case. Save the result in
# result_planet variable

result_planet = 'Earth'.upper()
print(result_planet )