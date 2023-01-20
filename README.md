# My data science projects

## NLP : named-entity recognition (NER) in hospital admission notes

Starting with a dataset containing approximately 500 hospital admission notes, we had to label data and build a NER (also called token-classification) model.
The goal is to augment the dataset, and train a model to extract as many of the following indicators for posology : the drug, the form, the dosage, the duration...
We relied on HuggingFace pre-trained LLM such as ```BertForTokenClassification``` and ```Camembert```
I was in charge of building the pipeline and training the models.

## QuantumBlack challenge

QuantumBlack's challenge was focused on two computer vision tasks : image classification, and then segmentation.
We also built a Streamlit app that encapsulates our CV model, and helps to visualize our business recommendations.
I was in charge of building the Streamlit app, and coming up with business recommendations.

## Optimizing IT infrastructure

It was a project on time series. For each server's CPU and memory, we had 500 data points corresponding to 500 days. A data point is actually three values: ```max_value```, ```avg_value``` and ```min_value```. The objective is to optimize the CPU and memory settings (number of core, mem size) to avoid both saturation and idleness.
I was in charge of data processing, more particularly analysing and validating periodicity within the time series. So that we could feed only relevant signals to our Prophet time-series model.

## Finding connected components in graph

We implemented an algo called CCF-iterate available here: https://www.cse.unr.edu/~hkardes/pdfs/ccf.pdf
We used Scala and Python, and wrote programs using RDD (Resilient Distributed Datasets) or Spark DataFrame and tested both methods on increasingly big graphs.
I was in charge of writing Python code.
