import os
import VisionAPIDemo
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = r'VisionAPIDemo/Images/Text'
app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template("home.html")

"""
@app.route('/')
def text_content():
    return VisionAPIDemo.text()
"""

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    uploaded_file = request.files['file']
    file_name()
    if uploaded_file.filename != '':
        #uploads to images folder
        uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(uploaded_file.filename)))
        text = VisionAPIDemo.text()
        displaytext = "Your file says the following:"
        return render_template("home.html",text=text, displaytext = displaytext)
    else:
        displaytext = "Please make sure you have submitted an image file (.jpg, .png)."
        return render_template("home.html", displaytext = displaytext)
    ##return redirect(url_for('home'))

def file_name():
    file_name = request.files['file']
    return file_name.filename

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)