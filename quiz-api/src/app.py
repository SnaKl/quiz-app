from urllib.request import Request
from flask import Flask, request
from flask_cors import CORS
from endpoints.participation import createParticipation, deleteAllParticipations
import jwt_utils as jwtu
from endpoints.question import createQuestion, deleteQuestion, getQuestion, updateQuestion
from model.Participation import Participation
from model.Question import Question
from utils import getRequest, secured_endpoint

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    x = 'world'
    return f"Hello, {x}"


@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
    particpipations = list(map(lambda part: Participation.fromSQLResponse(
        part).toDict(), getRequest(Participation.getAllSQL())))
    particpipations.sort(
        key=lambda participation: participation["score"], reverse=True)
    return {"size": len(getRequest(Question.getAllQuestionsSQL())), "scores": particpipations}, 200


@app.route('/login', methods=['POST'])
def login():
    payload = request.get_json()

    # On vérifie si le password est set
    if "password" in payload:
        password = payload["password"]
    else:
        return {"error": "You must specify a body with the 'password' field"}, 400

    # si oui, on vérifie qu'il correspond au mdp attendu
    # TODO: Mettre ça dans une variable d'environnement !
    if password == "Vive l'ESIEE !":
        # On génère un token
        token = jwtu.build_token()
        return {"token": token}, 200

    return {"error": "Invalid Password"}, 401


"""
SECTION QUESTIONS
"""


@app.route('/questions/<pos>', methods=['GET'])
def get_question(pos):
    return getQuestion(pos)


@app.route('/questions', methods=['POST'])
@secured_endpoint
def post_question():
    return createQuestion()


@app.route('/questions/<pos>', methods=['DELETE'])
@secured_endpoint
def delete_question(pos):
    return deleteQuestion(pos)


@app.route('/questions/<pos>', methods=['PUT'])
@secured_endpoint
def update_question(pos):
    return updateQuestion(pos)


"""
SECTION REPONSES
"""


@app.route('/participations', methods=['POST'])
def addParticipation():
    return createParticipation()


@app.route('/participations', methods=['DELETE'])
@secured_endpoint
def deleteParticipations():
    return deleteAllParticipations()


if __name__ == "__main__":
    app.run()
