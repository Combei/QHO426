#Declare a tuple
p = ("Cristian", 34, False)
y = tuple([3, 6, 9])
#Print tuple
print(p)
print(y)
print(p[1])
print(y[0]*y[2])
#Cannot change values in tuple  => immutable
#y[1] = 7778
#y.append(8)

#Cancatenate tuple
z = p + y
print(z)
print(p)
print(y)
