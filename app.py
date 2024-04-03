import sys

from sign_language.logger import logging
from sign_language.exception import SignException
from sign_language.pipeline.train_pipeline import TrainPipeline

if __name__ == '__main__':
    obj = TrainPipeline()
    obj.run_pipeline()
    print('Executed successfully')
