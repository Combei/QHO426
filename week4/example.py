# Python program to get average of a lost

def Average(list):
  return sum(list)/len(list)

#Driver Code
list = [15, 9, 55, 41, 99, 29, 62, 49]
average = Average(list)

#Printing average of the list
print("Average =" , round(average, 2))

#round(average, 2) how many numbers after the rezult just 2 = 44.88 instead of round(average, 4) 44,875