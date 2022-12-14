class Circle:
    def __init__(self, r=1):
        self.r = r
        self.__pi = 3.1412
    
    def area(self):
        return self.__pi * self.r ** 2
    
    def circumference(self):
        return 2 * self.__pi * self.r
    
    def __str__(self):
        return f'A circle with the radius of {self.r}'

# This part will run if the script is executed as a Python program
if __name__ == '__main__':
    c1 = Circle(4)
    print(f'Area={c1.area()}, circumference={c1.circumference()}')
    print(c1)