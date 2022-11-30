# Write a Python script to ask for the length and width of a rectangle, 
# calculate and print the perimeter and area of the rectangle.
# E.g.
# Enter length: 5
# Enter width: 3
# perimeter = 16, area = 15.

try:
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
except:
    print('Error! Invalid input value.')
else:
    print(f'perimeter = {2*length + 2*width}, area = {length * width}')
