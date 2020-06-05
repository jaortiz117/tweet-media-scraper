from flask import Flask, render_template, send_file, request, redirect, url_for
from media_scraper import scrape
app = Flask(__name__)

# index (adds user through view)
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    try:
        # term = request.json["term"]
        term = request.form.get("search")
        print(term)
        file = scrape(term, term + '/', count=50, zip=True)

        return send_file(
        file,
        mimetype='application/zip',
        as_attachment=True,
        attachment_filename=term + '.zip'
        )

    except:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
