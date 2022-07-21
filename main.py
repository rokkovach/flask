from flask import Flask, request, jsonify
import os
import requests
import json

app = Flask(__name__)


@app.route("/", methods=['POST'])
def encode_url():
    data = json.loads(request.data)
    payload = {"text" : f"{data['text']"}
    headers = {'Content-Type': 'application/json'}
    r = requests.post(f"{data['url']", headers=headers, data=json.dumps(payload))
    return json.loads(r.text)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
