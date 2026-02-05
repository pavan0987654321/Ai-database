"""Minimal test Flask app to verify Render deployment works"""
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return {'status': 'ok', 'message': 'Test app is running!'}

@app.route('/health')
def health():
    return {'status': 'healthy'}

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
