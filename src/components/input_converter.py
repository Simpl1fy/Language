# Importing necessary libraries

from sklearn.feature_extraction.text import CountVectorizer

def bag_of_words(text):
    cv = CountVectorizer()
    text_vectorized = cv.fit_transform(text).toarray()
    return text_vectorized