# Write a Python script to find the frequency of occurance for each alphabet in a string.
astring = 'The quick brown fox jumps over the lazy dog.'

alist = [c.lower() for c in astring if c.isalpha()]

# Solution 1 using for loop
d1 = {}
for c in sorted(set(alist)):
    d1[c] = alist.count(c)
print(d1)

# Solution 2 using dictionary comprehension
d2 = {c: alist.count(c) for c in sorted(set(alist))}
print(d2)

for k in d2:
    print(f"{k} appears {d2[k]} {'times' if d2[k] > 1 else 'time'}")