from flask import Flask, redirect, url_for, render_template, current_app, request
from api import Refran

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	refran = Refran()
	if request.method == 'POST':
		return render_template('index.html', linea=refran.generate_refran())
		
	return render_template('index.html', linea=refran.generate_refran())
    
if __name__ == '__main__':
    app.run(debug=True)
