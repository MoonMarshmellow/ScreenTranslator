from translate import Translator

def transtode(text):
    translator = Translator(from_lang='de',to_lang='en')
    print(translator.translate(str(text)))
