from flask import Flask, render_template, send_file, request
from media_scraper import scrape
app = Flask(__name__)

# index (adds user through view)
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/download', methods=['GET'])
def download():
    term = request.json["term"]
    file = scrape(term, term + '/', count=30, zip=True)
    return send_file(
    file,
    mimetype='application/zip',
    as_attachment=True,
    attachment_filename=term + '.zip'
    )

if __name__ == '__main__':
    app.run(debug=True)
