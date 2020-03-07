from flask import Flask, render_template

app = Flask(__name__)

# index (adds user through view)
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
