__author__ = 'rabbiabram@gmail.com'
import  random
class PyLoremPyIpsum(object):
    raw_dict = ''
    words_list = []
    def __init__(self, dict):
        self.raw_dict = dict
        self.words_list = dict.split(' ')


    def get_word(self, max_words):
        for j in range(max_words):
            i = random.randint(0, len(self.words_list) -1)
            yield self.words_list[i]


    def get_string(self,max_words_in_string=10):
        if max_words_in_string <= 0:
            yield ''
        string_length = random.randint(0, max_words_in_string)
        words = 0
        string = ''
        for word in self.get_word(string_length):
            string += word
            words += 1
            if words > 0 and words < string_length:
                string += ' '
            elif words == string_length:
                string += '.'
        yield string

