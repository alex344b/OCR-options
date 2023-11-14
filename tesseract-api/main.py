from flask import Flask, request, render_template, redirect
from werkzeug.utils import secure_filename
from files import background_task
from db import selectAll

app = Flask(__name__)

print('Started server')


@app.post('/upload')
def uploadImage():
    if 'files' not in request.files:
        return "No files in request", 400
    file = request.files['files']
    if file.filename == '':
        return "No file provided", 400
    if file:
        filename = secure_filename(file.filename)
        file.save('./files/' + filename)
        background_task(filename)
        return redirect(request.url_root)


@app.get('/')
def uploadForm():
    return render_template('upload.html')


@app.get('/invoces')
def invoces():
    return selectAll()
