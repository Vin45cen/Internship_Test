import ollama
from flask import Flask, jsonify, request

app = Flask(__name__)

def generate(prompt):
    response = ollama.generate(model='llama3.2', prompt=prompt)
    return response

@app.route('/inference', methods=['POST'])

def inference():
    data = request.get_json()

    if 'prompt' not in data:
        return jsonify({'Error': 'Please include "prompt" key in payload data'}), 400
    else:
        prompt = data['prompt']

    try:
        response = generate(prompt)
        return jsonify({'Response': response['response']}), 200
    except Exception as e:
        return jsonify({'Error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)