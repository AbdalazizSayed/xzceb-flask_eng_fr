import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('{apikey}')
language_translator = LanguageTranslatorV3(
    version='2023-02-23',
    authenticator=authenticator
    )

language_translator.set_service_url('{url}')


def english_to_French(text1):
    frenchtranslation = language_translator.translate(
            text=text1,
            model_id='en-fr').get_result()
    return frenchtranslation.get("translation")[0].get("translation")


def french_to_english(text1):
    
    englishtranslation = language_translator.translate(
            text=text1,
            model_id='fr-en').get_result()
    return englishtranslation.get("translation")[0].get("translation")
