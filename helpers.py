# File to store helper functions

import torch
import torch.nn as nn
import numpy as np
from transformers import AutoModelForMaskedLM, AutoTokenizer, AutoModel
from sentence_transformers import SentenceTransformer
import pandas as pd
from tqdm import tqdm


def build_tinybioBERT_features(sentence_list):

    # Determine if a GPU is available and set the device accordingly
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')  # Check if GPU is available
    print(f'Using device: {device}')

    # Load the tokenizer and the model from the pre-trained model
    tokenizer = AutoTokenizer.from_pretrained("nlpie/tiny-biobert")
    tinybiobert = AutoModel.from_pretrained("nlpie/tiny-biobert")

     # Move model to GPU if available
    tinybiobert.to(device) 

    # Set the model to evaluation mode to disable dropout and other training-specific layers
    tinybiobert.eval() 

    # Initialize an empty list to store the embeddings
    embeddings_list = []

    for sentence in tqdm(sentence_list, desc="Processing sentences"):
        # Tokenize the text
        encoded_input = tokenizer(sentence, padding='max_length', max_length=512, truncation=True, return_tensors='pt')
        encoded_input = {key: value.to(device) for key, value in encoded_input.items()}  # Move inputs to GPU if available
        
        # Pass the tokenized input through the model
        with torch.no_grad():
            model_output = tinybiobert(**encoded_input)
        
        # Extract the embeddings for the [CLS] token
        cls_embeddings = model_output.last_hidden_state[:, 0, :] 
        
          # Move embeddings back to CPU and convert to numpy array
        cls_embeddings_np = cls_embeddings.cpu().detach().numpy()


        embeddings_list.append(cls_embeddings_np)
    
    return embeddings_list

def build_medBERT_features(sentence_list):
    # Determine if a GPU is available and set the device accordingly
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu') 
    print(f'Using device: {device}')

    # Load the tokenizer and the model from the pre-trained model
    tokenizer = AutoTokenizer.from_pretrained("Charangan/MedBERT")
    medbert = AutoModel.from_pretrained("Charangan/MedBERT")

    # Move model to GPU if available
    medbert.to(device)

    # Set the model to evaluation mode to disable dropout and other training-specific layers
    medbert.eval()

    # Initialize an empty list to store the embeddings
    embeddings_list = []

    # # Get the model configuration to check max length for padding
    # config = biomedbert.config
    # # Print the maximum sequence length
    # print(f"Maximum sequence length: {config.max_position_embeddings}")

    # Process each sentence/word in the input list
    for sentence in tqdm(sentence_list, desc="Processing sentences"):
        # Tokenize the sentence/word, applying padding and truncation, and return as PyTorch tensors
        encoded_input = tokenizer(sentence, padding='max_length', max_length=512, truncation=True, return_tensors='pt')

        # Move the tokenized input tensors to the specified device (GPU or CPU)
        encoded_input = {key: value.to(device) for key, value in encoded_input.items()}
        
        # Pass the tokenized input through the model without calculating gradients (inference mode)
        with torch.no_grad():
            model_output = medbert(**encoded_input)
        
        # Extract the embeddings for the [CLS] token from the last hidden state
        cls_embeddings = model_output.last_hidden_state[:, 0, :]  

        # Move the embeddings back to the CPU and convert to a numpy array
        cls_embeddings_np = cls_embeddings.cpu().detach().numpy()

        # Append the numpy array to the list of embeddings
        embeddings_list.append(cls_embeddings_np)
    
    return embeddings_list

def build_BioSimCSE_features(sentence_list):
    # Determine if a GPU is available and set the device accordingly
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'Using device: {device}')

    # Load the model
    model = SentenceTransformer('kamalkraj/BioSimCSE-BioLinkBERT-BASE')

    # Move model to GPU if available
    model = model.to(device)

    # Set the model to evaluation mode
    model.eval()

    # Initialize an empty list to store the embeddings
    embeddings_list = []

    # Process each sentence in the input list
    for sentence in tqdm(sentence_list, desc="Processing sentences"):
        # Generate embeddings
        with torch.no_grad():
            embedding = model.encode(sentence, convert_to_tensor=True)
        
        # Move the embedding to CPU and convert to numpy array
        embedding_np = embedding.cpu().numpy()

        # Append the numpy array to the list of embeddings
        embeddings_list.append(embedding_np)
    
    return embeddings_list

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

def longest_and_average_word_count(data, columns):
    results = {}

    for column in columns:
        max_length = 0
        total_word_count = 0
        cell_count = 0

        for text in data[column]:
            if text is not None:  # Check for None values
                word_count = len(text.split())
                total_word_count += word_count
                cell_count += 1
                if word_count > max_length:
                    max_length = word_count

        average_word_count = total_word_count / cell_count if cell_count > 0 else 0
        results[column] = (max_length, average_word_count)

    return results