side1 = int(input())
side2 = int(input())
side3 = int(input())

if side1 + side2 > side3:
    if side1 == side2 == side3:
        print('equilateral')
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print('isosceles')
    else:
        print('scalene')    
else:
    print('not a triangle')