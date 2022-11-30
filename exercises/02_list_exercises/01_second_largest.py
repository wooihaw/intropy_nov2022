# Write a Python script to find the second largest value in a list.
alist = [12, 43, 57, 98, 83, -103, 256, -55, 185]
print(f'{alist=}')

print(f'Second largest number = {sorted(alist)[-2]}')

# Alternative solution
alist.sort()
print(f'Second largest number = {alist[-2]}')