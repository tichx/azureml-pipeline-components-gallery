# Text classification by convolutional neural network
![](https://contentmamluswest001.blob.core.windows.net/content/14b2744cf8d6418c87ffddc3f3127242/9502630827244d60a1214f250e3bbca7/f43e79f47d8a4219bf8613d271ea2c45/image?18739520845379465)

<img src="https://maxcdn.icons8.com/Share/icon/p1em/Logos/github1600.png" width=22px>[See Source Code]()
<img width=21px src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/1200px-Jupyter_logo.svg.png"> [Open with Notebook]()
<img src="https://ms-toolsai.gallerycdn.vsassets.io/extensions/ms-toolsai/vscode-ai/0.5.1/1556575437282/Microsoft.VisualStudio.Services.Icons.Default" width=18px> [Run in Azure Machine Learning Studio Designer]()
## Summary
This sample pipeline contains some components that implement with Text CNN for sentiment classification scenarios.

#### You will learn how to:

1. Register components from local code using component SDK.
2. Build pipeline with registered components and AzureML built-in components.

## Details

The goal of text classification is to assign some piece of text to one or more predefined classes or categories. The piece of text could be a document, news article, search query, email, tweet, support tickets, customer feedback, user product review etc. Applications of text classification include categorizing newspaper articles and news wire contents into topics, organizing web pages into hierarchical categories, filtering spam email, sentiment analysis, predicting user intent from search queries, routing support tickets, and analyzing customer feedback. As part of the Azure Machine Learning offering, Microsoft provides a template to help data scientists easily build and deploy a text classification solution. In this document, you will learn how to use and customize the template through a demo use case.

| Contributed by | Maintained by | Category | Tags | Last update | 
|---|---|---|---|---|
| Microsoft | @Microsoft Open Source | Tutorials |text-processing, text-classification, CNN| September 4, 2020 |

## Industry

### Online Streaming - Netflix
<img width=400px src="https://fm.cnbc.com/applications/cnbc.com/resources/img/editorial/2017/05/04/104449321-netflix-offline-1.720x405.jpg?v=1493920615"><br>
Netflix has 500M users gloablly, and 132 million users streaming content on daily basis. At Netflix, recommending best selection of videos based on each individual's preference is critical to its product success. Using text classification of IMDB movie database, Netflix leverages machine learning to classify a large set of genres, categories, and combine them to form quirkey new area that tailored for each individual's taste.

### Banking - Bank of America
<img width=400px src="https://th.bing.com/th/id/OIP.mmyufsLQuNmq8HkRaUWJ3wHaD4?pid=Api&rs=1">
Traditionally, customers of Bank of America reported that 60% of the expense cateogory appeared on their monthly balance statement are inaccuarate. Customers would correct a category every time they see an error. With these historical correction data retained as training data set, Bank of America uses ML text classification to continously improve predictions for accurate expense cateogrization.


## Related components
| Source code               | Description                                                  |
| --- |--- |
| [textcnn-train](textcnn-train) | A module to perform training of a text classicification model from scratch using pytorch, used in [text classification pipeline](../text-classification.ipynb). |
| [textcnn-preprocess](textcnn-preprocess) | A module to preprocess input text before scoring in [text classification pipeline](https://github.com/tichx/azureml-pipeline-components-gallery/blob/master/Pipelines/textcnn-pipeline/text-classification.ipynb). |
| [textcnn-score](textcnn-score) | A module to score text classicification model in [text classification pipeline](#). |
