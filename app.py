# Flask file

# Importing necessary libraries
from flask import Flask, request, render_template

# Creating a Flask object
app = Flask(__name__)



if __name__ == "__main__":
    app.run(debug=True)