CREATE TABLE IF NOT EXISTS "Question" (
	"_id"	INTEGER NOT NULL UNIQUE,
	"position"	INTEGER NOT NULL,
	"title"	TEXT NOT NULL,
	"text"	TEXT NOT NULL,
	"image"	TEXT,
	PRIMARY KEY("_id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "Answer" (
	"_id"	INTEGER NOT NULL UNIQUE,
	"text"	TEXT NOT NULL,
	"isCorrect"	INTEGER NOT NULL,
    "questionId" INTEGER NOT NULL,
	PRIMARY KEY("_id" AUTOINCREMENT),
    FOREIGN KEY("questionId") REFERENCES "Question"("_id") ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS "Participation" (
	"_id"	INTEGER NOT NULL UNIQUE,
	"playerName" VARCHAR(255) NOT NULL,
	"score"	INTEGER NOT NULL,
	PRIMARY KEY("_id" AUTOINCREMENT)
);