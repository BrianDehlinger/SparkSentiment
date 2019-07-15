import re
from string import digits
import string
 
class DataCleaner:
    
    def __init__():
        pass


    @staticmethod
    def convert_to_lowercase(input_text):
        return input_text.lower()
    

    @staticmethod
    def remove_numbers(input_text):
        return re.sub(r'\d+', '', input_text)


    @staticmethod
    def remove_punctuation(input_text):
        return input_text.translate(str.maketrans('', '', string.punctuation))


    @staticmethod
    def remove_whitespace(input_text):
        stripped_text = input_text.strip()
        return ' '.join(stripped_text.split())
