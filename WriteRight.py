from flask import Flask, jsonify, request
import easyocr
import os  

app = Flask(__name__)
reader = easyocr.Reader(['en'])

@app.route('/')
def home():
    return "Welcome to the WriteRight app!"

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    image_file = request.files['image']
    result = reader.readtext(image_file)
    recognized_text = [text[1] for text in result]
    
    return jsonify({"recognized_text": recognized_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))  # Render uses the PORT environment variable
