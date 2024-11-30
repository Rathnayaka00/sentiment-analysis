from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import re
import string
import pickle
from nltk.stem import PorterStemmer

app = Flask(__name__)

with open('static/model/model.pickle', 'rb') as f:
    model = pickle.load(f)

with open('static/model/corpora/stopwords/english', 'r') as file:
    stopwords = file.read().splitlines()

vocab = pd.read_csv('static/model/vocabulary.txt', header=None)
tokens = vocab[0].tolist()

ps = PorterStemmer()

def remove_punctuations(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    return text

def preprocessing(text):
    data = pd.DataFrame([text], columns=['tweet'])
    data['tweet'] = data['tweet'].apply(lambda x: " ".join(x.lower() for x in x.split()))
    data['tweet'] = data['tweet'].apply(lambda x: " ".join(re.sub(r"https?://\S+|www\.\S+", '', x) for x in x.split()))
    data['tweet'] = data['tweet'].apply(remove_punctuations)
    data['tweet'] = data['tweet'].str.replace('\d+', '', regex=True)
    data['tweet'] = data['tweet'].apply(lambda x: " ".join(x for x in x.split() if x not in stopwords))
    data['tweet'] = data['tweet'].apply(lambda x: " ".join(ps.stem(x) for x in x.split()))
    return data['tweet']

def vectorizer(ds, vocabulary):
    vectorized_lst = []
    for sentence in ds:
        sentence_lst = np.zeros(len(vocabulary))
        for i in range(len(vocabulary)):
            if vocabulary[i] in sentence.split():
                sentence_lst[i] = 1
        vectorized_lst.append(sentence_lst)
    return np.asarray(vectorized_lst, dtype=np.float32)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        text = data.get('review', '')
        
        if not text:
            return jsonify({'error': 'No review text provided'}), 400
        
        preprocessed_text = preprocessing(text)
        vectorized_text = vectorizer(preprocessed_text, tokens)
        
        prediction = model.predict(vectorized_text)
        sentiment = "Positive" if prediction == 0 else "Negative" if prediction == 1 else "Neutral"
        
        return jsonify({'sentiment': sentiment})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
