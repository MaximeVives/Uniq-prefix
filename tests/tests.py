import unittest
from Word import Word


class TestStringMethods(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestStringMethods, self).__init__(*args, **kwargs)
        self.input_1 = ""
        self.input_2 = ""
        self.word = None

    def test_1_length(self):
        self.input_1 = "5"
        self.input_2 = "find the shortest unique prefix"
        self.word = Word(self.input_1, self.input_2)
        self.assertEqual(self.word.uniq_prefix(), ['f', 't', 's', 'u', 'p'])

    def test_4_length(self):
        self.input_1 = "4"
        self.input_2 = "pretend present previous prefix"
        self.word = Word(self.input_1, self.input_2)
        self.assertEqual(self.word.uniq_prefix(), ["pret", "pres", "prev", "pref"])

    def test_weekly(self):
        self.input_1 = "6"
        self.input_2 = "alphabet book carpet cadmium cadeau alpine"
        self.word = Word(self.input_1, self.input_2)
        self.assertEqual(self.word.uniq_prefix(), ["alph", "b", "car", "cadm", "cade", "alpi"])

    def test_ascending(self):
        self.input_1 = "3"
        self.input_2 = "a aa aaa"
        self.word = Word(self.input_1, self.input_2)
        self.assertEqual(self.word.uniq_prefix(), ["a", "aa", "aaa"])

    def test_descending(self):
        self.input_1 = "3"
        self.input_2 = "aaa aa a"
        self.word = Word(self.input_1, self.input_2)
        self.assertEqual(self.word.uniq_prefix(), ["aaa", "aa", "a"])