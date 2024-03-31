import sys
import os

from src.logger import logging
from src.exception import CustomException
from src.utils import Remove, Vectorizer, save_object
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split


from dataclasses import dataclass

import numpy as np
import pandas as pd
import pickle

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')
    target_processor_obj_file_path = os.path.join('artifacts', 'target_processor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_data_transformation_object(self):
        input_pipeline = Pipeline([
               ("remover", Remove()),
               ("vectorizer", Vectorizer())
        ])
        le = LabelEncoder()
        return (
            input_pipeline,
            le
        )


    def initiate_data_transformation(self, raw_data_path):
        '''
           this function is used for initiating the data transformation 
        '''
        try:
            raw_data = pd.read_csv(raw_data_path)
            logging.info("Reading the data as csv from the function parameters")

            target_column_name = "Language"
            logging.info("Read of training and testing data complete")

            logging.info("Obtaining preprocessing object for input and output")
            input, output = self.get_data_transformation_object()


            X = raw_data.drop([target_column_name], axis=1)
            y = raw_data[target_column_name]
            logging.info('Divided the data into input and output df')


            logging.info("Applying the preprocessor")

            X_vectorized = input.fit_transform(X)
            y_encoder = output.fit_transform(y)

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=input
            )             

            save_object(
                file_path = self.data_transformation_config.target_processor_obj_file_path,
                obj=output
            )

            data = np.c_[X_vectorized, np.array(y_encoder)]
            logging.info('Dividing the data into train and test array')
            train_data, test_data = train_test_split(data, test_size=0.2)
            logging.info('Division Completed')
            logging.info('Returning the train array and testing array')
            return (
                train_data,
                test_data
            )

        except Exception as e:
            raise CustomException(e, sys)
