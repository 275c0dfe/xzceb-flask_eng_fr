import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

auth = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(version="2018-05-01" , authenticator = auth)
language_translator.set_service_url(url)


def englishToFrench(englishText):
    if not englishText:
        return ""

    translation_request = language_translator.translate(text=englishText , model_id="en-fr")

    if translation_request.get_status_code() != 200:
        return "Error Connecting to Translation Service"

    translations = translation_request.get_result()["translations"]

    if len(translations) < 1:
        return "No Translation"

    frenchText = translations[0]["translation"]
    return frenchText


def frenchToEnglish(frenchText):
    if not frenchText:
        return ""

    translation_request = language_translator.translate(text=frenchText , model_id="fr-en")

    if translation_request.get_status_code() != 200:
        return "Error Connecting to Translation Service"

    translations = translation_request.get_result()["translations"]

    if len(translations) < 1:
        return "No Translation"

    englishText = translations[0]["translation"]
    return englishText



