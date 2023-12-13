from googletrans import Translator
# command install googletrans: pip install googletrans==4.0.0-rc1

def translater(input):
    if not input:
        print("Texto de entrada vazio ou nulo.")
        return None
    
    translator = Translator()

    
    try:
        output = translator.translate(input, dest='en')
        
        if output is None:
            print("output is None")
            return None
        
        return output
    except Exception as e:
        print(f"Error traduction: {e}")
        return None
