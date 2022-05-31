import json
from flask import request
from model.Answer import Answer
from model.Question import Question
from utils import getRequest, sendRequest

"""
Fonction utilitaire pour update une liste de questions en y ajoutant une question et en faisant les update
"""


def insertQuestion(questionList: list, questionToAdd: Question):
    questionList.insert(questionToAdd.position - 1, questionToAdd)
    for i, question in enumerate(questionList):
        if i == questionToAdd.position - 1:
            continue

        question.position = i + 1

    return questionList


"""
Fonction utilitaire pour supprimer une question d'une liste, et réindexer le tout
"""

def popQuestion(questionList: list, indexToRemove: int):
    questionList.pop(indexToRemove)
    for i, question in enumerate(questionList):
        question.position = i + 1

    return questionList


def getQuestion(pos):
    try:
        pos = int(pos)
    except Exception:
        return {"error": "Position argument in url must be a number"}, 400
    row = getRequest(Question.getSQL(pos))
    if(len(row)) == 0:
        return {"error": "Question not found"}, 404

    question = Question.fromSQLResponse(row[0])

    # On fetch les réponses
    answers = getRequest(question.fetchPossibleAnswersSQL())
    answers = list(map(Answer.fromSQLResponse, answers))
    question.setPossibleAnswers(answers)

    return question.toJSON(), 200


def createQuestion():
    # récupèrer un l'objet json envoyé dans le body de la requète
    question = Question.fromJSON(request.get_json())

    # On récupères toutes les questions pour décaler si besoin
    questions = getRequest(Question.getAllQuestionsSQL())
    questions = list(map(lambda row: Question.fromSQLResponse(row), questions))
    questions.sort(key=lambda q: q.position)

    # Si la position est plus grande que la taille de la liste + 1, on renvoie une erreur
    if question.position <= 0 and question.position > len(questions) + 1:
        return {"error": f"Invalid Position, min=1 and max={len(questions) + 1}"}, 400

    # On verifie si la position est dejà prise, si oui, on decalle
    if len(list(filter(lambda q: q.position == question.position, questions))) != 0:
        # On update les index
        questions = insertQuestion(questions, question)
        for q in questions:
            if q.position != question.position:
                sendRequest(q.updateSQL())

    id = sendRequest(question.insertSQL())
    for answer in question.possibleAnswers:
        answer.questionId = id
        sendRequest(answer.insertSQL())

    return {"status": "OK"}, 200


def updateQuestion(pos):
    # récupèrer un l'objet json envoyé dans le body de la requète
    newQuestion = Question.fromJSON(request.get_json())

    try:
        pos = int(pos)
    except Exception:
        return {"error": "Position argument in url must be a number"}, 400

    row = getRequest(Question.getSQL(pos))
    if(len(row)) == 0:
        return {"error": "Question not found"}, 404

    question = Question.fromSQLResponse(row[0])
    newQuestion._id = question._id

    # Si la position courante et la nouvelle position sont différente, on update les positions des autres questions (osskour)
    if question.position != newQuestion.position:
        # On récupères toutes les questions pour décaler
        questions = getRequest(Question.getAllQuestionsSQL())
        questions = list(
            map(lambda row: Question.fromSQLResponse(row), questions))

        # On vérifie si la nouvelle position est valide
        if newQuestion.position <= 0 and newQuestion.position > len(questions):
            return {"error": f"Invalid Position, min=1 and max={len(questions)}"}, 400

        # On update les positions
        questions.sort(key=lambda q: q.position)
        questions = popQuestion(questions, question.position - 1)
        questions = insertQuestion(questions, newQuestion)

        questions = questions if newQuestion.position > question.position else questions[
            ::-1]
        for q in questions:
            if q.position != newQuestion.position:
                sendRequest(q.updateSQL())

    # On delete toutes les réponses et on les recrées
    sendRequest(question.deletePossibleAnswersSQL())

    # On update la question et les réponses
    sendRequest(newQuestion.updateSQL())
    for answer in newQuestion.possibleAnswers:
        answer.questionId = newQuestion._id
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

    # On vérifie que la question existe bien
    if len(list(filter(lambda q: q.position == pos, questions))) == 0:
        return {"error": "Question not found"}, 404

    try:
        sendRequest(Question.deleteSQL(pos))
    except Exception:
        return {"error": "Unable to delete question"}, 400

    # On update la position des questions après cette question
    questions = popQuestion(questions, pos - 1)
    for q in questions:
        sendRequest(q.updateSQL())

    return {}, 204

def getAllQuestion():
    questions = getRequest(Question.getAllQuestionsSQL())
    questions = list(map(lambda row: Question.fromSQLResponse(row), questions))
    questions.sort(key=lambda q: q.position)

    for question in questions:
        # On fetch les réponses
        answers = getRequest(question.fetchPossibleAnswersSQL())
        answers = list(map(Answer.fromSQLResponse, answers))
        question.setPossibleAnswers(answers)
    
    return json.dumps(questions, default=lambda o: o.__dict__, indent=2), 200