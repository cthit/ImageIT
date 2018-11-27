import os
import uuid
import config
from datetime import datetime

from flask import Flask, flash, request, redirect, url_for, send_from_directory
from pony.orm import Database, PrimaryKey, Required

db = Database()
db.bind(
    provider='postgres',
    user=config.POSTGRES_USER,
    password=config.POSTGRES_PASSWORD,
    host=config.POSTGRES_HOST,
    database=config.POSTGRES_DB
)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = config.IMAGE_FOLDER

if not os.path.exists(config.IMAGE_FOLDER):
    raise (Exception('Directory not found: "%s"\n'
                     'Create the directory or change "config.py"' % config.IMAGE_FOLDER))


class Image(db.Entity):
    imageid = PrimaryKey(uuid, auto=True)
    imagelink = Required(str)
    userid = Required(uuid, auto=True)
    uploadtime = Required(datetime, auto=True)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in config.ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return redirect(url_for('uploaded_file', filename=file.filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run()
