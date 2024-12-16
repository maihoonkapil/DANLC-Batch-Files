cha = input("Enter a character: ")

result = "Alphabet" if ('a' <= cha <= 'z' or 'A' <= cha <= 'Z') else "Number" if '0' <= cha <= '9' else "Special Character"

print(result)
