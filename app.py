from flask import Flask
from flask import render_template

app = Flask(__name__, static_folder='static')
app.config['UPLOAD_FOLDER'] = 'media'


@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
