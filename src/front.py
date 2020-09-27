from flask import Flask, render_template, request, redirect, abort
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk import word_tokenize
import bentoml
import itertools

app = Flask(__name__)
LOAD_PATH = "/home/parthparikh/bentoml/repository/PyTorchModel/20200926132654_E3B49E"

@app.route('/')
def index():
	return render_template('index.html', word_range=0)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        bento_service = bentoml.load(LOAD_PATH)
        # request debug
        print({"sentence": request.form["ner_text"]})
        sentence = request.form["ner_text"]

        result = bento_service.predict([{"sentence": request.form["ner_text"]}])
        tokens = result[0].split(",")
        all_words = [[word_tokenize(w), ' '] for w in sentence.split()]
        all_words = list(itertools.chain(*list(itertools.chain(*all_words))))
        print(all_words)

        return render_template('index.html', 
                                word_range=len(all_words), 
                                words=all_words, 
                                tokens=tokens, 
                                sentence=sentence)

if __name__ == "__main__":
    app.run(debug=True)