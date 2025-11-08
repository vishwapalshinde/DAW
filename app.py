from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/mice')
def mice():
    return render_template('mice.html')

@app.route('/insurance')
def insurance():
    return render_template('insurance.html')

if __name__ == '__main__':
    app.run(debug=True)
