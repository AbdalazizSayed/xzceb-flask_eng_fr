from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

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

##printing 
