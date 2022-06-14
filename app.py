from flask import (
    Blueprint, Flask, flash, redirect, render_template, request, url_for
)

from model import is_hotdog

base = Blueprint('base', __name__, template_folder='templates')

# A simple landing page
@base.route('/')
def index():
    return render_template('index.html')
    # base_page_html = f"""
    # <html>
    #    <body>
    #     <h1>Hot dog? Or not...</h1>
    #     Upload your image here:
    #       <form action="{server_address}/result" method="POST" 
    #          enctype="multipart/form-data">
    #          <input type="file" name="file" />
    #          <input type="submit"/>
    #       </form>
    #    </body>
    # </html>
    # """
    # return base_page_html

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