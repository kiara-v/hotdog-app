from flask import (
    Blueprint, Flask, flash, redirect, render_template, request, url_for
)

import model

app = Flask(__name__)
server_address = "http://kiaravong.pythonanywhere.com"

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
 	app.run()