import os
import sys

from src.exception import CustomException
from src.logger import logging
from src.utils import evaluate_models, save_object

from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score

class ModelTrainerConfig:
    model_file_path = os.path.join('artifacts', 'model,pkl')


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()


    def initiate_model_trainer(self, train_arr, test_arr):
        '''
            This function is responsible for training different models and finding the result
        '''
        try:
            logging.info("Initiated model trainer")
            logging.info('Converting the data into training and testing data')
            X_train, y_train, X_test, y_test = (
                train_arr[:, :-1],
                train_arr[:, -1],
                test_arr[:, :-1],
                test_arr[:, -1]
            )
            model = MultinomialNB()

            logging.info("Initialized models")
            
            model.fit(X_train, y_train)
            logging.info('Fitted the model with X_train and y_train')

            y_test_pred = model.predict(X_test)
            logging.info('Predicting on X_test')
        
            save_object(
                file_path=self.model_trainer_config.model_file_path,
                obj=model
            )
        
            logging.info('saved the model.pkl in artifacts folder')
        
            
        
            logging.info('calculating the f1_score')
            score = f1_score(y_test, y_test_pred, average='micro')
        
            logging.info('calculated the f1_score and returning it')
            return score
        except Exception as e:
            raise CustomException(e, sys)
