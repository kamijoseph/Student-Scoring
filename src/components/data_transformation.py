
# data transformation
import os
import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocess_obj_path = os.path.join(
        "artifacts",
        "preprocessor.pkl"
    )

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_transformer(self):
        try:
            numerical_features = [
                "writing_score",
                "reading_score"
            ]

            categorical_features = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]

            num_pipeline = Pipeline(
                steps = [
                    ("Imputer", SimpleImputer(strategy = "median")),
                    ("scaler", StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy = "most_frequent")),
                    ("one_hot_necoder", OneHotEncoder()),
                    ("scaler", StandardScaler())
                ]
            )

            logging.info("numerical features scaling complete.................")
            logging.info("categorical features encoding complete..............")

            preprocesser = ColumnTransformer([
                ("num_pipeline", num_pipeline, numerical_features),
                ("cat_pipeline", cat_pipeline, categorical_features)
            ])

            return preprocesser

        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_transformation(self, train_path, test_path):
        try:
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)

            logging.info("reading training and testing data completed ..........")
            logging.info("obtaining preprocessing object .......")

            preprocess_obj = self.get_transformer()

            X_train, y_train = train_data.drop("math_Score", axis=1), train_data["math_score"]
            X_test, y_test = test_data.drop("math_score", axis=1), test_data["math_score"]

            logging.inf0("applying preprocessor on train and test datasets.............")

            X_train_transformed = preprocess_obj.fit_transform(X_train)
            X_test_transformed = preprocess_obj.transform(X_test)

            train_array = np.c_[
                X_train, np.array(y_train)
            ]
            test_array = np.c_[
                X_test, np.array(y_test)
            ]

            logging.info('saved preprocessing object...............')

            save_object(
                file_path = self.data_transformation_config.preprocess_obj_path,
                obj = preprocess_obj
            )

            return (
                train_array,
                test_array,
                self.data_transformation_config.preprocess_obj_path
            )

        except:
            pass
