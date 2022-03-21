#The first function should be named movements and should have no parameters.
#The function should create a list named path.
#The function should populate the list with the following values: "Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1
#Finally, the function should return the list named path.
#The second function should be named run and should have no parameters.
#The function should start by displaying the message "Moving...".
#The function should then call the first function and store the return list in a local variable
#The function should then display the values in the list in the following format: "{direction} for {steps} steps" where {direction} is the direction of movement and {steps} is the number of steps to move.

def movement():
  path = ["Move Forward",10 , "Move backward",5 , "Move left",3 , "Move right",1 ]
  return path
def run():
  print("Moving...")
  path = movement()
  
  print(f"{path[0]} for {path[1]} steps")
  print(f"{path[2]} for {path[3]} steps")
  print(f"{path[4]} for {path[5]} steps")
  print(f"{path[6]} for {path[7]} steps")
run()