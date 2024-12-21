from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/generate-report', methods=['POST'])
def generate_report():
    # Here you can add logic to process the uploaded file if needed
    # For now, we will just return a simple message
    report_message = "Hello Madarchod!"
    
    return jsonify({'message': report_message})

if __name__ == '__main__':
    app.run(host='192.168.106.65', port=8000)