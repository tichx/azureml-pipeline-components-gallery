from textclscnn.predictor import Predictor
from textclscnn.utils.args_util import predict_args
from textclscnn.utils.io_util import read_as_dataframe
import pandas as pd
import logging
import os


root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
root_logger.addHandler(logging.StreamHandler())


if __name__ == '__main__':
    args = predict_args()
    predictor = Predictor(args.trained_model)
    df = read_as_dataframe(args.predict_path)
    result_df = predictor.predict(df)

    if not os.path.isdir(args.predict_result_path):
        os.makedirs(args.predict_result_path)
    result_df.to_csv(f"{args.predict_result_path}/output.csv", index=False)
    
    predictor.evaluation(predictor.config, df, result_df, args.predict_result_path)
