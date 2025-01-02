class RangeExcludingPrimes:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def display_numbers(self):
        for num in range(self.start, self.end + 1):
            if not self.is_prime(num):
                print(num, end=" ")

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

range_obj = RangeExcludingPrimes(start, end)

range_obj.display_numbers()
