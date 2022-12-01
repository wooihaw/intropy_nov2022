# Write a Python script to find common items between two lists.
alist = [99, 'P', 1, 'xyz', 'a', 2.5]
blist = ['xyz', 2.5, 2.5, 3, 99, 99, 2.5, 'xyz', -1.2, 99]

print(set(alist) & set(blist))

# Alternative
print(set(alist).intersection(set(blist)))

# Alternative solution using list
clist = []
for i in alist:
    if i in blist:
        clist.append(i)
print(clist)

# Alternative solution using list comprehension
dlist = [i for i in alist if i in blist]
print(dlist)