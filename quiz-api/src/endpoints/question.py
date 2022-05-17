from flask import request
from jwt_utils import JwtError, decode_token
from model.Answer import Answer
from model.Question import Question
from utils import getRequest, sendRequest

def getQuestion(pos):
    try:
        pos = int(pos)
    except Exception:
        return {"error": "Position argument in url must be a number"}, 400
    row = getRequest(Question.getSQL(pos))
    if(len(row)) == 0:
        return {"error": "Question not found"}, 404

    question = Question.fromSQLResponse(row[0])
    answers = getRequest(question.fetchPossibleAnswersSQL())
    answers = list(map(Answer.fromSQLResponse, answers))
    question.setPossibleAnswers(answers)

    return question.toJSON(), 200

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
    

    id = sendRequest(question.insertSQL())
    for answer in question.possibleAnswers:
        answer.questionId = id
        sendRequest(answer.insertSQL())

    return {"status": "OK"}, 200

def deleteQuestion(pos):
    try:
        pos = int(pos)
    except Exception:
        return {"error": "Position argument in url must be a number"}, 400

    questions = getRequest(Question.getAllQuestionsSQL())
    questions = list(map(lambda row: Question.fromSQLResponse(row), questions))
    questions.sort(key=lambda q: q.position)
    questions = questions[pos:]

    try:
        sendRequest(Question.deleteSQL(pos))
    except Exception:
        return {"error": "Unable to delete question"}, 400

    #On update la position des questions après cette question
    for q in questions:
            q.position -= 1
            
            #On Update en BDD
            sendRequest(q.updateSQL())

    return {}, 204
