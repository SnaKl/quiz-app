

import json


class Participation():

    def __init__(self, _id: int, playerName: str, score: int):
        self._id = _id
        self.playerName = playerName
        self.score = score
    
    def toJSON(self):
        return json.dumps(self,  default=lambda o: o.__dict__, indent=2)
    
    def toDict(self):
        return {"playerName": self.playerName, "score": self.score}
    
    def fromSQLResponse(row: tuple):
        return Participation(row[0], row[1], row[2])
    
    def insertSQL(self):
        if self._id != -1:
            return f"INSERT INTO Participation(_id, playerName, score) VALUES ({self._id}, \"{self.playerName}\", {self.score});"
        else:
            return f"INSERT INTO Participation(playerName, score) VALUES (\"{self.playerName}\", {self.score});"
    
    def deleteAllSQL():
        return f"DELETE FROM Participation;"
    
    def getAllSQL():
        return f"SELECT * FROM Participation;"
        

Participation.deleteAllSQL = staticmethod(Participation.deleteAllSQL)
Participation.getAllSQL = staticmethod(Participation.getAllSQL)
Participation.fromSQLResponse = staticmethod(Participation.fromSQLResponse)