# Flask file

# Importing necessary libraries
from flask import Flask, request, render_template, url_for
import pickle
from src.pipeline.predict_pipeline import CustomData, PredictPipeline


# Creating a Flask object
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictlanguage', methods=['POST','GET'])
def predictlanguage():
    if request.method == 'GET':
        return render_template('result.html')
    else:
        data = CustomData(text=request.form.get('text'))
        df = data.get_data_as_dataframe()
        print(df)
        print('Before Prediction')
        predict_pipeline = PredictPipeline()
        print("Mid Prediction")
        result = predict_pipeline.predict(df)
        output = result[0]
        print('Prediction Completed')
        print(output)
        return render_template('result.html', language=output)




if __name__ == "__main__":
    app.run(debug=True)
