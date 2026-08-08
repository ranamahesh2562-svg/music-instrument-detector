from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Music Instrument Detector is Running!"

@app.route('/predict', methods=['POST'])
def predict():
    # यहाँ आप बाद में अपना मॉडल लोड करके प्रेडिक्शन का लॉजिक जोड़ सकते हैं
    return jsonify({'status': 'success', 'message': 'Instrument Detection Model'})

if __name__ == '__main__':
    app.run(debug=True)
