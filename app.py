from flask import (
    Blueprint, Flask, flash, redirect, render_template, request, url_for
)
from waitress import serve
from .model import is_hotdog
import os

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config["CACHE_TYPE"] = "null"

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.context_processor
def inject_git_sha():
    return dict(sha=os.environ.get('GIT_HASH', 'none'))



base = Blueprint('base', __name__, template_folder='templates')
# A simple landing page
@base.route('/')
def index():
    return render_template('index.html')

# Page presenting results and option to try again
@base.route('/result', methods=['GET','POST'])
def hotdog_result():
	# Redirect back to landing page if nothing was submitted
    if 'file' not in request.files:
        flash('No file uploaded')
        return redirect(url_for("index"))
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for("index"))

    if is_hotdog(file):
        result = "✅ hotdog"
    else:
        result = "❌ not hotdog"

    return render_template('result.html', result = result)
                           
if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000, url_scheme='https')
 	# app.run()