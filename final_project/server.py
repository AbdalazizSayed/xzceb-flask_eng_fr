from machinetranslation import translator
from flask import Flask, render_template, request
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
import json

app = Flask("Web Translator")
apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2023-02-23',
    authenticator=authenticator
    )
@app.route("/englishToFrench")

def english_to_French(text1):
    frenchtranslation = language_translator.translate(
            text=text1,
            model_id='en-fr').get_result()
    return frenchtranslation.get("translation").get("translation")



@app.route("/frenchToEnglish")

def french_to_english(text1):
    
    englishtranslation = language_translator.translate(
            text=text1,
            model_id='fr-en').get_result()
    return englishtranslation.get("translation").get("translation")


@app.route("/")
def renderIndexPage():
    # Write the code to render template

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8080)
    renderIndexPage()
##printing  
