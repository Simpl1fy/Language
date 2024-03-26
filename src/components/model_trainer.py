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


    def initiate_model_trainer(self, input_train, target_train, input_test, target_test):
        '''
            This function is responsible for training different models and finding the result
        '''
        try:
            logging.info("Initiated model trainer")
            
            models = {
                "Multinomial Naive Bayes": MultinomialNB(),
                "Decision Tree Classifier": DecisionTreeClassifier()
            }

            logging.info("Initialized models")
            print(input_train.shape)
            print(target_train.shape)
            print(input_test.shape)
            print(target_test.shape)
        #     
        #     model_report:dict = evaluate_models(X_train=input_train, y_train=target_train, X_test=input_test, y_test=target_test, models=models)
        #
        #     logging.info("Called the evaluate_models function")
        #     best_model_score = max(sorted(model_report.values()))
        #     
        #     logging.info('got the best model score')
        #
        #     best_model_name = list(model_report.keys())[
        #         list(model_report.values().index(best_model_score))
        #     ]
        #     logging.info('got the best model name')
        #
        #     best_model = models[best_model_name]
        #     logging.info("created the best model object")
        #
        #     if best_model_score < 0.6:
        #         raise CustomException('No best model found!')
        #
        #     logging.info('best model found for training and testing datasets')
        #
        #     save_object(
        #         file_path=self.model_trainer_config.model_file_path,
        #         obj=best_model
        #     )
        #
        #     logging.info('saved the model.pkl in artifacts folder')
        #
        #     predicted = best_model.predict(input_test)
        #     logging.info('got a predicted value for test array')
        #
        #     logging.info('calculating the f1_score')
        #     score = f1_score(target_test, predicted)
        #
        #     logging.info('calculated the f1_score and returning it')
        #     return score
        except Exception as e:
            raise CustomException(e, sys)
