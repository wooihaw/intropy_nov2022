# Write a Python script to ask for a string, 
# and print the string with uppercase letters in lowercase
# and vice-versa. Include punction and other non-cased 
# characters unchanged.
# E.g.
# Enter a string: Arg!
# aRG!
# Enter a string: PyThoN
# pYtHOn

astring = input("Enter a string: ")
print(astring.swapcase())