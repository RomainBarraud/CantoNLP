"""Master FLask application file for cantoNLP demo"""

import os, requests, uuid, json

from flask import Flask, request, jsonify, render_template
from textblob import TextBlob


subscription_key = 'bd3939e5b1174e2495dd86d1a30b825a'


def get_translation(text_input, language_output):
    base_url = 'https://api.cognitive.microsofttranslator.com'
    path = '/translate?api-version=3.0'
    params = '&to=' + str(language_output)
    constructed_url = base_url + path + params

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        #'Ocp-Apim-Subscription-Region': 'location',
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{

        'text' : text_input
    }]
    response = requests.post(constructed_url, headers=headers, json=body)
    return response.json()


def polarizer(polarity):
    if polarity < -0.5:
        return "very negative"
    elif polarity < -0.25:
        return "negative"
    elif polarity < 0:
        return "slightly negative"
    elif polarity == 0:
        return "neutral"
    elif polarity < 0.25:
        return "sligthly positive"
    elif polarity < 0.5:
        return "positive"   
    else:
        return "very positive"


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/", methods=["GET"])
def home():
    myResponse = ""
    return render_template("index.html", myResponse=myResponse)


@app.route('/', methods=['POST'])
def my_form_post():
    input_text = request.form['text']
    response = get_translation(input_text, 'en')
    engTranslation = response[0]['translations'][0]['text']
    blob = TextBlob(engTranslation)
    mySentiment = blob.sentences[0].sentiment.polarity
    myResponse = str(input_text) + " is " + str(polarizer(mySentiment)) + " with a polarity of " + str(round(mySentiment, 3))
    return render_template("index.html", myResponse=myResponse)


if __name__ == "__main__":
    app.debug = True
    app.run(host="127.0.0.1", port=5001)