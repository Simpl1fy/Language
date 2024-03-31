from sklearn.feature_extraction.text import CountVectorizer
from sklearn.base import BaseEstimator, TransformerMixin
import re
import os
import numpy as np
import pickle
import sys
from src.logger import logging
from src.exception import CustomException
from sklearn.metrics import f1_score

class Remove(BaseEstimator, TransformerMixin):
    def fit(self, X):
        return self
    
    def transform(self, X):
        text_list = []
        for _,row in X.iterrows():
            text = row['Text']
            text = re.sub(r'[!@#$(),n%^&*?:;~`0-9]', ' ', text)
            text = text.replace("[", "")
            text = text.replace("]", "")
            text = text.lower()
            text_list.append(text)
        return text_list



class Vectorizer(BaseEstimator, TransformerMixin):
    def fit(self, X):
        return self
    def transform(self, X):
        cv = CountVectorizer()
        x = cv.fit_transform(X).toarray()
        return x
    

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        logging.info("Creating directories")
        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)
    
    except Exception as e:
        raise CustomException(e, sys)



def evaluate_models(X_train, y_train, X_test, y_test, models):
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]

            # Fitting the model
            model.fit(X_train, y_train)

            y_test_pred = model.predict(X_test)

            y_test_score = f1_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = y_test_score

        return report
    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)
