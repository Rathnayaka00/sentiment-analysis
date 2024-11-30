# Sentiment Analysis Web Application

This is a web application that performs sentiment analysis on given text using Natural Language Processing (NLP). The application allows users to input text (reviews, tweets, etc.) and receives sentiment results such as **Positive**, **Negative**, or **Neutral**.

## Features
- **Real-time Sentiment Analysis**: Classifies user input text as **Positive**, **Negative**, or **Neutral**.
- **User-friendly Interface**: Built with **Streamlit** to provide an easy and interactive web interface.
- **Emoji-based Feedback**: Display sentiment with emojis (😊 for Positive, 😞 for Negative).

## Tech Stack
- **Backend**: Python, Flask
- **Frontend**: Streamlit
- **Sentiment Analysis Model**: A custom model trained on labeled data and saved as a pickled file.
- **Text Preprocessing**: Utilizes techniques such as stemming, stopword removal, and punctuation removal to improve accuracy.

## Installation Instructions

To run this project locally, follow the steps below:

### Prerequisites:
Make sure you have the following installed:
- Python 3.x
- pip

### Setup:
1. Clone the repository:
   ```bash
   git clone https://github.com/Rathnayaka00/sentiment-analysis-web-app.git

cd sentiment-analysis-web-app

pip install -r requirements.txt

## start the flask app
python app.py

## Launch the Streamlit app
streamlit run ui.py

