import unittest
from datacleaner import *

class TestDataCleaner(unittest.TestCase):

    def test_convert_to_lowercase(self):
        self.assertEqual(DataCleaner.convert_to_lowercase('!@DooDlEBoBLoooOOvesYOU'),
                        '!@doodleboblooooovesyou')

    def test_remove_numbers(self):
        self.assertEqual(DataCleaner.remove_numbers('Box3 contains 3231 red a3nd2 two white balls, while Box B contains red balls only111111100000095'),
                                                    'Box contains  red and two white balls, while Box B contains red balls only')

    def test_remove_punctuation(self):
        self.assertEqual(DataCleaner.remove_punctuation('Box \#3 contains.! punctuation!!'),
                                                        'Box 3 contains punctuation') 

    def test_remove_whitespace(self):
        self.assertEqual(DataCleaner.remove_whitespace('   Box 3 contains    whitespace   '),
                                                       'Box 3 contains whitespace')


if __name__ == '__main__':
    unittest.main()


