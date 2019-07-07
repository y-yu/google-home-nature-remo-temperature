#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
import os
import requests
from flask_basicauth import BasicAuth

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = os.getenv('BASIC_AUTH_USERNAME', '')
app.config['BASIC_AUTH_PASSWORD'] = os.getenv('BASIC_AUTH_PASSWORD', '')
app.config['JSON_AS_ASCII'] = False

nature_remo_token = os.getenv('NATURE_REMO_TOKEN')

basic_auth = BasicAuth(app)

@app.route('/temperature', methods=['POST'])
@basic_auth.required
def temprature():
  r = requests.get(
    'https://api.nature.global/1/devices',
    headers = {
      'Authorization': 'Bearer ' + nature_remo_token
    }
  )
  response = {
    'payload': {
      'google': {
        'expectUserResponse': False,
        'richResponse': {
          'items': [
            {
              'simpleResponse': {
                'textToSpeech': '現在の室温は' + str(r.json()[0]['newest_events']['te']['val']) + '度です'
              }
            }
          ]
        }
      }
    }
  }
  return jsonify(response)

if __name__ == "__main__":
  p = os.getenv('PORT', '80')
  app.run(host = '0.0.0.0', port = p, debug = False)
