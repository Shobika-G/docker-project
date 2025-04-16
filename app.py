from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# ✅ Add this route to serve the login page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Dummy check for now
    if username == "admin" and password == "admin":
        return jsonify({'message': 'Login Successful'}), 200
    else:
        return jsonify({'message': 'Invalid Credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True)
