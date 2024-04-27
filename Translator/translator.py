from flask import Flask, request, render_template
from googletrans import Translator
import requests

app = Flask(__name__)
app.secret_key = 'arkajit'
WORDNIK_API_KEY = 'your_wordnik_api_key_here'  # Replace this with your Wordnik API key

@app.route("/translate_lang", methods=["POST"])
def translate_lang():
    if request.method == "POST":
        sentence = request.form["sentence"]
        code = request.form["code"]
        
        translator = Translator()
        translation = translator.translate(sentence, dest=code)
        translated_text = translation.text

        meaning = get_sentence_meaning(sentence)
        
        return render_template("translation_result.html", language_selected=code, sentence=sentence, translated_res=translated_text, sentence_meaning=meaning)

def get_sentence_meaning(sentence):
    url = 'https://api.wordnik.com/v4/word.json/{}/definitions'
    params = {'api_key': 'b3uphyeo9o7fh2o0fo8379zg1tl7tw8vgzvscjid7qw8xj9l2'}
    words = sentence.split()  # Split sentence into individual words
    meanings = []

    for word in words:
        # Send API request for each word
        response = requests.get(url.format(word), params=params)
        if response.status_code == 200:
            definitions = response.json()
            if definitions:
                meanings.append(f"{word}: {definitions[0]['text']}")
            else:
                meanings.append(f"{word}: Meaning not found")
        else:
            meanings.append(f"{word}: Error in fetching meaning")

    # Combine the meanings for each word
    return "\n".join(meanings)



@app.route("/")
def index():
    languages = [
        {"name": "African", "code": "af"},
        {"name": "Irish", "code": "ga"},
        {"name": "Albanian", "code": "sq"},
        {"name": "Italian", "code": "it"},
        {"name": "Arabic", "code": "ar"},
        {"name": "Bengali", "code": "bn"},
        {"name": "Hindi", "code": "hi"},
        {"name": "English", "code": "en"},
        {"name": "Korean", "code": "ko"},
        {"name": "Japanese", "code": "ja"},
        {"name": "Armenian", "code": "hy"},
        {"name": "German", "code": "de"},
        {"name": "Filipino", "code": "tl"},
        {"name": "Russian", "code": "ru"},
        {"name": "Vietnamese", "code": "vi"},
        {"name": "Spanish", "code": "es"},
        {"name": "Thai", "code": "th"},
        {"name": "Turkish", "code": "tr"},
        {"name": "Urdu", "code": "ur"},
        {"name": "Punjabi", "code": "pa"},
        {"name": "Portguese", "code": "pt"},
        {"name": "Polish", "code": "pl"},
        {"name": "Persian", "code": "fa"},
        {"name": "Odia", "code": "or"},
        {"name": "Nepali", "code": "ne"},
        {"name": "French", "code": "fr"},
        {"name": "Chinese (Simplified)", "code": "zh-CN"},
        {"name": "Chinese (Traditional)", "code": "zh-TW"},
        {"name": "Dutch", "code": "nl"},
        {"name": "Swedish", "code": "sv"},
        {"name": "Greek", "code": "el"},
        {"name": "Danish", "code": "da"},
        {"name": "Finnish", "code": "fi"},
        {"name": "Norwegian", "code": "no"},
        {"name": "Czech", "code": "cs"},
        {"name": "Hungarian", "code": "hu"},
        {"name": "Indonesian", "code": "id"},
        {"name": "Malay", "code": "ms"},
        {"name": "Romanian", "code": "ro"},
        {"name": "Slovak", "code": "sk"},
        {"name": "Ukrainian", "code": "uk"},
        {"name": "Croatian", "code": "hr"},
        {"name": "Bulgarian", "code": "bg"},
        {"name": "Slovenian", "code": "sl"},
        {"name": "Estonian", "code": "et"},
        {"name": "Latvian", "code": "lv"},
        {"name": "Lithuanian", "code": "lt"}
    ]
    
    return render_template("index.html", languages=languages)

if __name__ == "__main__":
    app.run(debug=True)
