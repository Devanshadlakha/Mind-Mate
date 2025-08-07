from deep_translator import GoogleTranslator

def detect_lang(text):
    try:
        return GoogleTranslator(source='auto', target='en').translate(text)
    except Exception:
        return 'en'

def translate_to_english(text):
    try:
        return GoogleTranslator(source='auto', target='en').translate(text)
    except Exception:
        return text

def translate_from_english(text, target_lang):
    try:
        return GoogleTranslator(source='en', target=target_lang).translate(text)
    except Exception:
        return text

