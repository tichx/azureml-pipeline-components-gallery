# Text classification by convolutional neural network
![](https://contentmamluswest001.blob.core.windows.net/content/14b2744cf8d6418c87ffddc3f3127242/9502630827244d60a1214f250e3bbca7/f43e79f47d8a4219bf8613d271ea2c45/image?18739520845379465)

<img src="https://maxcdn.icons8.com/Share/icon/p1em/Logos/github1600.png" width=22px>[Clone pipeline]()
<img width=21px src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/1200px-Jupyter_logo.svg.png"> [Open with Notebook]()
<img src="https://ms-toolsai.gallerycdn.vsassets.io/extensions/ms-toolsai/vscode-ai/0.5.1/1556575437282/Microsoft.VisualStudio.Services.Icons.Default" width=18px> [Open in Azure Machine Learning Studio Designer]()
## Summary
This sample pipeline contains some components that implement with Text CNN for sentiment classification scenarios.

#### You will learn how to:

1. Register components from local code using component SDK.
2. Build pipeline with registered components and AzureML built-in components.

## Details

The goal of text classification is to assign some piece of text to one or more predefined classes or categories. The piece of text could be a document, news article, search query, email, tweet, support tickets, customer feedback, user product review etc. Applications of text classification include categorizing newspaper articles and news wire contents into topics, organizing web pages into hierarchical categories, filtering spam email, sentiment analysis, predicting user intent from search queries, routing support tickets, and analyzing customer feedback. As part of the Azure Machine Learning offering, Microsoft provides a template to help data scientists easily build and deploy a text classification solution. In this document, you will learn how to use and customize the template through a demo use case.

| Contributed by | Maintained by | Category | Tags | Last update | 
|---|---|---|---|---|
| Microsoft | @Microsoft Open Source | Tutorials |text-processing, text-classification, CNN| September 4, 2020

## Related components
| Component Folder               | Description                                                  |
| --- |--- |
| [textcnn-train](textcnn-train) | A module to perform training of a text classicification model from scratch using pytorch, used in [text classification pipeline](../text-classification.ipynb). |
| [textcnn-preprocess](textcnn-preprocess) | A module to preprocess input text before scoring in [text classification pipeline](../text-classification.ipynb). |
| [textcnn-score](textcnn-score) | A module to score text classicification model in [text classification pipeline](../text-classification.ipynb). |
