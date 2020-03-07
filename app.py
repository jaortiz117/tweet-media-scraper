from flask import Flask, render_template

app = Flask(__name__)

# index (adds user through view)
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/download', methods=['GET'])
def download():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
