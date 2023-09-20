class Anagram:
    def __init__(self, word):
        self.word = word
    def match(self, anagram_list):
        # filtered_words = [possible_word for possible_word in anagram_list if sorted([letter for letter in possible_word]) == sorted(self.word)]
        # return(filtered_words)
        filtered_words = list()
        for possible_word in anagram_list:
            if sorted([letter for letter in possible_word]) == sorted(self.word):
                filtered_words.append(possible_word)
        return filtered_words


# listen = Anagram("listen")
# listen.match(['enlists', 'google', 'inlets', 'banana'])