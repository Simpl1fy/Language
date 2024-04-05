import os
import sys

from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

import pandas as pd

class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self, features):
        try:
            model_path = os.path.join('artifacts', 'model.pkl')
            input_processor_path = os.path.join('artifacts', 'preprocessor.pkl')
            target_processor_path = os.path.join('artifacts', 'target_processor.pkl')


            print('Before Loading')
            model = load_object(model_path)
            input_processor = load_object(input_processor_path)
            output_processor = load_object(target_processor_path)
            print('After Loading')

            logging.info(f'Shape of feature before changing is {features}')
            data_scaled = input_processor.transform(features).toarray()
            print(data_scaled)
            logging.info(f'Shape of scaled data is {data_scaled.shape}')


            pred = model.predict(data_scaled)
            language = output_processor.inverse_transform(pred)
            return language
        except Exception as e:
            raise CustomException

class CustomData:
    def __init__(self, text):
        self.text = text

    def get_data_as_dataframe(self):
        try:
            custom_dict = {
                "Text": [self.text]
            }
            return pd.DataFrame(custom_dict)
        except Exception as e:
            raise CustomException
