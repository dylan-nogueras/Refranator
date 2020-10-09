from flask import Flask, redirect, url_for, render_template, current_app
from api import Refran

app = Flask(__name__)

@app.route('/')
def home():
	refran = Refran()
	return render_template('index.html', linea=refran.generate_refran())
    
if __name__ == '__main__':
    app.run(debug=True)
