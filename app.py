from flask import Flask, jsonify, request, send_file
from werkzeug.utils import secure_filename
import urllib.request
import base64

app = Flask(__name__)
UPLOAD_FOLDER = '/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/square/', methods=['POST'])
def square():
    n = request.get_json()['n']
    result = {
        "Number": n,
        "Square": n*n
    }
    return jsonify(result)


@app.route('/image/', methods=['POST'])
def image():
    f1 = request.files.get('image1')
    f1.save(secure_filename(f1.filename))
    f2 = request.files.get('image2')
    f2.save(secure_filename(f2.filename))
    result = {
        "status": "Ok"
    }
    return jsonify(result)


@app.route('/imageUrl/', methods=['POST'])
def imageUrl():
    url1 = request.get_json()['image1']
    url2 = request.get_json()['image2']

    urllib.request.urlretrieve(url1, 'uploads/image1.jpg')
    urllib.request.urlretrieve(url2, 'uploads/image2.jpg')

    # return send_file('result.jpg', as_attachment=False, mimetype="image/jpg")

    with open("result.jpg", "rb") as image_file:
        encoded_string = 'data:image/jpg;base64,' + base64.b64encode(image_file.read()).decode('utf-8')
    
    result = {
        "result": encoded_string
    }

    return jsonify(result)


@app.route("/", methods=['POST'])
def hello_world():
    name = request.get_json()['name']
    return f"<p>Hello, World! {name}</p>"
