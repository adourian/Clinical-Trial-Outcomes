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

![Process Overview](![image](https://github.com/user-attachments/assets/235f0cda-0abb-494a-acbf-f88e91b37da1)
)

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

In this section, we describe how we leveraged rich feature representations generated via domain-specific NLP models to predict the outcome of clinical trials. Our approach integrates heterogeneous data modalities—chemical, textual, and numerical—into a unified architecture designed to preserve and exploit their unique structure. Rather than flattening all inputs into a single representation from the outset, we allow the model to first specialize per modality and then learn meaningful cross-modal interactions through attention.

#### Model Architecture Overview

Our approach uses a multi-modal neural network architecture to handle the diverse types of data in our dataset. Here's a step-by-step breakdown of the process:

1. **Feature Representation**: 
   - **SMILES** strings are embedded using **ChemBERTa**, capturing structural and functional chemical information.
   - **Disease names, trial descriptions, inclusion/exclusion criteria** are encoded using models like **BioSimCSE** and **MedBERT**, optimized for biomedical and clinical text.

2. **Modality-specific Towers**:
   - Each input modality is routed through a **dedicated neural network tower**, allowing the model to learn features specific to the structure and distribution of that modality (e.g., chemical structure vs. clinical language).
   - This modular approach improves representational depth while reducing destructive interference between unrelated feature types.

3. **Attention-based Fusion**:
   - The outputs of all towers are then fused using an **attention mechanism**, enabling the model to dynamically weight and integrate the most relevant information across modalities.
   - This allows the model to learn context-sensitive interactions—for example, how trial design criteria may modulate the relevance of certain molecular properties.

5. **Joint Processing**:
   - The fused representation is concatenated with numerical features (e.g., trial phase, number of drugs) and passed through a final prediction head, which outputs the probability of trial success.


![Model Architecture](![image](https://github.com/user-attachments/assets/35150235-e3e1-4a23-b861-82f2c156db98))
*Figure 4: Simplified diagram of the multi-modal neural network architecture used for outcome prediction.*

This design enables the model to learn complementary and context-dependent signals from each data source—rather than forcing them into a single representation too early. The use of attention ensures that downstream predictions are driven by the most informative cross-modal interactions for each case. For detailed implementation and configuration, see the `clinical_trial_outcomes.ipynb` notebook in this repository.
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

