#We wish to create a program that allows us to help Beep learn to paint.

#The program should start by prompting the user for a direction to move the paint brush (up, down, left or right).
#The program should then work out in which direction Beep should paint and display a suitable message.

#An example run of such a program is shown below:

print("Towards which direction should I paint (up, down, left or right)?")
direction = input() 
if (direction == "up"):
  print("\nI am painting up!")
elif (direction == "down"):
  print("\nI am painting to down!")
elif (direction == "left"):
  print("\nI am painting to left!")
elif (direction == "right"):
  print("\nI am painting to right!")
else: 
  print("\nNot sure which direction in am painting in!")

