#Declare an empty list
bleh = []
meh = list()
#Declare non-empty list
yummy = ["Pizza", "Lasagna", "Spaghetti Bolognese"]
#Print entire list
print(yummy)
#Print single item
print(yummy[2])
#Printing some elements
print(yummy[:2])
#Add elements to our list (expand it) - adding elements at the end
print(bleh)
bleh.append("Fish")
bleh.append("Coconut")
bleh.append("Onion")
bleh.append("Chocolate")
print(bleh)
#Add multiple items to list, based on user input
n = int(input("How many items to add"))
for i in range(5):
  yummy.append(input("Enter a new yummy food: "))
print(yummy)
#Adding data at any point inside a list
print(bleh)
bleh.insert(1, "mash potatoes")
print(blah)
bleh.insert(3, "cabbege")
print(bleh)
#Remove an item from list
if "Frankfurters" in bleh:
  bleh.remove("Frankfurters")
if "Coconut" in bleh:
   bleh.remove("Coconut")
print(bleh)
#Remove items via index
bleh.pop(2)
print(bleh)
print(x)
#Alternative way of deleting via index
del bleh[1]
print(bleh)
#Extending a list
print(yummy)
yummy.extend(["fish", "Bacon", "ketchup"])
print(yummy)
lista = ["fred", True, 6, 8, -7.88, False, "Lalala", 55]
total = 0
for item in lista:
  if isinstance(item, str):
      total += item

print(total)
