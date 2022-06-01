import json

from src.model.Answer import Answer


class Question():

    def __init__(self, _id: int, position: int, title: str, text: str, image: str):
        self._id = _id
        self.position = position
        self.title = title
        self.text = text
        self.image = image
        # On ne les fetch pas par défaut
        self.possibleAnswers = []
    
    def setPossibleAnswers(self, possibleAnswers):
        self.possibleAnswers = possibleAnswers 

    def fetchPossibleAnswersSQL(self):
        return f"SELECT * FROM Answer WHERE questionId = {self._id};"
    
    def deletePossibleAnswersSQL(self):
        return f"DELETE FROM Answer WHERE questionId = {self._id};"

    def toJSON(self):
        return json.dumps(self,  default=lambda o: o.__dict__, indent=2)

    def fromJSON(json: dict):
        if "_id" in json:
            _id = json["_id"]
        position = json["position"]
        title = json["title"]
        text = json["text"]
        image = json["image"]

        question = None
        if "_id" in json:
            question = Question(_id, position, title, text, image)
        else:
            question = Question(-1, position, title, text, image)
        
        #On parse les réponses
        reponses = []
        for answer in json["possibleAnswers"]:
            reponses.append(Answer.fromJSON(answer, question._id))

        question.setPossibleAnswers(reponses)

        return question
    
    def fromSQLResponse(row: tuple):
        return Question(row[0], row[1], row[2], row[3], row[4])


    def insertSQL(self):
        if self._id != -1:
            return f"INSERT INTO Question(_id, position, title, text, image) VALUES ({self._id}, {self.position}, \"{self.title}\", \"{self.text}\", \"{self.image}\");"
        else:
            return f"INSERT INTO Question(position, title, text, image) VALUES ({self.position}, \"{self.title}\", \"{self.text}\", \"{self.image}\");"

    def updateSQL(self):
        return f"UPDATE Question SET position={self.position}, title=\"{self.title}\", text=\"{self.text}\", image=\"{self.image}\" WHERE _id={self._id};"
    
    def deleteSQL(position: int):
        return f"DELETE FROM Question WHERE position = {position};"
    
    def getSQL(position: int):
        return f"SELECT * FROM Question WHERE position = {position};"

    def getAllQuestionsSQL():
        return "SELECT * FROM Question;"

# On rend statique des méthodes
Question.fromJSON = staticmethod(Question.fromJSON)
Question.getAllQuestionsSQL = staticmethod(Question.getAllQuestionsSQL)
Question.fromSQLResponse = staticmethod(Question.fromSQLResponse)
Question.deleteSQL = staticmethod(Question.deleteSQL)
Question.getSQL = staticmethod(Question.getSQL)

