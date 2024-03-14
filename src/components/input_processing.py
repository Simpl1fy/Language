import re

def input_preprocessing(text):
    
    # Removing symbols and numeric values
    text = re.sub(r'[!@#$(),n%^&*?:;~`0-9]', ' ', text)

    # Removing square brackets
    text = re.sub(r'[[]]', ' ', text)

    # converting the text to lower
    text = text.lower()

    return text
    