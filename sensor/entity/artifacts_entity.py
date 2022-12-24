from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    feature_store_file:str
    train_file_path:str
    test_file_path:str

@dataclass
class DataValidationArtifact:
    report_file_path:str

@dataclass
class DataTransformationArtifact:
    pass

@dataclass
class ModelTrainerArtifact:
    pass

@dataclass
class ModelEvaluatorArtifact:
    pass

@dataclass
class ModelPusherArtifact:
    pass