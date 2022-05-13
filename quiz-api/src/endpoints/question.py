from msilib.schema import Error
from flask import request
from jwt_utils import JwtError, decode_token
from model.Question import Question
from utils import getRequest, sendRequest

def createQuestion():
    #récupèrer un l'objet json envoyé dans le body de la requète
    question = Question.fromJSON(request.get_json())

    #On récupères toutes les questions pour décaler si besoin
    questions = getRequest(Question.getAllQuestionsSQL())
    questions = list(map(lambda row: Question.fromSQLResponse(row), questions))
    
    #Si la position est plus grande que la taille de la liste + 1, on renvoie une erreur
    if question.position <= 0 and question.position > len(questions) + 1:
        return {"error": f"Invalid Position, min=1 and max={len(questions) + 1}"}, 400

    #On verifie si la position est dejà prise, si oui, on decalle
    if len(list(filter(lambda q: q.position == question.position, questions))) != 0:
        #On décalle tous les questions de +1 pour placer cette question à la place
        for q in questions:
            if q.position >= question.position:
                q.position += 1
            
            #On Update en BDD
            sendRequest(q.updateSQL())

    sendRequest(question.insertSQL())

    return {"status": "OK"}, 200
