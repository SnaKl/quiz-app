# Quiz APP

[![CI - Test de l'API](https://github.com/SnaKl/quiz-app/actions/workflows/test-api.yml/badge.svg)](https://github.com/SnaKl/quiz-app/actions/workflows/test-api.yml)

Application Web de quizz développé dans le cadre de l'unité Web Full Stack

## Notes
Notre base de données n'est pas historisé, en effet, nous avons mis en place un mécanisme simple permettant de la recréer (accompagné de son schéma SQL) au lancement de l'application lorsque celle-ci n'est pas présente.

## Utilisation
Pour lancer le serveur, installez les dépendances avec:
`python -m pip install -r quiz-api/requirements.txt`
Puis lancez le serveur avec la commande avec:
`python quiz-api/src/app.py`

## Docker
Le projet est également fourni avec deux docker, un pour l'api et un pour le front-end.

### Build
Pour l'api, il suffit d'éxécuter la commande : `docker build -f docker/api-Dockerfile -t quiz-api:latest .` en étant à la racine du projet.
Pour ce qui est de l'ui: `docker build -f docker/ui-Dockerfile -t quiz-ui:latest .`

### Run
Pour l'api, il suffit d'utiliser la commande: `docker run -p 8080:5000 --name quiz-api -d quiz-api` (ou 8080 est le port sur la host machine).
Pour ce qui est de l'ui, c'est similaire : `docker run -p 80:80 --name quiz-ui -d quiz-ui` (ou le premier 80 est le port sur la host machine).