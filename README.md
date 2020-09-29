<h1 align="left">
  <br>
    <img src="https://i.imgur.com/llRw5MA.png" align="right" height=400px title="Auto-Tagger" alt="Auto-Tagger Logo">
  <br>
  Auto-Tagger
  <br>
</h1>

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/MLH-Fellowship/Auto-Tagger.svg)](https://github.com/MLH-Fellowship/Auto-Tagger/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/MLH-Fellowship/Auto-Tagger.svg)](https://github.com/MLH-Fellowship/Auto-Tagger/pulls)

<h4 align="left">An Artificial Intelligence tool that uses Transformer models and NER (Named Entity Recognition) techniques to detect proper names in a text. <br><br>
This repo contains:</h4>

* **The Auto-Tagger Web App**
* **The Auto-Tagger Discord bot**

**A video demo can be found here: <a href="https://www.youtube.com/watch?v=3XF4hOLtU1o"> **https://www.youtube.com/watch?v=3XF4hOLtU1o**</a>**

<br><br><br><br><br><br>

<h2 align="center">Auto-Tagger Repo</h2>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#calling-the-api">Calling the API</a> •
  <a href="#using-flask">Using Flask</a> •
  <a href="#creating-and-running-a-docker-image-and-deploying-it-on-heroku">Docker image</a> •
  <a href="#data">Data</a> •
  <a href="#training-a-new-model">Training a new model</a> •
  <a href="#contributing">Contributing</a>
</p>

<br><br>
## Our Auto-Tagger Web Application
<p align="center">
<img src="https://i.imgur.com/7wWrjNS.gif" >
</p>

## Our Auto-Tagger Discord Bot
<p align="center">
<img src="https://i.imgur.com/tdKFxwr.gif" >
</p>

## Key Features 

- [x] Usage of Transformer models ( BERT in this case ) and NER ( Named Entity Recognition ) techniques.
- [x] Building a training pipeline.
- [x] Implementing and training the model ( using Google Colab ).
- [x] Building an inference pipeline.
- [x] Serving the model using BentoML.
- [x] Create a Web Application to visualize our Auto-Tagger features.
- [x] Create a Discord bot that implements the Auto-Tagger features.

-------

## Installation

- All the `code` required to get started

### Clone

- Clone this repo to your local machine using `https://github.com/MLH-Fellowship/Auto-Tagger.git`

### Setup

In order to install all packages follow the steps below:

1. Download the model from this drive: https://drive.google.com/file/d/1TyuIoMO42CHHvQVlOpw6Ynco39rQbc6t/view?usp=sharing

2. Put it in the `/results/model.bin` ( rename the file as `model.bin` )

3. Download the BERT uncased model from here: https://www.kaggle.com/abhishek/bert-base-uncased

4. Unzip the files in `/model/`

5. Run `python serving.py` inside `/src/`

6. Execute the command `bentoml serve PyTorchModel:latest`

> The model will be served on **http://127.0.0.1:5000/**

-------

## Calling the api
To send a request you'd need to send in a POST request:

```bash
curl -i --header "Content-Type: application/json" \
        --request POST \
        --data '{"sentence": "John used to play for The Beatles"}' \
        http://127.0.0.1:5000/predict
```

Example:

```bash
#request
{ 
  "sentence": "Jack and James went to the university and they met Emily"
}
```

The response will be a string of all the names detected separated by a ','. In this example it will be:

```bash
#response
"jack,james,emily"
```

-------

## Using Flask
Follow these steps after step 5 in **Setup** (in `/src/` directory):

```bash
export FLASK_APP=front.py
export FLASK_DEBUG=1 # For debugging
flask run
```
> Note: Be sure to modify the `LOAD_PATH` variable in `front.py` depending on your bentoml latest model location

-------

## Creating and running a Docker image and deploying it on Heroku
This sub-section is thoroughly explained in the [wiki page](https://github.com/MLH-Fellowship/Auto-Tagger/wiki/Creating-and-running-a-Docker-image) of this repository.

-------

## Creating and running the discord bot
Documentation is available at the [wiki page](https://github.com/MLH-Fellowship/Auto-Tagger/wiki/Running-the-bot-on-Discord) of this repository.

-------

## Data
We used an Annotated Corpus for Named Entity Recognition dataset, that we found on kaggle: https://www.kaggle.com/abhinavwalia95/entity-annotated-corpus

This is the extract from GMB corpus which is tagged, annotated and built specifically to train the classifier to predict named entities such as name, location, etc.

This dataset contains 47958 sentences with 948241 words.

-------
## Training a new model
You can train your own model by using the `train.py` script.
Change the `config.py` file with the parameters you want and then execute the following command:

```bash
python train.py
```
This will generate your model file in `config.MODEL_PATH` as `model.bin`.

-------

## Contributing

> To get started...

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using `https://github.com/MLH-Fellowship/Auto-Tagger.git`

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request using <a href="https://github.com/MLH-Fellowship/Auto-Tagger/compare/" target="_blank">`https://github.com/MLH-Fellowship/Auto-Tagger/compare/`</a>.

-------

## License
This project is licensed under the [Apache License, Version 2.0](https://github.com/MLH-Fellowship/Auto-Tagger/blob/master/LICENSE).
