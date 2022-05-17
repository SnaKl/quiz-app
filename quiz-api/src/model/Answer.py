import json


class Answer():

    def __init__(self, _id: int, text: str, isCorrect: bool, questionId: int):
        self._id = _id
        self.text = text
        self.isCorrect = isCorrect
        self.questionId = questionId

    def toJSON(self):
        return json.dumps(self,  default=lambda o: o.__dict__, indent=2)

    def fromJSON(json: dict, questionId: int):
        if "_id" in json:
            _id = json["_id"]
        text = json["text"]
        isCorrect = json["isCorrect"]

        if "_id" in json:
            return Answer(_id, text, isCorrect, questionId)
        else:
            return Answer(-1, text, isCorrect, questionId)
    
    def fromSQLResponse(row: tuple):
        return Answer(row[0], row[1], bool(row[2]), row[3])

    def insertSQL(self):
        if self._id != -1:
            return f"INSERT INTO Answer(_id, text, isCorrect, questionId) VALUES ({self._id}, \"{self.text}\", {1 if self.isCorrect else 0}, {self.questionId});"
        else:
            return f"INSERT INTO Answer(text, isCorrect, questionId) VALUES (\"{self.text}\", {1 if self.isCorrect else 0}, {self.questionId});"

    def getAllAnswersSQL():
        return "SELECT * FROM Answer;"

# On rend statique des méthodes
Answer.fromJSON = staticmethod(Answer.fromJSON)
Answer.getAllAnswersSQL = staticmethod(Answer.getAllAnswersSQL)
Answer.fromSQLResponse = staticmethod(Answer.fromSQLResponse)

