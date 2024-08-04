# Clinical-Trial-Outcomes

## Project Overview

Drug development is a lengthy, expensive, and high-risk process, typically taking 12 to 15 years and costing between 1 and 3 billion USD, with a success rate as low as 7.9% from Phase I to market. This project addresses the need for better decision-making tools in the pharmaceutical industry by predicting the outcomes of clinical trials using a multi-modal neural network architecture. By leveraging machine learning techniques, we provide a tool to estimate the chances of success for clinical trials, potentially reducing the high costs and risks associated with drug development. The main file for this project is clinical_trial_outcomes.ipynb.

![image](https://github.com/user-attachments/assets/a1d6b8c0-e531-47e1-b56a-b01f2f809e4c)

## Data

The dataset used in this project is derived from the official U.S. Food and Drug Administration (FDA) database at clinicaltrials.gov. The outcome labeling was performed by Fu et al. in their work on the HINT model [Link](https://arxiv.org/abs/2102.04252) and further refined by IQVIA, resulting in a benchmark dataset. We enhanced this dataset by incorporating brief trial descriptions retrieved from clinicaltrials.gov using the unique NCTID identifiers.

Main features include:

- Drug SMILES data
- Number of drugs involved in trial
- Disease names
- Protocol descriptions (Inclusion/exclusion criteria, brief text description of trial)
- Clinical trial phases

The clinical trial phases are one-hot encoded. The text and SMILES features are transformed into semantically rich embeddings. Several embedding/language models were tested. 

![PCA_diseases](https://github.com/user-attachments/assets/560721c0-92cf-4339-b0bb-b369426add72)


## Data

- **Source**: clinicaltrials.gov, compiled by Fu et al. (GitHub link to be added)
- **Preprocessing**: 
  - Data cleaning (removing NaNs)
  - Separating inclusion/exclusion criteria
  - One-hot encoding of phases
  - Creating a 'number of drugs' feature
  - Generating embeddings for textual features

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
