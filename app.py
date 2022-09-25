from flask import Flask, send_from_directory
from flask import render_template, request, flash, url_for
from werkzeug.utils import secure_filename
import os
import videoEditor

app = Flask(__name__, static_folder='static')
app.config['UPLOAD_FOLDER'] = 'static/media'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['video_file']
        if not file.filename:
            flash('Видео не загружено!')
        else:
            filename = secure_filename(file.filename)
            file.save((os.path.join(app.config['UPLOAD_FOLDER'], filename)))
            fileLink = str((os.path.join(app.config['UPLOAD_FOLDER'], filename)))
    return render_template('index.html')


@app.route('/render', methods=['POST'])
def index1():
    if request.method == 'POST':
        cutJson = request.json
        data = json.load(cutJson)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
