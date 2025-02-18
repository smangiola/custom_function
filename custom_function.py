def area(base, height): #function that calculates the area of a triangle
    if base <= 0: 
        return 'Cannot calculate. The base is too low.' #will return this statement if the base is 0 or less
    elif height <= 0:
        return 'Cannot calculate. The height is too low.' #will return this statement if the height is 0 or less
    else: #if both the base and height are greater than 0...
        return (height*base)/2 #then the area of the triangle is returned

print(area(5, 6))
print(area(0, 2))
print(area(3, 0))
    