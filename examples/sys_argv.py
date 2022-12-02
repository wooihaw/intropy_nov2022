import sys
print(f"{sys.argv=}")

print(f"You have entered {sys.argv[1]}")

for i in range(int(sys.argv[1])):
    print(i)
