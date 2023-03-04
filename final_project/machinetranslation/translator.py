from os import environ
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = environ['apikey']
url = environ['url']

# Add code to create an instance of the IBM Watson Language Translator service
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)


def none_check(function):
    def check(param):
        if param is not None:
            return function(param)
        return None

    return check


# Add function englishToFrench which takes in the englishText as a string argument
@none_check
def english_to_french(english_text=None):
    language_translator.set_service_url(url)
    translated_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = translated_text['translations'][0]['translation']

    return french_text


# Add function frenchToEnglish which takes in the frenchText as a string argument
@none_check
def french_to_english(french_text=None):
    language_translator.set_service_url(url)
    translated_text = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = translated_text['translations'][0]['translation']

    return english_text
