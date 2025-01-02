class StringAnalyzer:
    def __init__(self, input_string):
        self.input_string = input_string

    def count_digits_and_letters(self):
        digits_count = 0
        letters_count = 0

        for char in self.input_string:
            
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                letters_count += 1
            
            elif '0' <= char <= '9':
                digits_count += 1

        return digits_count, letters_count

input_string = input("Enter a string: ")

analyzer = StringAnalyzer(input_string)

digits, letters = analyzer.count_digits_and_letters()
print(f"Number of digits: {digits}")
print(f"Number of letters: {letters}")

