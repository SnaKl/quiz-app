import json


class Question():

    def __init__(self, _id: int, position: int, title: str, text: str, image: str):
        self._id = _id
        self.position = position
        self.title = title
        self.text = text
        self.image = image

    def toJSON(self):
        return json.dumps(self,  default=lambda o: o.__dict__, indent=2)

    def fromJSON(json: dict):
        if "_id" in json:
            _id = json["_id"]
        position = json["position"]
        title = json["title"]
        text = json["text"]
        image = json["image"]

        if "_id" in json:
            return Question(_id, position, title, text, image)
        else:
            return Question(-1, position, title, text, image)
    
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

