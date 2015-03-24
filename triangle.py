def triangles(size):
  for i in range(1, size +1):
    for c in range(i):
      print("T", end="")
    print()

  for i in range(1, size):
    for c in range(size-i):
      print("T", end="")
    print()

size=int(input("Size of the triangle: "))
triangles(size)
