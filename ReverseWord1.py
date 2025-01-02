class ReverseWord:
    def __init__(self, word):
        self.word = word

    def reverse(self):
        reversed_word = ""
        
        for i in range(len(self.word) - 1, -1, -1):
            reversed_word += self.word[i]
        return reversed_word

word = input("Enter a word: ")

reverse_word_object = ReverseWord(word)

print("Reversed word:", reverse_word_object.reverse())
