from flask import Flask, request, render_template
from googletrans import Translator

app = Flask(__name__)
app.secret_key = 'arkajit'

@app.route("/translate_lang", methods=["POST"])
def translate_lang():
    if request.method == "POST":
        sentence = request.form["sentence"]
        code = request.form["code"]
        
        translator = Translator()
        translation = translator.translate(sentence, dest=code)
        translated_text = translation.text
        
        return render_template("translation_result.html", language_selected=code, sentence=sentence, translated_res=translated_text)

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
        {"name": "Japanese", "code": "ja"}
    ]
    
    return render_template("index.html", languages=languages)

if __name__ == "__main__":
    app.run(debug=True)