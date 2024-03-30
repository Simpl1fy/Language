import sys
import os

from src.logger import logging
from src.exception import CustomException
from src.utils import Remove, Vectorizer, save_object
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer


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


    def initiate_data_transformation(self, train_path, test_path):
        '''
           this function is used for initiating the data transformation 
        '''
        try:
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)
            logging.info("Reading the data as csv from the function parameters")

            target_column_name = "Language"
            logging.info("Read of training and testing data complete")

            logging.info("Obtaining preprocessing object for input and output")
            input, output = self.get_data_transformation_object()


            input_feature_train_df = train_data.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_data[target_column_name]

            input_feature_test_df = test_data.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_data[target_column_name]
            
            logging.info('Divided the data into X_train, y_train, X_test, y_test')


            logging.info("Applying the processor objects in training and testing dataset")

            input_feature_train_arr = input.fit_transform(input_feature_train_df)
            input_feature_test_arr = input.transform(input_feature_test_df)
            print("Shape of input train array = {}".format(input_feature_train_arr.shape))
            print("Shape of input test array = {}".format(input_feature_test_arr.shape))

            target_feature_train_arr = np.array(output.fit_transform(target_feature_train_df))
            target_feature_test_arr = np.array(output.transform(target_feature_test_df))

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=input
            )             

            save_object(
                file_path = self.data_transformation_config.target_processor_obj_file_path,
                obj=output
            )

            return (
                input_feature_train_arr,
                target_feature_train_arr,
                input_feature_test_arr,
                target_feature_test_arr
            )

        except Exception as e:
            raise CustomException(e, sys)
