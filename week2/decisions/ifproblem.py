# check whether first number is bigger than the second number.
# Assume first_number and second_number are existing variables.
    if (first_number > second_number):
        print("First is bigger!")
    
    print("Done!")
  
  
  We wish to create a program that allows us to specify what type of book is being read by Beep.
    
    The program should start by asking the user to enter the type of book e.g. adventure.
    If the book is an "adventure" book then the message "I like adventure books!" should be displayed.
    Finally, the program should display "Finished reading book!".


Ask user for the type of book 
print("What type of book is this?")
book_type = input() 

# Determine if the book is an adventure book
if (book_type == "adventure"):
    print("\nI like adventure books!")

# Display message
print("\nFinished reading book.")