size = int(input("Enter the size of the pattern: "))
if size <= 0:
    print("Enter a positive number")

i = 0

while i < size:
    for j in range(size):
        print("*", end="")
    print("")
    i += 1