import sys
import os

from src.logger import logging
from src.exception import CustomException
from src.utils import Remove, Vectorizer, save_object
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder


from dataclasses import dataclass

import numpy as np
import pandas as pd
import pickle

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')
    target_processor_obj_file_path = os.path.join('artifacts', 'target-processor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
       '''
           this function is responsible for data transformation 
       ''' 

       try:
           
        input_cols = ['Text']
        output_cols = ['Language']

        input_pipeline = Pipeline([
            ("remove", Remove()),
            ("vectorizer", Vectorizer())
        ])

        le = LabelEncoder()

        return (input_pipeline, le)

       except Exception as e:
           raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        '''
           this function is used for initiating the data transformation 
        '''
        try:
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)

            logging.info("Read of training and testing data complete")

            logging.info("Obtaining preprocessing object for input and output")

            input_processing, output_processing = self.get_data_transformer_object()

            

            input_feature_train_df = train_data.drop(columns=["Language"], axis=1)
            target_feature_train_df = train_data["Language"]

            input_feature_test_df = test_data.drop(columns=["Language"], axis=1)
            target_feature_test_df = test_data["Language"]

            logging.info("Applying the processor objects in training and testing dataset")

            input_feature_train_arr = input_processing.fit_transform(input_feature_train_df)
            input_feature_test_arr = input_processing.transform(input_feature_test_df)

            target_feature_train_arr = np.array(output_processing.fit_transform(target_feature_train_df))
            target_feature_test_arr = np.array(output_processing.transform(target_feature_test_df))

            train_arr = np.c_[input_feature_train_arr, target_feature_train_arr]
            test_arr = np.c_[input_feature_test_arr, target_feature_test_arr]

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=input_processing
            )             

            save_object(
                file_path=self.data_transformation_config.target_processor_obj_file_path,
                obj = output_processing
            )   

            return (
                train_arr,
                test_arr
            )

        except Exception as e:
            raise CustomException(e, sys)