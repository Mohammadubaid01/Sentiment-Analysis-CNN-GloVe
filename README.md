🎬 Movie Review Sentiment Analysis using CNN and GloVe

Overview

This project performs binary sentiment classification on movie reviews using a Convolutional Neural Network (CNN) combined with pre-trained GloVe (Global Vectors for Word Representation) embeddings.

The model classifies reviews as either:

* Positive 😊
* Negative 😞

Pre-trained GloVe embeddings are used to provide semantic understanding of words, while the CNN extracts important sentiment-related patterns from review text.

⸻

Features

* Text preprocessing and cleaning
* Tokenization and sequence padding
* Pre-trained GloVe word embeddings (100-dimensional)
* Fine-tuned embedding layer during training
* CNN-based sentiment classification
* Early Stopping and Learning Rate Scheduling
* Model evaluation using:
    * Accuracy
    * Precision
    * Recall
    * F1-Score
    * Confusion Matrix
* Training and Validation Accuracy Curves
* Training and Validation Loss Curves

⸻

Technologies Used

* Python
* TensorFlow / Keras
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-Learn
* NLTK
* SpaCy

⸻

Model Architecture

Input Review
↓
Tokenization & Padding
↓
GloVe Embedding Layer (100D)
↓
Conv1D (256 Filters, Kernel Size = 5)
↓
Global Max Pooling
↓
Dense Layer (64 Neurons, ReLU)
↓
Dropout (0.5)
↓
Output Layer (Sigmoid)
↓
Positive / Negative Sentiment

⸻

Training Configuration

* Vocabulary Size: 10,000 Words
* Maximum Review Length: 200 Tokens
* Embedding Dimension: 100
* Batch Size: 128
* Epochs: 12
* Optimizer: Adam
* Loss Function: Binary Crossentropy

⸻

Results

Model Performance

Metric	Score
Test Accuracy	88.57%
Sentiment Classes	Positive / Negative
Embedding Type	GloVe 100D
Neural Network	CNN

The model demonstrates strong generalization performance on unseen movie reviews and effectively captures sentiment patterns from textual data.

⸻

Visualizations

The project includes:

* Training Accuracy vs Validation Accuracy
* Training Loss vs Validation Loss
* Confusion Matrix Heatmap

These visualizations help analyze model performance and potential overfitting.

⸻

Project Structure

project/

├── notebook/

├── models/

├── images/

├── configuration.py

├── predict.py

├── requirements.txt

└── README.md

⸻

Example Prediction

Input Review:

“This movie was absolutely amazing and the acting was outstanding.”

Prediction:

Positive Sentiment

⸻

Future Improvements

* Multi-Kernel CNN Architecture
* CNN + BiLSTM Hybrid Model
* Attention Mechanism
* BERT Fine-Tuning
* RoBERTa Fine-Tuning
* Streamlit Web Application
* Docker Deployment
* Model API using FastAPI

⸻

Author

Developed as a Machine Learning and Natural Language Processing project to explore deep learning techniques for sentiment analysis using pre-trained word embeddings and convolutional neural networks.
