# Clinical Trial Outcomes Prediction

🎯 **Objective**: This project aims to improve decision-making in the pharmaceutical industry by predicting the outcomes of clinical trials using a multi-modal neural network architecture. By leveraging machine learning techniques, we offer a tool to estimate the chances of success for clinical trials, potentially reducing the high costs and risks associated with drug development.

## 📚 Table of Contents
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Data & Data Sources](#data--data-sources)
- [Modelling](#modelling)
- [Results](#results)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## 🚀 Project Overview

Drug development is a lengthy, expensive, and high-risk process, typically taking 12 to 15 years and costing between 1 and 3 billion USD, with a success rate as low as 7.9% from Phase I to market. This project addresses the need for better decision-making tools in the pharmaceutical industry by predicting clinical trial outcomes using advanced machine learning techniques.

Our approach involves building a multi-modal neural network that integrates various data types to predict trial success. The main file for this project is `clinical_trial_outcomes.ipynb`.

![Process Overview](https://github.com/user-attachments/assets/a1d6b8c0-e531-47e1-b56a-b01f2f809e4c)
*Figure 1: Overview of the clinical trial prediction process.*

## 🛠️ Installation

To get started with this project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/adourian/Clinical-Trial-Outcomes.git
   cd Clinical-Trial-Outcomes
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

## 📊 Data & Data Sources

The dataset used in this project is derived from the official U.S. Food and Drug Administration (FDA) database at [clinicaltrials.gov](https://clinicaltrials.gov). The outcome labeling was performed by Fu et al. (1) and further refined by IQVIA, resulting in a benchmark dataset. We enhanced this dataset by incorporating brief trial descriptions retrieved from clinicaltrials.gov using the unique NCTID identifiers.

### Key Features:
- **Drug SMILES Data**: Represents the chemical structure of drugs.
- **Number of Drugs**: Count of drugs involved in the trial.
- **Disease Names**: Names of diseases targeted by the trial.
- **Protocol Descriptions**: Includes inclusion/exclusion criteria and brief descriptions of the trial.
- **Clinical Trial Phases**: One-hot encoded representations of the trial phases.

The text and SMILES features are transformed into semantically rich embeddings. For disease names, we experimented with different embedding models, and a PCA analysis was performed to evaluate the embeddings' quality. Two models, MedBERT and tinyBioBERT, were found to be effective, with MedBERT being used in the final models.

![PCA Analysis](https://github.com/user-attachments/assets/560721c0-92cf-4339-b0bb-b369426add72)
*Figure 2: PCA analysis of disease embeddings. Similar diseases are grouped closely together, indicating effective biological relevance capture.*

## 🧠 Modelling

To leverage the multi-modal nature of the data, a multi-modal neural network architecture was employed. Each type of data (excluding numerical data such as phases and the number of drugs) is processed through a separate neural network to create a learned representation for that data type. These representations, along with the numerical data, are concatenated and fed into a final neural network that outputs the probability of trial success.

This approach allows the model to extract and utilize features specific to each data type more effectively. By processing each modality separately before combining them, the model captures nuanced patterns within each data type, enhancing its ability to predict trial success.

![Model Architecture](https://github.com/user-attachments/assets/296275dd-f74e-451a-b090-4696400fc123)
*Figure 3: Simplified representation of the multi-modal neural network architecture.*

## 📈 Results

The model showed improved performance over baseline models and XGBoost. Its performance was also comparable to the more complex GNN-based HINT model, suggesting that integrating rich, multi-modal data contributes significantly to the model’s effectiveness.

![Model Accuracy](https://github.com/user-attachments/assets/b7b4795e-66f5-4ca8-8e57-79bda40e96bb)
*Figure 4: Accuracy comparison of the multi-modal neural network against baseline models and XGBoost.*

![Model Performance](https://github.com/user-attachments/assets/4b0db35b-eedf-4573-84a4-f489039b06b9)
*Figure 5: F1 score and ROC AUC for the multi-modal neural network compared to the HINT benchmark model.*

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

For any questions or feedback, feel free to reach out:

- **Email**: kari.adourian@gmail.com
- **LinkedIn**: [LinkedIn](https://www.linkedin.com/in/kariadourian/)

## 🙏 Acknowledgements

- **Fu et al. (1)**: For the original dataset.
- **ClinicalTrials.gov**: For the XML file containing information about all clinical trials.



# Clinical-Trial-Outcomes

## Project Overview

Drug development is a lengthy, expensive, and high-risk process, typically taking 12 to 15 years and costing between 1 and 3 billion USD, with a success rate as low as 7.9% from Phase I to market. This project addresses the need for better decision-making tools in the pharmaceutical industry by predicting the outcomes of clinical trials using a multi-modal neural network architecture. By leveraging machine learning techniques, we provide a tool to estimate the chances of success for clinical trials, potentially reducing the high costs and risks associated with drug development. The main file for this project is **clinical_trial_outcomes.ipynb**.

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

The clinical trial phases are one-hot encoded. The text and SMILES features are transformed into semantically rich embeddings. For diseases, an experiment was conducted in the Diseases.ipynb notebook to test different embedding models. A PCA analysis was performed on the resulting embeddings to see if biologically-related terms are grouped together. Two models stood out from the rest, MedBERT and tinyBioBERT. MedBERT embeddings ended up being used due to performing better in the final models. 

![PCA_diseases](https://github.com/user-attachments/assets/560721c0-92cf-4339-b0bb-b369426add72)

> *Figure 2:* PCA analysis of embeddings for diseases. Analysis carried out in Diseases.ipynb. Similar diseases are grouped close by together, suggesting that the embedding models effectively capture biologically relevant information about the diseases.



## Modelling

To leverage the feature-rich, multi-modal nature of the data, we employed a multi-modal neural network architecture. Each data type (excluding numerical data such as phases and number of drugs) is processed independently through its own neural network. This approach generates a learned representation for each data type. These learned representations are then concatenated (along with the numerical data) and fed into a final neural network, which outputs the probability of trial success.

The rationale behind this architecture is to allow the model to discover relevant features specific to each data type more effectively. By processing each modality separately before combining them, the model can capture nuanced patterns within each data type. This approach enhances the model's ability to assess the probability of trial success by considering the unique contributions of each data modality.

![image](https://github.com/user-attachments/assets/296275dd-f74e-451a-b090-4696400fc123)
> *Figure 3:* Simplified representation of model. More details about architecture in notebook clinical_trial_outcomes.ipynb. 


## Performance

The model performed better than the baseline model and XGBoost:

![image](https://github.com/user-attachments/assets/b7b4795e-66f5-4ca8-8e57-79bda40e96bb)
> *Figure 4:* Accuracy of models

The model performance was also similar to the more complex, GNN-based HINT model. This would suggest that the HINT authors' intuition, that the good performance compared to previous benchmarks is at least partly due to the integration of information rich, multi-modal data, is likely correct.

![image](https://github.com/user-attachments/assets/4b0db35b-eedf-4573-84a4-f489039b06b9)
> *Figure 5:* F1 score and ROC AUC for multi-modal NN and HINT benchmark

