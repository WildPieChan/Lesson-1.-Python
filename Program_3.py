# Write a program that takes the coordinates of a point (X and Y) as
# input, with X ≠ 0 and Y ≠ 0 and outputs the number of the quarter
# of the plane in which this point is located (or on which axis it is located).

x = float(input("~Computer~ Enter X coordinate: "))
y = float(input("~Computer~ Enter Y coordinate: "))

if (x > 0) and (y > 0):
    print("~Computer~ 1")
elif (x < 0) and (y > 0):
    print("~Computer~ 2")
elif (x < 0) and (y < 0):
    print("~Computer~ 3")
elif (x > 0) and (y < 0):
    print("~Computer~ 4")
else:
    print("~Computer~ Point isn't on any quarter of the plane")