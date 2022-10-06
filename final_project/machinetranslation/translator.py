'''
This module translates English to French and vice-versa
'''

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def english_to_french(english_text):
    '''
    This function returns English to French translations
    '''
    apikey = "G89iK2YEDHwJrNljSVB3V1adiu1AupTsHcrnI4lcbRDi"
    url = "https://api.us-south.language-translator.watson.cloud.ibm.com/instances/\
        87399dae-34dd-4354-8f6c-5eab31f5edfe"

    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )

    language_translator.set_service_url(url)

    fr_translation_response = language_translator.translate(\
        text=english_text, model_id='en-fr')

    fr_translation=fr_translation_response.get_result()

    return list(fr_translation.items())[0][1][0]['translation']


def french_to_english(french_text):
    '''
    This function returns French to English translations
    '''
    apikey = "G89iK2YEDHwJrNljSVB3V1adiu1AupTsHcrnI4lcbRDi"
    url = "https://api.us-south.language-translator.watson.cloud.ibm.com/instances/\
            87399dae-34dd-4354-8f6c-5eab31f5edfe"

    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )

    language_translator.set_service_url(url)

    en_translation_response = language_translator.translate(\
        text=french_text, model_id='fr-en')

    en_translation=en_translation_response.get_result()

    return list(en_translation.items())[0][1][0]['translation']
