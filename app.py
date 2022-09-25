from flask import Flask, send_from_directory
from flask import render_template, request, flash, url_for, json
from werkzeug.utils import secure_filename
import os
from videoEditor import VideoEdit
import glob, time

app = Flask(__name__, static_folder='static')
app.config['UPLOAD_FOLDER'] = 'static\\media'

FRAME_RATE = 30
cur_dir = os.getcwd()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['video_file']
        if not file.filename:
            flash('Видео не загружено!')
        else:
            fileName = secure_filename(file.filename)
            file.save((os.path.join(app.config['UPLOAD_FOLDER'], fileName)))
            file.save((os.path.join('./', fileName)))
    return render_template('index.html')


@app.route('/render', methods=['POST'])
def render():
    if request.method == 'POST':
        cutJson = request.json
        data = cutJson['framesToCut']
        fileName = r'*.mp4'
        file = glob.glob(fileName)[0]
        editor = VideoEdit(file)
        time1, time2 = 0, 0
        for item in data:
            time1, time2 = item[0] // FRAME_RATE, item[1] // FRAME_RATE
        editor.trim_video(time1, time2)
        editor.render()
    return render_template('return.html', ret='../output.mp4')



if __name__ == '__main__':
    app.run()
