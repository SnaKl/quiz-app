from flask import request
from model.Answer import Answer
from model.Participation import Participation
from model.Question import Question
from utils import getRequest, sendRequest


def createParticipation():
    # récupèrer un l'objet json envoyé dans le body de la requète
    participationJSON = request.get_json()
    participation = Participation(-1, participationJSON["playerName"], 0)

    # On récupères toutes les questions pour vérifier les réponses
    questions = getRequest(Question.getAllQuestionsSQL())
    questions = list(map(lambda row: Question.fromSQLResponse(row), questions))
    questions.sort(key=lambda q: q.position)

    if len(participationJSON["answers"]) != len(questions):
        return {"error": f"You didn't answer to all question !"}, 400

    # on fetch les réponses
    for question in questions:
        answers = getRequest(question.fetchPossibleAnswersSQL())
        answers = list(map(Answer.fromSQLResponse, answers))
        question.setPossibleAnswers(answers)

    # on updates le score
    print(participationJSON["answers"])
    for i, answer in enumerate(participationJSON["answers"]):
        if questions[i].possibleAnswers[answer - 1].isCorrect:
            participation.score += 1
    

    #on insert en bdd
    sendRequest(participation.insertSQL())
    return participation.toJSON(), 200
    
def deleteAllParticipations():
    sendRequest(Participation.deleteAllSQL())
    return {"status": "OK"}, 204
