"""
This module contains functions to translate text from english
to french and from french to english.
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)


def english_to_french(english_text):
    """
    This function translates an input text in english
    to french.
    """
    french_translation = language_translator.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()
    return french_translation.get("translations")[0].get('translation')


def french_to_english(french_text):
    """
    This function translates an input text in french
    to english.
    """
    english_translation = language_translator.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()
    return english_translation.get("translations")[0].get('translation')
