#The program should start by prompting the user to enter a whole number.
#The program should then work out if the number is even or odd.
#Finally, the program should display a suitable message to indicate if the number is even or odd.# Ask user for a number 

print("Please enter a whole number.")
number = int(input()) 

# Display relevant message
if (number % 2 == 0):
    print("\nThe number {} is an even number.".format(number))
else:
    print("\nThe number {} is an odd number.".format(number))