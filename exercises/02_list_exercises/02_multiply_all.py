# Write a Python script to multiply all the items in a list.
alist = [12, 43, 57, 98, 83, -103, 256, -1]
print(f'{alist=}')

sum_of_list = 0
for i in alist:
    sum_of_list += i

print(sum_of_list)

product_of_list = 1
for i in alist:
    product_of_list *= i

print(product_of_list)