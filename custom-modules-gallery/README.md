# Custom Modules Gallery
## Tutorials
All the tutorials are now presented on Azure's Documentation at:
#### https://docs.microsoft.com/en-us/azure/machine-learning/tutorial-custom-module

## Contributing
Instructions on how to contribute to the custom modules

## Modules
In this directory, you will find a host of modules to be used as a in Azure Machine Learning Studio, contibuted by Microsoft and open community. Custom modules expand the capabilities of Azure Machine Learning Studio to allow you to develop even more advanced predictive analytics solutions. notebooks are provided to perform a quick demonstration of different algorithms such as Simple Algorithm for Recommendation ([SAR](https://github.com/Microsoft/Product-Recommendations/blob/master/doc/sar.md)). 

| GitHub | Notebook | AML Studio | Type | Description |
| --- | --- | --- | --- | --- |
|![](https://az712634.vo.msecnd.net/content/14b2744cf8d6418c87ffddc3f3127242/9502630827244d60a1214f250e3bbca7/ba9e9cfd25a74690aec5983cb7cbf9ad/7662044d475d416ab30dc12fe41692e5/image?5131359820425363)[Simple Algorithm for Recommendation (SAR)*](https://github.com/microsoft/recommenders/tree/master/examples/00_quick_start) | [sar_azureml.ipynb](https://github.com/microsoft/recommenders/blob/master/examples/00_quick_start/sar_movieratings_with_azureml_designer.ipynb)<br> | [sar_azureml](sar_movielens_with_azureml.ipynb) | Algorithm | An example of how to utilize and evaluate SAR using the [Azure Machine Learning service](https://docs.microsoft.com/azure/machine-learning/service/overview-what-is-azure-ml) (AzureML). It takes the content of the [sar quickstart notebook](sar_movielens.ipynb) and demonstrates how to use the power of the cloud to manage data, switch to powerful GPU machines, and monitor runs while training a model.
|![](https://az712634.vo.msecnd.net/content/14b2744cf8d6418c87ffddc3f3127242/9502630827244d60a1214f250e3bbca7/df36abc90cf742abb7ed0375788afd84/e9a8067dbd0c4335b9a830530d536184/image?9379528722646815)[Anomaly Detection Module](https://github.com/microsoft/anomalydetector/tree/master/aml_module#spectral-residual-anomaly-detection-module)| N/A | N/A| Services | Anomaly detection aims to discover unexpected events or rare items in data. It is designed to be accurate, efficient and general, using Spectral Residual (SR) and Convolutional Neural Network (CNN).|

## Reference papers
- Ren, Hansheng et al. “Time-Series Anomaly Detection Service at Microsoft.” Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining (2019): n. pag. Crossref. Web.

[Image classification with MPI training](https://github.com/Azure/DesignerPrivatePreviewFeatures/blob/master/azureml-modules/samples/image-classification.ipynb) Demonstrates how to perform a distributed training using an mpi module.
