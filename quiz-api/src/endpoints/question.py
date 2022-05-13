from msilib.schema import Error
import sqlite3
from flask import request
from jwt_utils import JwtError, decode_token
from model.Question import Question

def createQuestion():
    #Récupérer le token envoyé en paramètre
    token = request.headers.get('Authorization')

    #On check si le token est valide
    #TODO: Mettre dans un middleware
    try:
        decode_token(token.removeprefix("Bearer "))
    except JwtError as err:
        return {"error": err.message}, 401

    #récupèrer un l'objet json envoyé dans le body de la requète
    question = Question.fromJSON(request.get_json())

    #création d'un objet connection
    db_connection = sqlite3.connect("db/db.db")
    # set the sqlite connection in "manual transaction mode"
    # (by default, all execute calls are performed in their own transactions, not what we want)
    db_connection.isolation_level = None

    #On l'insert en base de données
    cursor = db_connection.cursor()

    # start transaction
    cursor.execute("begin")

    try:
        # save the question to db
        cursor.execute(question.insertSQL())

        #send the request
        cursor.execute("commit")
    except Exception as err:
        #in case of exception, roolback the transaction
        cursor.execute('rollback')
        return {"error": str(err)}, 500

    return question.toJSON(), 200