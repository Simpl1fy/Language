from sklearn.feature_extraction.text import CountVectorizer
from sklearn.base import BaseEstimator, TransformerMixin
import re
import os
import pickle
import sys
from src.logger import logging
from src.exception import CustomException

class Remove(BaseEstimator, TransformerMixin):
    def fit(self, X):
        return self
    
    def transform(self, X):
        text_list = []
        for text in X:
            text = re.sub(r'[!@#$(),n%^&*?:;~`0-9]]', ' ', text)
            text = re.sub(r'[[]]', ' ', text)
            text = text.lower()
            text_list.append(text)
        return text_list


class Vectorizer(BaseEstimator, TransformerMixin):
    def fit(self, X):
        return self
    
    def transform(self, X):
        cv = CountVectorizer()
        bow = cv.fit_transform(X).toarray()
        return bow
    

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, existOk=True)
        logging.info("Creating directories")
        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)
    
    except Exception as e:
        raise CustomException(e, sys)