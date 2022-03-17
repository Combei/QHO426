#We wish to create a program that allows us to help Beep by suggesting activities for Beep to complete.

#The program should start by asking the user to enter an activity.
#If the activity is "calculate" then the message "Performing calculations..." should be displayed otherwise the message "Performing activity..." should be displayed.
#Finally, the program should display "Activity completed!".

# Ask user for the type of activity
print("Please enter the activity to be performed.")
activity = input() 

# Determine if the activity is calculate
if (activity == "calculate"):
    print("\nPerforming calculations...")
else:
    print("\nPerforming activity...")

# Display message
print("\nActivity completed.")