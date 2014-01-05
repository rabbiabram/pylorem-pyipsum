__author__ = 'rabbiabram@gmail.com'
import unittest, random
from pylorempyipsum import PyLoremPyIpsum

class TestPyLoremPyIpsum(unittest.TestCase):

    def setUp(self):
        self.dict_string = 'ala olo aha oho ath ame aro'
        self.lorem_object = PyLoremPyIpsum.PyLoremPyIpsum(self.dict_string)

    def testGetWord(self):
        word = ''
        for i in self.lorem_object.get_word(0):
            word = i
        self.assertIsNone(word)
        new_word = ''
        for i in self.lorem_object.get_word(1):
            new_word = i
        self.assertIsNotNone(new_word)
        words_count = random.randint(0, 255)
        words = []
        for i in self.lorem_object.get_word(words_count):
            words.append(i)
        self.assertEqual(words_count, len(words))

    def testGetString(self):
        string = None
        for i in self.lorem_object.get_string(0):
            string = i
        self.assertEqual('', string)
        new_string = ''
        for i in self.lorem_object.get_string(1):
            new_string = i
        self.assertNotEqual('', new_string)
        string_count = random.randint(0, 255)
        strings = []
        for i in self.lorem_object.get_string(string_count):
            strings.append(i)
        self.assertEqual(string_count, len(strings))

    def testGetParagraph(self):
        paragraph = None
        for i in self.lorem_object.get_paragraphs(0):
            paragraph = i
        self.assertEqual('', paragraph)

        new_paragraph = ''
        for p in self.lorem_object.get_paragraphs(1):
            new_paragraph = p
        self.assertNotEqual('', new_paragraph)
        paragraphs_count = random.randint(0, 10)
        paragraphs = []
        for p in self.lorem_object.get_paragraphs(paragraphs_count):
            paragraphs.append(p)
        self.assertEqual(paragraphs_count, len(paragraphs))

    def testGetText(self):
        empty_text = self.lorem_object.get_text(0)
        self.assertEqual(0, len(empty_text))

        typical_text = self.lorem_object.get_text()
        self.assertGreater(500, len(typical_text))

        greater_text = self.lorem_object.get_text(1000)
        self.assertLess(500, len(greater_text))

        small_text = self.lorem_object.get_text(100)
        self.assertGreater(500, len(small_text))