x = int(input("x = "))
y = int(input("y = "))
if x == 0 and y == 0:
    location = "at the origin (0,0)"
elif x > 0 and y > 0:
    location = "in the first quadrant"
elif x < 0 and y > 0:
    location = "in the second quadrant"
elif x < 0 and y < 0:
    location = "in the third quadrant"
else:
    location = "in the fourth quadrant"

print(f"The point P({x}, {y}) is  {location} of the coordinate system")