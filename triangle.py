import random
def calc_area(h= 4, b = 6):
  area = h*b*0.5
  print(area)
  return area

def run():
  print(calc_area(random.randint(1, 4)))
  a1 = calc_area(10, 9)
  a2 = calc_area(2, 2)
  if a1>a2:
    print("Area 1 is bigger")
  print(calc_area(100))
  print(calc_area(b=20))
  calc_area()

run() 