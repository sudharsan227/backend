from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



# Configuration for uploads
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload-image', methods=['POST'])
def upload_image():
    print(request.headers)
    print(request.files)
    print("hi")
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(save_path)
        return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 200
    else:
        return jsonify({'error': 'File type not allowed'}), 400

@app.route('/translate-text', methods=['POST'])
def translate_text():
    print("hiiiii")
    data = request.get_json()
    original_text = data.get('text', '')
    # Placeholder for translation logic. In a real app, you might use an external API or library for this.
    translated_text = f"Translated version of: {original_text}"
    return jsonify({'originalText': original_text, 'translatedText': translated_text})

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)