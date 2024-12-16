note = int(input("Enter the currency note for deposit: "))

if (note == 2000) or (note == 500) or (note == 200) or (note == 100) or (note == 50):
    print("Valid currency note for deposit.")
else:
    print("Invalid currency note. Please provide a valid note.")