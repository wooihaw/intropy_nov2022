# Write a Python script to remove duplicates from a list.
alist = [99, 3, -1.2, 2.5, -1.2, -1.2, 5.75, 'xyz', 'a', 99, 'P', 'a', 2.5, 'xyz', 99, 'xyz', 99, 'xyz', 1, -1.2]
print(f'{alist=}')

print(list(set(alist)))

# Alternative solution
uniq_list = []
for i in alist:
    if i not in uniq_list:
        uniq_list.append(i)
print(uniq_list)

# Alternative solution 2
uniq_list2 = list({k: None for k in alist}.keys())
print(uniq_list2)