__author__ = 'rabbiabram@gmail.com'
import  random
class PyLoremPyIpsum(object):
    raw_dict = ''
    words_list = []
    def __init__(self, dict):
        self.raw_dict = dict
        self.words_list = dict.split(' ')


    def get_word(self, max_words):
        if max_words <= 0:
            yield None
        for j in range(max_words):
            i =  random.randint(0, len(self.words_list) -1)
            yield self.words_list[i]


    def get_string(self,strings_count, max_words_in_string=10):
        if max_words_in_string <= 0 or strings_count <= 0:
            yield ''
        else:
            for j in range(strings_count):
                if max_words_in_string == 1:
                    string_length = 1
                else:
                    string_length = random.randint(1, max_words_in_string)
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

    def get_paragraphs(self, paragraphs_count, max_strings_in_paragraph=10, max_string_length=10):
        if max_strings_in_paragraph <= 0 or paragraphs_count <= 0:
            yield ''
        else:
            for j in range(paragraphs_count):
                if max_strings_in_paragraph == 1:
                    paragraph_length = max_strings_in_paragraph
                else:
                    paragraph_length = random.randint(1, max_strings_in_paragraph)
                paragraph = ''
                strings = 0

                for string in self.get_string(paragraph_length, max_string_length):
                    paragraph += string
                    strings += 1
                    if strings > 1 and  strings < paragraph_length:
                        paragraph += ' '
                yield paragraph

    def get_text(self, max_chars=500):
        i = 0
        text = ''
        failed = 0
        if (max_chars <= 0):
            return ''
        while i <= max_chars and failed < 3:
            sub_text = ''
            for t in self.get_paragraphs(1, random.randint(1, 10), random.randint(1, 15)):
                sub_text = t
            if len(text) + len(sub_text) + 1 <= max_chars:
                text += sub_text + '\n'
                i = len(text)
            else:
                failed += 1

        return text




