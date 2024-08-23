# Clinical Trial Outcomes Prediction

🎯 **Objective**: This project aims to improve decision-making in the pharmaceutical industry by predicting the outcomes of clinical trials using NLP and a multi-modal neural network architecture. By leveraging machine learning techniques, we create a tool to estimate the chances of success for clinical trials, potentially reducing the high costs and risks associated with drug development by identifying trials with a higher probability of failure early in the process.

## 📚 Table of Contents
- [Project Overview](#-project-overview)
- [Data & Data Sources](#-data--data-sources)
- [Modelling](#-modelling)
- [Results](#-results)
- [License](#-license)
- [Installation](#%EF%B8%8F-installation)
- [Contact](#-contact)
- [Acknowledgements](#acknowledgements)

## 🚀 Project Overview

Drug development is a lengthy, expensive, and high-risk process, typically taking [12 to 15](https://www.frontiersin.org/journals/drug-discovery/articles/10.3389/fddsv.2023.1201419/full) years and costing between [1 and 3 billion USD](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2021.760762/full), with success rates as low as 8% from Phase I to market according to some [sources](https://go.bio.org/rs/490-EHZ-999/images/ClinicalDevelopmentSuccessRates2011_2020.pdf). This project addresses the need for better decision-making tools in the pharmaceutical industry by predicting clinical trial outcomes using machine learning techniques.

Our approach involves building a multi-modal neural network that integrates various data types to predict trial success. The main file for this project is `clinical_trial_outcomes.ipynb`.

![Process Overview](https://github.com/user-attachments/assets/a1d6b8c0-e531-47e1-b56a-b01f2f809e4c)
*Figure 1: Overview of the clinical trial prediction model.*

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

Text data needs to be transformed into a format that can be processed by machine learning algorithms. In this project, we tackled four text features using natural language processing (NLP) techniques to create meaningful embeddings.

#### Why Use NLP?

Text data, such as SMILES, disease names, and trial descriptions, cannot be fed directly into machine learning algorithms. Biomedical text, in particular, is complex and contains domain-specific terminology. To capture the significance of this data while retaining as much information as possible, we use embeddings. These embeddings convert text into numerical vectors that preserve semantic meaning, making the data suitable for machine learning tasks.

![NLP for ML example](https://github.com/user-attachments/assets/82f8e57f-2575-47c0-b079-41332c4b75d2)
*Figure 2: Example of use case of NLP for Machine Learning tasks.*

#### Disease Names

To represent disease names, we explored several pre-trained language models optimized for biomedical data, as detailed in the notebook `Disease_Embeddings.ipynb`:

- **BERT**: A general-purpose model used for baseline comparison.
- **BioBERT**, **BiomedBERT**, **MedBERT**, **tinyBioBERT**, **ClinicalBERT**, **BlueBERT**: Domain-specific models trained on biomedical text corpora to capture specialized knowledge.

**Process:**

1. **Generating Embeddings**: We used each model to generate embeddings for a set of categorized diseases. This step involves converting text data into numerical vectors that represent semantic information.
   
2. **Clustering Analysis**: PCA analysis was conducted on the embeddings to evaluate how well similar diseases were clustered together. This analysis helped us understand which model best preserved the semantic relationships between diseases.

![PCA Analysis](https://github.com/user-attachments/assets/560721c0-92cf-4339-b0bb-b369426add72)
*Figure 3: PCA analysis of disease embeddings showing clustering of similar diseases.*

The PCA analysis of embeddings showed MedBERT as the most effective, clustering similar diseases closely. TinyBioBERT, despite its smaller size, also performed well, offering reduced dimensional complexity. Both models were tested in predictive modeling, but MedBERT ultimately delivered better results across architectures.

#### SMILES Data & Clinical Trial Descriptions

- **SMILES (Simplified Molecular Input Line Entry System)**: 
  - A compact, readable notation for chemical structures, ideal for computational tasks in cheminformatics.
  - **Chosen Embedding Model**: *ChemBERTa*.

- **Clinical Trial Descriptions and Enrollment Criteria**: 
  - Include complex textual information such as trial protocols and inclusion/exclusion criteria.
  - **Chosen Embedding Model**: *BioSimCSE*.

##### Why ChemBERTa & BioSimCSE Were Chosen:

| **Criterion**   | **ChemBERTa** | **BioSimCSE** |
|-----------------|---------------|---------------|
| **Performance** | Tailored for SMILES, maintains chemical details, excels in various tasks. | Handles complex clinical text effectively. |
| **Integration** | Compatible with Hugging Face, easy implementation. | Also integrates smoothly with Hugging Face. |

#### Summary of Approach

1. **Feature Representation**: Applied NLP techniques to convert text into embeddings.
2. **Model Selection**: Evaluated multiple models and selected those that provided the best performance based on PCA analysis and literature research.
3. **Tools**: Created text embedding functions to automatically embed text features for later use during modelling. These functions are dumped in the `helpers.py` file. 

Below is an example function for generating embeddings from SMILES data using ChemBERTa:

```python 
def build_ChemBERTa_features(smiles_list):

    # Determine if a GPU is available and set the device accordingly
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')  # Check if GPU is available
    print(f'Using device: {device}')

    # Load the tokenizer and the model from the pre-trained model
    chemberta = AutoModel.from_pretrained("DeepChem/ChemBERTa-77M-MTR")
    tokenizer = AutoTokenizer.from_pretrained("DeepChem/ChemBERTa-77M-MTR")

    # Move model to GPU if available
    chemberta.to(device)

    # Set the model to evaluation mode to disable dropout and other training-specific layers
    chemberta.eval()
    
    # Initialize an empty list to store the embeddings
    embeddings_list = []

    # Process each SMILES in the input list
    for smile in tqdm(smiles_list, desc="Processing sentences"):
        # Tokenize the SMILES, applying padding, and return as PyTorch tensors
        encoded_input = tokenizer(smile, padding=True, truncation=True, return_tensors='pt')

        # Move the tokenized input tensors to the specified device (GPU or CPU)
        encoded_input = {key: value.to(device) for key, value in encoded_input.items()}  

        # Pass the tokenized input through the model without calculating gradients (inference mode)
        with torch.no_grad():
            model_output = chemberta(**encoded_input)
        
        # Extract the embeddings for the [CLS] token from the last hidden state
        cls_embeddings = model_output.last_hidden_state[:, 0, :]
        
        # Move the embeddings back to the CPU and convert to a numpy array
        cls_embeddings_np = cls_embeddings.cpu().detach().numpy()

        # Append the numpy array to the list of embeddings
        embeddings_list.append(cls_embeddings_np)
    
    return embeddings_list
```

This approach ensured that we retained critical information from the text data while making it suitable for machine learning models.

### 🔮 Outcome Prediction with Multi-Modal Neural Network

In this section, we describe how we leveraged the feature representations created using NLP to predict the outcome of clinical trials. The process involves integrating multiple modalities of data into a unified model to make accurate predictions. The idea is to allow for neural networks to learn complex features about each data modality separately before combining these learned features to learn about their interactions and make a prediction.

#### Model Architecture Overview

Our approach uses a multi-modal neural network architecture to handle the diverse types of data in our dataset. Here's a step-by-step breakdown of the process:

1. **Feature Representation**: 
   - **SMILES**: Processed through ChemBERTa to generate chemical embeddings.
   - **Disease Names, Trial Descriptions, Criteria**: Embedded using domain-specific models like MedBERT and BioSimCSE.

2. **Separate Neural Networks for Each Modality**:
   - Each type of feature representation (e.g., SMILES embeddings, disease embeddings) is passed through its own dedicated neural network. This allows each network to learn features specific to the data type.

3. **Concatenation**:
   - The learned representations from each neural network are concatenated with numerical features, such as clinical trial phases and the number of drugs involved. This combined feature vector represents the complete set of inputs for the final prediction.

5. **Joint Processing Layer**:
   - The concatenated feature vector is processed by a joint neural network layer. This layer integrates information from all modalities to learn complex patterns and interactions.

6. **Prediction**:
   - The output of the joint processing layer is fed into a final prediction layer, which outputs the probability of the clinical trial's success or failure.

![Model Architecture](https://github.com/user-attachments/assets/296275dd-f74e-451a-b090-4696400fc123)
*Figure 4: Simplified diagram of the multi-modal neural network architecture used for outcome prediction.*

This multi-modal approach enables the model to leverage the rich, complementary information provided by different feature types, enhancing its ability to predict clinical trial outcomes accurately. For detailed information about the neural network architecture, including the exact implementation and configuration of the networks, refer to the `clinical_trial_outcomes.ipynb` notebook in this repository.

## 📈 Results

The model showed improved performance over baseline models and XGBoost. Its performance was also comparable to the more complex GNN-based [HINT](https://arxiv.org/abs/2102.04252) model, suggesting that integrating rich, multi-modal data contributes significantly to the model’s effectiveness.

![Model Accuracy](https://github.com/user-attachments/assets/b7b4795e-66f5-4ca8-8e57-79bda40e96bb)
*Figure 5: Accuracy comparison of the multi-modal neural network against baseline models and XGBoost.*

![Model Performance](https://github.com/user-attachments/assets/4b0db35b-eedf-4573-84a4-f489039b06b9)
*Figure 6: F1 score and ROC AUC for the multi-modal neural network compared to the HINT benchmark model.*

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🛠️ Installation

To get started with this project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/adourian/Clinical-Trial-Outcomes.git
   cd Clinical-Trial-Outcomes
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

## 📧 Contact

For any questions or feedback, feel free to reach out:

- **Email**: kari.adourian@gmail.com
- **LinkedIn**: [LinkedIn](https://www.linkedin.com/in/kariadourian/)

## Acknowledgements

- **Fu et al.**: For the [original dataset](https://github.com/futianfan/clinical-trial-outcome-prediction/tree/main/data).
- **ClinicalTrials.gov**: For the XML file containing information about all clinical trials.

