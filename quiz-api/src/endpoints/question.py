from msilib.schema import Error
from flask import request
from jwt_utils import JwtError, decode_token
from model.Question import Question
from utils import sendRequest

def createQuestion():
    #récupèrer un l'objet json envoyé dans le body de la requète
    question = Question.fromJSON(request.get_json())

    sendRequest(question.insertSQL())

    return question.toJSON(), 200