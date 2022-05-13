from flask import Flask, request
import jwt_utils as jwtu
from endpoints.question import createQuestion
from utils import secured_endpoint

app = Flask(__name__)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

@app.route('/login', methods=['POST'])
def login():
    payload = request.get_json()

    #On vérifie si le password est set
    if "password" in payload:
        password = payload["password"]
    else:
        return {"error": "You must specify a body with the 'password' field"}, 400
    
    #si oui, on vérifie qu'il correspond au mdp attendu
    #TODO: Mettre ça dans une variable d'environnement !
    if password == "Vive l'ESIEE !":
        #On génère un token
        token = jwtu.build_token()
        return {"token": token}, 200
    
    return {"error": "Invalid Password"}, 401

@app.route('/questions', methods=['POST'])
@secured_endpoint
def post_question():
    return createQuestion()

if __name__ == "__main__":
    app.run(ssl_context='adhoc')