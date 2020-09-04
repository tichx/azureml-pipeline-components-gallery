import logging
import logging.handlers
import os
import pickle
from azureml.data.azure_storage_datastore import AzureFileDatastore, AzureBlobDatastore
from textclscnn.trainer import Trainer
from textclscnn.utils.args_util import train_args


root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
root_logger.addHandler(logging.StreamHandler())


if __name__ == '__main__':
    args = train_args()
    if not os.path.isdir(args.trained_model):
        os.makedirs(args.trained_model)

    trainer = Trainer(args)
    with open(os.path.join(args.trained_model, 'config.pkl'), 'wb') as f:
        pickle.dump(args, f, protocol=pickle.HIGHEST_PROTOCOL)

    try:
        trainer.train()
    except KeyboardInterrupt:
        logging.warning('\nExiting from training early')
