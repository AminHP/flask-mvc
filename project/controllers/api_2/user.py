# -*- coding: utf-8 -*-

# flask imports
from flask import jsonify

# project imports
from project import app


@app.api_route('')
def get():
    """
    Get user info
    Returns baby knight2
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
              description: knight2
    """
    return jsonify(baby='knight2'), 200


@app.api_route('', methods=['POST'])
@app.api_validate('user.signup')
#@app.validate('api_2.user.signup')
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
        description: username, email and password for signup
        required: true
        schema:
          id: Signup
          required:
            - username
            - email
            - password
          properties:
            username:
              type: string
              pattern: ^[a-zA-Z0-9_]+$
              example: babyknight
            email:
              type: string
              example: baby@knight.com
            password:
              type: string
              example: baby123
              minLength: 5
    responses:
      201:
        description: Created
      400:
      	description: Bad request
    """
    return '', 201
