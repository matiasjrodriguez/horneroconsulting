from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    import os
    from flask import send_from_directory

    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'Pajaro.ico',mimetype='image/vnd.microsoft.icon')