amount = int(input("Enter the amount: "))

count_2000 = 0
count_500 = 0
count_200 = 0
count_100 = 0
count_50 = 0

if amount >= 2000:
    count_2000 = amount // 2000
    amount = amount - (count_2000 * 2000)

if amount >= 500:
    count_500 = amount // 500
    amount = amount - (count_500 * 500)

if amount >= 200:
    count_200 = amount // 200
    amount = amount - (count_200 * 200)

if amount >= 100:
    count_100 = amount // 100
    amount = amount - (count_100 * 100)

if amount >= 50:
    count_50 = amount // 50
    amount = amount - (count_50 * 50)


print("Denominations:")
if count_2000 > 0:
    print("2000:", count_2000)
if count_500 > 0:
    print("500:", count_500)
if count_200 > 0:
    print("200:", count_200)
if count_100 > 0:
    print("100:", count_100)
if count_50 > 0:
    print("50:", count_50)