n = int(input("Enter the number of rows: "))

for i in range(n):
    for j in range(i + 1):
        print(chr(65 + j), end="")
    for j in range(i, n - 1):
        print(chr(65 + n - j - 1), end="")
    print()