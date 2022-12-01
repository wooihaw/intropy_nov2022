#%% Empty sequences are treated as False, otherwise they are treated as True
alist = []
print('Not empty list' if alist else 'Empty list')

alist.append(0)
print('Not empty list' if alist else 'Empty list')

#%% Iterate through more than one lists in a for loop
fruits = ['apple', 'orange', 'pear']
prices = [1.5, 2.5, 4]

for i in range(len(fruits)):
    print(f'{fruits[i]}: {prices[i]}')

# Alternatively, zip() can be used to combined the lists
for i, j in zip(fruits, prices):
    print(f'{i}: {j}')

# Using enumerate to add index to each item
for i, j in enumerate(fruits, start=1):
    print(f'{i}. {j.capitalize()}')

# Using pass or ellipsis as placeholder
for i in range(5):
    pass

for i in range(5):
    ...

#%% List comprehension 1
names = ['ali', 'bala', 'chen', 'david']
cap_names_1 = []

for n in names:
    cap_names_1.append(n.capitalize())
print(cap_names_1)

# Using list comprehension
cap_names_2 = [n.capitalize() for n in names]
print(cap_names_2)


# %% List comprehension 2
alist = ['Java', 'Rust', 'Python', 'Swift', 'Go']

filtered_list1 = []
for i in alist:
    if 'o' in i:
        filtered_list1.append(i)
print(filtered_list1)

# Using list comprehension
filtered_list2 = [i for i in alist if 'o' in i]
print(filtered_list2)

#%% List comprehension 3
s = 'Testing 123! Are you there?'
t1 = []
for c in s:
    t1.append(c if c.isalpha() else ' ')
print(''.join(t1))

# Using list comprehension
t2 = [c if c.isalpha() else ' ' for c in s]
print(''.join(t2))

#%% Idctionary comprehension
fruits = ['apple', 'orange', 'pear']
prices = [1.5, 2.5, 4]
inventory = dict(zip(fruits, prices))
print(inventory)

# Dictionary with 10% discount applied
discounted_inventory = {k: 0.9*inventory[k] for k in inventory}
print(discounted_inventory)

#%% Generator expression
squares1 = [i**2 for i in range(1, 101)]
print(squares1.__sizeof__())  # squares1 is a list

squares2 = (i**2 for i in range(1, 101))
print(squares2.__sizeof__())  # squares2 is a generator


