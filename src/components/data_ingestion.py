import sys
import os

from src.logger import logging
from src.exception import CustomException

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    raw_data_path:str = os.path.join('artifacts', 'data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    
    def initiate_data_ingestion(self):
        logging.info("Initiating Data Ingestion")
        try:
            df = pd.read_csv('notebook/data/Language Detection.csv')
            logging.info("Read the csv file as a dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            logging.info("Created a directory with the name artifacts")

            df.to_csv(self.ingestion_config.raw_data_path, header=True, index=False)

            logging.info("ingestion of data is completed")

            return(
                self.ingestion_config.raw_data_path
            )


        except Exception as e:
            raise CustomException(e, sys)
        
    
# Checking if data ingestion works
if __name__ == "__main__":
    obj = DataIngestion()
    raw_data = obj.initiate_data_ingestion()
    
    data_transformation = DataTransformation()
    train_arr, test_arr = data_transformation.initiate_data_transformation(raw_data)
    # print(train_arr.shape)
    # print(test_arr.shape)

    model_trainer = ModelTrainer()
    f1_score = model_trainer.initiate_model_trainer(train_arr, test_arr)
    print(f1_score)
