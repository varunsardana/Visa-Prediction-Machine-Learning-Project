# Whenever we are exectuing the pipeline, example : data ingestion, data validation, data transformation, model trainer, model evaluation, model pusher
# the output from the pipeline will be stored in the artifact entity which is then sent to the next step in the pipeline. 
# example : data ingestion will send the output to data validation, data validation will send the output to data transformation and so on.
# basically the output from one step in the pipeline is the input to the next step in the pipeline.

from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    trained_file_path:str 
    test_file_path:str 


@dataclass
class DataValidationArtifact:
    validation_status:bool
    message: str
    drift_report_file_path: str



@dataclass
class DataTransformationArtifact:
    transformed_object_file_path:str 
    transformed_train_file_path:str
    transformed_test_file_path:str


@dataclass
class ClassificationMetricArtifact:
    f1_score:float
    precision_score:float
    recall_score:float



@dataclass
class ModelTrainerArtifact:
    trained_model_file_path:str 
    metric_artifact:ClassificationMetricArtifact
