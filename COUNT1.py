class Number:
    def __init__(self, num):
        self.num = num

    def count_digits(self):
        count = 0
        num = self.num
        
        if num < 0:
            num = -num
        while num > 0:
            count += 1
            num //= 10  
        return count

num = int(input("Enter a number: "))

number = Number(num)

print("Total number of digits:", number.count_digits())
