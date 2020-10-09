from flask import Flask, redirect, url_for, render_template, current_app


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)
