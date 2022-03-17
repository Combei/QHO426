#The program should ask the user to enter three numbers (one number at a time) and should work out how many of these are even and odd. Finally, the program should display the number of even numbers and odd numbers entered.

# Ask user for numbers 
print("Please enter the first whole number?")
first_number = int(input())

print("Please enter the second whole number?")
second_number = int(input())

print("Please enter the third whole number?")
third_number = int(input()) 

even_numbers = 0
odd_numbers = 0 

# Determine which numbers are even and which are odd
if (first_number % 2 == 0):
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

if (second_number % 2 == 0):
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

if (third_number % 2 == 0):
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

# Display result
print("There were {} even and {} odd numbers.".format(even_numbers, odd_numbers))