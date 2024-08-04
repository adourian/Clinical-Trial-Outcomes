# Clinical-Trial-Outcomes

## Project Overview

This project aims to predict the outcomes of clinical trials using a multi-modal neural network architecture. By leveraging machine learning techniques, we provide a tool to estimate the chances of success for clinical trials, potentially reducing the high costs and risks associated with drug development.

## Background

Drug development is a lengthy, expensive, and high-risk process, typically taking 12 to 15 years and costing between 1 and 3 billion USD, with a success rate as low as 7.9% from Phase I to market. This project addresses the need for better decision-making tools in the pharmaceutical industry by predicting clinical trial outcomes.

## Model Architecture

Our model uses a multi-modal neural network architecture, processing various inputs:

- Drug SMILES data
- Disease names
- Protocol descriptions
- Clinical trial phases

We create semantically rich, high-dimensional vector embeddings using domain-specific large language models such as ChemBERTa and MedBERT. These embeddings are then fed into separate neural networks to create learned representations, which are concatenated and processed by a final neural network to output success probabilities.

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
