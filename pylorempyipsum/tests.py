__author__ = 'rabbiabram@gmail.com'
import unittest
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


    def testGetString(self):
        string = None
        for i in self.lorem_object.get_string(0):
            string = i
        self.assertEqual('', string)
        new_string = ''
        for i in self.lorem_object.get_string(1):
            new_string = i
        self.assertNotEqual('', new_string)