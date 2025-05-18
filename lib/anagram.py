# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        sorted_word = "".join(sorted([letter for letter in self.word]))
        matches = []
        for word in word_list:
            if "".join(sorted([letter for letter in word])) == sorted_word:
                matches.append(word)
        return matches

listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))
