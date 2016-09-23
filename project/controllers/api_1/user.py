# -*- coding: utf-8 -*-

# flask imports
from flask import jsonify

# project imports
from project import app


@app.api_route('')
def get():
    """
    Get user info
    Returns baby knight
    ---
    tags:
      - user
    responses:
      200:
        description: User info
        schema:
          id: UserInfo
          type: object
          properties:
            baby:
              type: string
              description: knight
    """
    return jsonify(baby='knight'), 200


@app.api_route('', methods=['POST'])
@app.api_validate('user.signup')
#@app.validate('api_1.user.signup')
def signup():
    """
    Signup
    ---
    tags:
      - user
    parameters:
      - name: body
        in: body
        type: object
        description: username and password for signup
        required: true
        schema:
          id: Signup
          required:
            - username
            - password
          properties:
            username:
              type: string
              description: username of user
            password:
              type: string
              description: password of user
    responses:
      201:
        description: Created
      400:
      	description: Bad request
    """
    return '', 201
