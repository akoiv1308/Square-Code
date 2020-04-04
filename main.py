
def square(value):
  for h in range (value):
    print()
    for i in range (value):
      print("*", end = ' ')

square(10)
print()

def rectangle(length, width):
  for y in range (width):
    print()
    for g in range (length):
      print("*", end = ' ')

rectangle(12, 8)
print()
print()

def rightTriangle(number):
  value = ""
  for j in range (number):
    value += "*"
    print(value)

rightTriangle(5)
print()

def numTriangle(number):
  value = ""
  for w in range(number):
    value += str(w + 1) + " "
    print(value)

numTriangle(5)
print()
