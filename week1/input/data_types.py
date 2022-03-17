#We wish to create program that allows Beep to learn more about us.  The program should start by asking the user to enter their name, age (in years), weight (in kilograms) and height (in meters). The program should then use this information to calculate the user's body-mass index (bmi) and display the result with a suitable message that includes their name and age.
#Note that the bmi can be calculated by dividing the weight (kg) by the height squared.  To work out the square of the height you can multiply the height by itself or use the power operator (**) e.g. height ** 2.  You can learn more about the power operator by clicking here.

print("What is your name, human?")
name = input()
print("How old are you (in years)?")
age = int(input())
print("How tall are you(in m)?")
height = float(input())
print("How much do you weight(in kg)?")
weight = float(input())
bmi =  weight/(height**2)
print(f"{name} you are {age} years old. Your BMI is {bmi}")

# or we can do it as this

# Read in user data 
  print("What is your name?")
  name = input() 
  
  print("What is your age?")
  age = int(input())
  
  print("What is your weight?") 
  weight = float(input()) 
  
  print("What is your height?")
  height = float(input())
  
  # Calculate bmi
  bmi = weight / (height ** 2)
  
  # Display result
  print(f"{name} your bmi is {bmi}")