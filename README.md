# Clinical Trial Outcomes Prediction

🎯 **Objective**: This project aims to improve decision-making in the pharmaceutical industry by predicting the outcomes of clinical trials using NLP and a multi-modal neural network architecture. By leveraging machine learning techniques, we create a tool to estimate the chances of success for clinical trials, potentially reducing the high costs and risks associated with drug development by identifying trials with a higher probability of failure early in the process.

## 📚 Table of Contents
- [Project Overview](#-project-overview)
- [Installation](#%EF%B8%8F-installation)
- [Data & Data Sources](#-data--data-sources)
- [Modelling](#-modelling)
- [Results](#-results)
- [License](#-license)
- [Contact](#-contact)
- [Acknowledgements](#-acknowledgements)

## 🚀 Project Overview

Drug development is a lengthy, expensive, and high-risk process, typically taking [12 to 15](https://www.frontiersin.org/journals/drug-discovery/articles/10.3389/fddsv.2023.1201419/full) years and costing between [1 and 3 billion USD](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2021.760762/full), with success rates as low as 8% from Phase I to market according to some [sources](https://go.bio.org/rs/490-EHZ-999/images/ClinicalDevelopmentSuccessRates2011_2020.pdf). This project addresses the need for better decision-making tools in the pharmaceutical industry by predicting clinical trial outcomes using machine learning techniques.

Our approach involves building a multi-modal neural network that integrates various data types to predict trial success. The main file for this project is `clinical_trial_outcomes.ipynb`.

![Process Overview](https://github.com/user-attachments/assets/a1d6b8c0-e531-47e1-b56a-b01f2f809e4c)
*Figure 1: Overview of the clinical trial prediction model.*

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

All the data for this project is sourced from the official U.S. government database for clinical trials at [clinicaltrials.gov](https://clinicaltrials.gov). 

A selection of trials were labelled by outcome by [Fu et al.](https://arxiv.org/abs/2102.04252) and IQVIA, providing a benchmark dataset, which we use as our base dataset. This base dataset is saved as `raw_data.csv`.
An XML file containing unlabeled data for all clinical trials was also retrieved from clinicaltrials.gov. This XML file was obtained by running the following line in a terminal:

```bash
wget https://clinicaltrials.gov/AllPublicXML.zip
```

This data was then parsed using the `read_xml.py` script. The resulting csv file in the data folder is called `compiled_clinical_trials.csv`. This is done to be able to retrieve additional features not present in the original benchmark dataset, such as the brief description of the trial protocol, by matching trials with their unique NCTID identifier.

### Key Features:
- **Drug SMILES Data**: Chemical structure representation of drugs.
- **Number of Drugs**: Count of drugs involved in each trial.
- **Disease Names**: Diseases targeted by the trials.
- **Protocol Description**: Brief text summary of the clinical trial protocol.
- **Inclusion Criteria**: Text description of the inclusion and exclusion criteria for trial participant enrollment. 
- **Clinical Trial Phases**: Phase of clinical trial. These are one-hot encoded.

All the relevant data can be found in the `/data` folder.

## 🧠 Modelling

### 🧩 Feature Representation Using NLP

Text data needs to be transformed into a format that can be processed by machine learning algorithms. In this project, we tackled four text features using natural language processing (NLP) techniques to create meaningful embeddings. Here’s a summary of our approach:

#### Why Use NLP?

Text data, such as SMILES, disease names and trial descriptions, cannot be fed directly into machine learning algorithms. To capture the significance of this data while retaining as much information as possible, we use embeddings. These embeddings convert text into numerical vectors that preserve semantic meaning.

![NLP for ML example](https://github.com/user-attachments/assets/82f8e57f-2575-47c0-b079-41332c4b75d2)
*Figure 2: Example of use case of NLP for Machine Learning tasks.*

#### Disease Names

Several pre-trained language models optimized for biomedical data were explored in the notebook `Disease_Embeddings.ipynb`:

- **BERT**: A general-purpose model for comparison.
- **BioBERT**, **BiomedBERT**, **MedBERT**, **tinyBioBERT**, **ClinicalBERT**, **BlueBERT**: Various domain-specific models trained on biomedical text corpuses.

For disease names, we used domain-specific embeddings to capture the biomedical context:

1. **Exploration**: We evaluated several models for their ability to represent diseases meaningfully. We classified diseases into categories and obtained embeddings from each model.
2. **Evaluation**: PCA analysis was performed on these embeddings to assess clustering and semantic similarity.

![PCA Analysis](https://github.com/user-attachments/assets/560721c0-92cf-4339-b0bb-b369426add72)
*Figure 3: PCA analysis of disease embeddings showing clustering of similar diseases.*

The PCA analysis of embeddings suggested that **MedBERT** provided the most promising results due to its ability to cluster similar diseases closely together. TinyBioBERT was also found to perform quite well given its reduced size. 

#### SMILES Data & Clinical Trial Descriptions

**SMILES** (Simplified Molecular Input Line Entry System) is a compact, readable notation used to represent chemical structures. It captures essential chemical information in a text format, making it ideal for computational tasks in cheminformatics. For embedding SMILES strings, **ChemBERTa** was chosen.
**Clinical Trial Descriptions and Enrollment Criteria** often include complex textual information, such as trial protocols and inclusion/exclusion criteria. To process these texts effectively, we used **BioSimCSE**.

**ChemBERTa** & **BioSimCSE** were chosen for two main reasons:
- **Performance**: ChemBERTa is designed specifically for SMILES, maintains chemical details effectively and performs well on a variety of tasks.
- **Integration**: It is compatible with the Hugging Face library, which facilitates easy implementation and manipulation.

#### Summary of Approach

1. **Feature Representation**: Applied NLP techniques to convert text into embeddings.
2. **Model Selection**: Evaluated multiple models and selected those that provided the best performance based on PCA analysis and literature research.
3. **Tools**: Created text embedding functions to automatically embed text features for later use during modelling. These functions are dumped in the `helpers.py` file. 

This approach ensured that we retained critical information from the text data while making it suitable for machine learning models.

### Outcome Prediction with Multi-Modal Neural Network

To leverage the multi-modal nature of the data, a multi-modal neural network architecture was employed. Each type of data (excluding numerical data such as phases and the number of drugs) is processed through a separate neural network to create a learned representation for that data type. These representations, along with the numerical data, are concatenated and fed into a final neural network that outputs the probability of trial success.

![Model Architecture](https://github.com/user-attachments/assets/296275dd-f74e-451a-b090-4696400fc123)
*Figure 4: Simplified representation of the multi-modal neural network architecture.*

This approach allows the model to extract and utilize features specific to each data type more effectively. By processing each modality separately before combining them, the model captures nuanced patterns within each data type, enhancing its ability to predict trial success.

## 📈 Results

The model showed improved performance over baseline models and XGBoost. Its performance was also comparable to the more complex GNN-based HINT model, suggesting that integrating rich, multi-modal data contributes significantly to the model’s effectiveness.

![Model Accuracy](https://github.com/user-attachments/assets/b7b4795e-66f5-4ca8-8e57-79bda40e96bb)
*Figure 5: Accuracy comparison of the multi-modal neural network against baseline models and XGBoost.*

![Model Performance](https://github.com/user-attachments/assets/4b0db35b-eedf-4573-84a4-f489039b06b9)
*Figure 6: F1 score and ROC AUC for the multi-modal neural network compared to the HINT benchmark model.*

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

For any questions or feedback, feel free to reach out:

- **Email**: kari.adourian@gmail.com
- **LinkedIn**: [LinkedIn](https://www.linkedin.com/in/kariadourian/)

## 🙏 Acknowledgements

- **Fu et al. (1)**: For the original dataset.
- **ClinicalTrials.gov**: For the XML file containing information about all clinical trials.



''# Clinical-Trial-Outcomes

''## Project Overview

Drug development is a lengthy, expensive, and high-risk process, typically taking 12 to 15 years and costing between 1 and 3 billion USD, with a success rate as low as 7.9% from Phase I to market. This project addresses the need for better decision-making tools in the pharmaceutical industry by predicting the outcomes of clinical trials using a multi-modal neural network architecture. By leveraging machine learning techniques, we provide a tool to estimate the chances of success for clinical trials, potentially reducing the high costs and risks associated with drug development. The main file for this project is **clinical_trial_outcomes.ipynb**.

![image](https://github.com/user-attachments/assets/a1d6b8c0-e531-47e1-b56a-b01f2f809e4c)
> *Figure 1:* Overview of process



''## Data

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



''## Modelling

To leverage the feature-rich, multi-modal nature of the data, we employed a multi-modal neural network architecture. Each data type (excluding numerical data such as phases and number of drugs) is processed independently through its own neural network. This approach generates a learned representation for each data type. These learned representations are then concatenated (along with the numerical data) and fed into a final neural network, which outputs the probability of trial success.

The rationale behind this architecture is to allow the model to discover relevant features specific to each data type more effectively. By processing each modality separately before combining them, the model can capture nuanced patterns within each data type. This approach enhances the model's ability to assess the probability of trial success by considering the unique contributions of each data modality.

![image](https://github.com/user-attachments/assets/296275dd-f74e-451a-b090-4696400fc123)
> *Figure 3:* Simplified representation of model. More details about architecture in notebook clinical_trial_outcomes.ipynb. 


''## Performance

The model performed better than the baseline model and XGBoost:

![image](https://github.com/user-attachments/assets/b7b4795e-66f5-4ca8-8e57-79bda40e96bb)
> *Figure 4:* Accuracy of models

The model performance was also similar to the more complex, GNN-based HINT model. This would suggest that the HINT authors' intuition, that the good performance compared to previous benchmarks is at least partly due to the integration of information rich, multi-modal data, is likely correct.

![image](https://github.com/user-attachments/assets/4b0db35b-eedf-4573-84a4-f489039b06b9)
> *Figure 5:* F1 score and ROC AUC for multi-modal NN and HINT benchmark

