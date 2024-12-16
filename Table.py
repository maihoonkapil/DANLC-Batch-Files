start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

for i in range(start, end + 1):

    print(f"Multiplication table of {i}:")
    for j in range(1, 11):
        
        product = i * j
        
        print(f"{i} x {j} = {product}")

    print()