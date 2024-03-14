# Flask file

# Importing necessary libraries
from flask import Flask, request, render_template, url_for
import pickle

# Importing the model
model = pickle.load(open('models/model.pkl', 'rb'))

# Creating a Flask object
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form', methods=['POST','GET'])
def form():
    if request.method == 'POST':
        input = request.form.get('input')
    return render_template('result.html', input=input)
    




if __name__ == "__main__":
    app.run(debug=True)