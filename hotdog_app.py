from flask import (
    Flask, flash, redirect, render_template, request
)

from . import model
from waitress import serve
import os

app = Flask(__name__)
server_address = "http://127.0.0.1:5000"

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config["CACHE_TYPE"] = "null"

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.context_processor
def inject_git_sha():
    return dict(sha=os.environ.get('GIT_HASH', 'none'))

# A simple landing page
@app.route('/')
def index():
    return render_template('index.html', server_address = server_address)

# Page presenting results and option to try again
@app.route('/result', methods=['GET','POST'])
def hotdog_result():
	# Redirect back to landing page if nothing was submitted
    if 'file' not in request.files:
        flash('No file uploaded')
        return redirect(f'{server_address}/')
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(f'{server_address}/')

    if model.is_hotdog(file):
        result = "✅ hotdog"
    else:
        result = "❌ not hotdog"

    return render_template('result.html', result = result, server_address = server_address)

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000, url_scheme='https')
 	# app.run()