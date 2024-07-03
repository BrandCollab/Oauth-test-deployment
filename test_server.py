from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/auth/success', methods=['GET'])
def auth_success():
    return jsonify({"message": "Authentication successful!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
