#%% Another Python Easter egg
import antigravity

#%% Check size of variables
a = 12345
print(a.__sizeof__())

#%% Binary and hexadecimal numbers
b = 567890
print(bin(b))
print(hex(b))

#%% Do not start with a digit when naming a variable
# 1star = 123  # This will cause a syntax error
_1star = 123  # instead we can start with an underscore

#%% Converting from string to integer
c = '123'
d = int(c)

#%% Cannot convert a string with alphabets to integer
e = 'abc'
f = int(e)

#%% Convert from a string with hex number to integer
g = 'abc'
h = int(g, base=16)
print(h)

#%% Arithmetic operators have different priority
print(2**2)
print(-2**2)
print((-2)**2)

#%% String slicing
i = 'apple pie'
print(i[2:-2])
print(i[-2:2])  # Not working as the default step is 1
print(i[-2:2:-1])  # works by changing the step to -1

#%% String is immutable
j = 'hello'
j[0] = 'c'  # error as string is immutable

#%% Change a character in a string by using string slicing and concatenation
k = 'c' + j[1:]
print(k)

#%% More string methods
m = 'Hello, World'
print(m.swapcase())
print(m.split())  # split using space by default
print(m.replace('l', ''))  # replace all 'l'
print(m.replace('l', '', 1))  # only replace the first 'l'

n = '   This is a string   \n'
print(n.encode())
print(n.strip().encode())
print(n.lstrip().encode())
print(n.rstrip().encode())

#%% Printing unicode
for i in range(50):
    print(chr(128522+i), end=' ')
# %%
