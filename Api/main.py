from flask import Flask, request, jsonify
import pickle
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    return jsonify({'msg': 'You are in the home page'})


def clean_text(a):
    x = re.sub('[^a-zA-Z]', ' ', a)
    x = x.lower()
    text = nltk.word_tokenize(x)
    text = [WordNetLemmatizer().lemmatize(word)
            for word in text if word not in stopwords.words('english')]
    text = ' '.join(text)
    return text


@app.route('/predict-tf', methods=['POST'])
def prepare():
    message = request.form.get('message')
    with open('./Models/tokenizer.pkl', 'rb') as f:
        tokenizer = pickle.load(f)
    model = tf.keras.models.load_model('Models/model_v6.hdf5')
    tokens = tokenizer.texts_to_sequences([message])
    padded = pad_sequences(tokens, maxlen=942)
    predict = model.predict(padded)
    pr = (predict > 0.5)
    if pr[0][0] == 0:
        return jsonify({'status': 200, 'msg': 'Depression'})
    elif pr[0][0] == 1:
        return jsonify({'status': 200, 'msg': 'Suicide'})
    else:
        return jsonify({'status': 404, 'msg': 'Server Error'})


@app.route('/predict', methods=['POST'])
def predict():
    message = request.form.get('message')
    with open('./Models/multinomialNB.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('./Models/count_vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    text = clean_text(message)
    x = vectorizer.transform([text])
    pr = model.predict(x)
    if pr[0] == 0:
        return jsonify({'status': 200, 'msg': 'Depression'})
    elif pr[0] == 1:
        return jsonify({'status': 200, 'msg': 'Suicide'})
    else:
        return jsonify({'status': 404, 'msg': 'Server Error'})


if __name__ == '__main__':
    print("flask server running")
    app.run(debug=True)
