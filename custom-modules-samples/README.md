# Custom Module Gallery
## Custom Modules Tutorials
All the tutorials are now presented on Azure's Documentation at:
#### https://docs.microsoft.com/en-us/azure/machine-learning/tutorial-custom-module

## Contributing
Instructions on how to contribute to the custom modules

## Modules
In this directory, notebooks are provided to perform a quick demonstration of different algorithms such as Alternating Least Squares ([ALS](https://spark.apache.org/docs/latest/api/python/_modules/pyspark/ml/recommendation.html#ALS)) or Simple Algorithm for Recommendation ([SAR](https://github.com/Microsoft/Product-Recommendations/blob/master/doc/sar.md)). The notebooks show how to establish an end-to-end recommendation pipeline that consists of data preparation, model building, and model evaluation by using the utility functions ([reco_utils](../../reco_utils)).

| Sources | Dataset | Environment | Description |
| --- | --- | --- | --- | 
|**GitHub repo:** [sar_azureml](sar_movielens_with_azureml.ipynb)<br>**Notebook:** [sar_azureml](sar_movielens_with_azureml.ipynb)<br>**AML Studio:** [sar_azureml](sar_movielens_with_azureml.ipynb) | MovieLens | Python CPU | An example of how to utilize and evaluate SAR using the [Azure Machine Learning service](https://docs.microsoft.com/azure/machine-learning/service/overview-what-is-azure-ml) (AzureML). It takes the content of the [sar quickstart notebook](sar_movielens.ipynb) and demonstrates how to use the power of the cloud to manage data, switch to powerful GPU machines, and monitor runs while training a model.


[Image classification with MPI training](https://github.com/Azure/DesignerPrivatePreviewFeatures/blob/master/azureml-modules/samples/image-classification.ipynb) Demonstrates how to perform a distributed training using an mpi module.

[Anomaly Detector](https://github.com/microsoft/anomalydetector/tree/master/aml_module)