units = int(input("Enter the units of electricity consumed: "))

bill = 0

if units < 200:
    bill = 0
elif (units >= 200) and (units < 300):
    bill = (units - 200) * 1.2 + 100 * 1
elif (units >= 300) and (units < 400):
    bill = (units - 300) * 1.5 + 100 * 1 + 100 * 2
elif (units >= 400) and (units < 500):
    bill = (units - 400) * 2.5 + 100 * 1 + 100 * 2 + 100 * 3
else: 
    bill = (units - 500) * 8 + 100 * 1 + 100 * 2 + 100 * 3 + 100 * 4

print("Your electricity bill is:", bill)