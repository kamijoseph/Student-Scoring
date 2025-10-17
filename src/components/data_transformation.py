
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
