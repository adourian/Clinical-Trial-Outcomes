# Clinical-Trial-Outcomes

## Project Overview

Drug development is a lengthy, expensive, and high-risk process, typically taking 12 to 15 years and costing between 1 and 3 billion USD, with a success rate as low as 7.9% from Phase I to market. This project addresses the need for better decision-making tools in the pharmaceutical industry by predicting the outcomes of clinical trials using a multi-modal neural network architecture. By leveraging machine learning techniques, we provide a tool to estimate the chances of success for clinical trials, potentially reducing the high costs and risks associated with drug development. The main file for this project is clinical_trial_outcomes.ipynb.

![image](https://github.com/user-attachments/assets/a1d6b8c0-e531-47e1-b56a-b01f2f809e4c)
> *Figure 1:* Overview of process



## Data

The dataset used in this project is derived from the official U.S. Food and Drug Administration (FDA) database at clinicaltrials.gov. The outcome labeling was performed by Fu et al. ([1](https://arxiv.org/abs/2102.04252)) and further refined by IQVIA, resulting in a benchmark dataset. We enhanced this dataset by incorporating brief trial descriptions retrieved from clinicaltrials.gov using the unique NCTID identifiers.

Main features include:

- Drug SMILES data
- Number of drugs involved in trial
- Disease names
- Protocol descriptions (Inclusion/exclusion criteria, brief text description of trial)
- Clinical trial phases

The clinical trial phases are one-hot encoded. The text and SMILES features are transformed into semantically rich embeddings. Several embedding/language models were tested. 

![PCA_diseases](https://github.com/user-attachments/assets/560721c0-92cf-4339-b0bb-b369426add72)

> *Figure 2:* PCA analysis of embeddings for diseases. Analysis carried out in Diseases.ipynb. Similar diseases are grouped close by together, suggesting that the embedding models effectively capture biologically relevant information about the diseases.



## Modelling

To leverage the feature-rich, multi-modal nature of the data, we employed a multi-modal neural network architecture. Each data type (excluding numerical data such as phases and number of drugs) is processed independently through its own neural network. This approach generates a learned representation for each data type. These learned representations are then concatenated (along with the numerical data) and fed into a final neural network, which outputs the probability of trial success.

The rationale behind this architecture is to allow the model to discover relevant features specific to each data type more effectively. By processing each modality separately before combining them, the model can capture nuanced patterns within each data type. This approach enhances the model's ability to assess the probability of trial success by considering the unique contributions of each data modality.

## Performance

Our model's performance is comparable to the HINT benchmark:

| Phase | F1 Score |
|-------|----------|
| 1     | 0.70     |
| 2     | 0.64     |
| 3     | 0.85     |

## Installation and Dependencies

```python
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import pickle
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score, confusion_matrix, precision_recall_curve, auc
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import xgboost as xgb
import optuna
from sklearn.dummy import DummyClassifier
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted
