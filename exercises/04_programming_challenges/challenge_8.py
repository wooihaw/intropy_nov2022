def convert_cel_to_far(c):
    return c * 9 / 5 + 32

def convert_far_to_cel(f):
    return (f - 32) * 5 / 9

error = True
while error:
    try:
        f = float(input('Enter temperature in degree Fahrenheit: '))
    except ValueError:
        print('Invalid input')
        continue
    else:     
        c = convert_far_to_cel(f)
        print(f'{f} degrees Fahrenheit is {c:.2f} degrees Celsius')
        error = False

error = True
while error:
    try:
        c = float(input('Enter temperature in degree Celsius: '))
    except ValueError:
        print('Invalid input')
        continue
    else:    
        f = convert_cel_to_far(c)
        print(f'{c} degrees Celsius is {f:.2f} degrees Fahrenheit')
        error = False