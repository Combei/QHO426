print("What is your name?")
n = input()
if len(n) > 8:
  print("You have a name to long. Please use a nickname!")
elif len(n) <=4:
  print("Your name is to short")
elif n == "Martha":
  print ("Why did you say that name?")
else:
  print("Nice to meet you!")
  
print("Please try again")
