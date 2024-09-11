from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Hello, World!'})

@app.route('/sum/<int:a>/<int:b>')
def sum_numbers(a, b):
    return jsonify({'result': a + b})

if __name__ == '__main__':
    app.run(debug=True)
