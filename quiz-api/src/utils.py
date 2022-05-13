from functools import wraps
import sqlite3
from flask import jsonify, make_response, request
import jwt
from jwt_utils import JwtError, decode_token

# Authentication decorator
def secured_endpoint(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        #Récupérer le token envoyé en paramètre
        token = request.headers.get('Authorization')

        if token is None:
            return make_response(jsonify({"error": "You need to specify the token with the Authorization Header"}), 401)
        #On check si le token est valide
        try:
            decode_token(token.removeprefix("Bearer "))
        except JwtError as err:
            return make_response(jsonify({"error": err.message}), 401)

         # Return the user information attached to the token
        return f(*args, **kwargs)
    return decorator

def getConnection():
    #création d'un objet connection
    db_connection = sqlite3.connect("db/db.db")
    # set the sqlite connection in "manual transaction mode"
    # (by default, all execute calls are performed in their own transactions, not what we want)
    db_connection.isolation_level = None

    return db_connection

def sendRequest(sqlRequest):
    db_connection = getConnection()

    #On l'insert en base de données
    cursor = db_connection.cursor()

    # start transaction
    cursor.execute("begin")

    try:
        # save the question to db
        cursor.execute(sqlRequest)

        #send the request
        cursor.execute("commit")
    except Exception as err:
        #in case of exception, roolback the transaction
        cursor.execute('rollback')
        raise err

def getRequest(sqlRequest):
    db_connection = getConnection()

    #On l'insert en base de données
    cursor = db_connection.cursor()

    cursor.execute(sqlRequest)

    return cursor.fetchall()
