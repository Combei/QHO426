#The program should start by prompting the user to enter the first number.
#The program should then read in the user’s first number.
#The program should then prompt the user to enter thesecond number.
#The program should then read in the user’s second number.
#The program should then decide which of the two numbers is the smallest and display the message "The first number is the smallest!" if the first number is smaller, "The second number is the smallest!" if the second number is smaller or "Both are equal!" if both numbers are equal in value.

# Ask user for the direction 
print("Please enter the first number.")
first_number = int(input()) 

print("Please enter the second number.")
second_number = int(input())

# Determine which message to display
if (first_number < second_number):
    print("\nThe first number is the smallest.")
elif (first_number > second_number):
    print("\nThe second number is the smallest.")
else:
    print("\nThe two numbers are equal.")