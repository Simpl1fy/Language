import sys
import os

from src.logger import logging
from src.exception import CustomException
from src.utils import Remove, Vectorizer, save_object
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer


from dataclasses import dataclass

import numpy as np
import pandas as pd
import pickle

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
       '''
           this function is responsible for data transformation 
       ''' 

       try:
        input_cols = ['Text']

        input_pipeline = Pipeline([
            ("remove", Remove()),
            ("vectorizer", Vectorizer())
        ])

        preprocessor = ColumnTransformer(
            [
                ("input-pipeline", input_pipeline, input_cols)
            ]
        )

        le = LabelEncoder()

        return (preprocessor, le)

       except Exception as e:
           raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        '''
           this function is used for initiating the data transformation 
        '''
        try:
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)

            target_column_name = "Language"

            logging.info("Read of training and testing data complete")

            logging.info("Obtaining preprocessing object for input and output")

            input_processing, label_encoder = self.get_data_transformer_object()

            print(train_data.head())
            print(test_data.head())

            input_feature_train_df = train_data.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_data[target_column_name]

            input_feature_test_df = test_data.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_data[target_column_name]

            logging.info("Applying the processor objects in training and testing dataset")

            input_feature_train_arr = input_processing.fit_transform(input_feature_train_df)
            input_feature_test_arr = input_processing.transform(input_feature_test_df)

            target_feature_train_arr = np.array(label_encoder.fit_transform(target_feature_train_df))
            target_feature_test_arr = np.array(label_encoder.transform(target_feature_test_df))

            train_arr = np.c_[input_feature_train_arr, target_feature_train_arr]
            test_arr = np.c_[input_feature_test_arr, target_feature_test_arr]

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=input_processing
            )             

            return (
                train_arr,
                test_arr
            )

        except Exception as e:
            raise CustomException(e, sys)
