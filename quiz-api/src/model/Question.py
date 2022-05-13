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

    def insertSQL(self):
        if self._id != -1:
            return f"INSERT INTO Question(_id, position, titre, content, img) VALUES ({self._id}, {self.position}, \"{self.title}\", \"{self.text}\", \"{self.image}\");"
        else:
            return f"INSERT INTO Question(position, titre, content, img) VALUES ({self.position}, \"{self.title}\", \"{self.text}\", \"{self.image}\");"


# On rend statique la méthode fromJSON
Question.fromJSON = staticmethod(Question.fromJSON)
