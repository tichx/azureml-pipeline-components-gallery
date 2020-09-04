import logging
import logging.handlers
from textclscnn.preprocessor import DataPreprocessor
from textclscnn.utils.args_util import preprocess_args
from textclscnn.utils.io_util import read_as_dataframe
import pandas as pd
import os


root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
root_logger.addHandler(logging.StreamHandler())


if __name__ == '__main__':
    args = preprocess_args()
    processor = DataPreprocessor(args.input_vocab, args.text_column)
    df = read_as_dataframe(args.input_data)
    output_df = processor.process(df)

    if not os.path.isdir(args.output_data):
        os.makedirs(args.output_data)
    output_df.to_parquet(f"{args.output_data}/word_id.parquet")
