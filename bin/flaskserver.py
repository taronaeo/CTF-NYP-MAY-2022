#! /usr/bin/env python3

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def root():
  print(request.form)
  return jsonify(success=True)

if __name__ == '__main__':
  app.run(debug=True)
