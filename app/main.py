from webbrowser import get

from domain.enigme import Enigme1, Enigme2, Enigme3, Enigme4, Enigme5, Enigme6, Enigme7, Enigme8, Enigme11, Enigme12, Enigme13, Enigme14, Enigme15, Enigme16, Enigme17, Enigme21, Enigme22, Enigme23, Enigme24, Enigme25, Enigme26
from domain.enigme import Door1, Door2, Door3
from fastapi import FastAPI

app = FastAPI()
i = 1
y = 1

while i <= 26:
    if i == 9:
        i = 11
    elif i == 17:
        i = 21

    @app.get(f"/Enigme{i}/question")
    def enigme_question(i=i):
        enigme = globals()[f"Enigme{i}"]
        return {
            "question": enigme.question,
        }

    @app.get(f"/Enigme{i}/reponse")
    def enigme_reponse(i=i):
        enigme = globals()[f"Enigme{i}"]
        return {
            "reponse": enigme.reponse,
        }

    @app.get(f"/Enigme{i}/indice")
    def enigme_indice(i=i):
        enigme = globals()[f"Enigme{i}"]
        return {
            "indice": enigme.indice,
        }

    @app.get(f"/Enigme{i}/lettre")
    def enigme_lettre(i=i):
        enigme = globals()[f"Enigme{i}"]
        return {
            "lettre": enigme.lettre,
        }
    i = i + 1

while y <= 3:
    @app.get(f"/Door{y}/question")
    def door_question(y=y):
        door = globals()[f"Door{y}"]
        return {
            "question": door.question,
        }

    @app.get(f"/Door{y}/reponse")
    def door_reponse(y=y):
        door = globals()[f"Door{y}"]
        return {
            "reponse": door.reponse,
        }

    @app.get(f"/Door{y}/indice1")
    def door_indice1(y=y):
        door = globals()[f"Door{y}"]
        return {
            "indice1": door.indice,
        }

    @app.get(f"/Door{y}/indice2")
    def door_indice2(y=y):
        door = globals()[f"Door{y}"]
        return {
            "indice2": door.indice2,
        }
    y = y + 1

@app.get("/health")
def health():
    return {"status": "online", "game_title": "Votre Titre",
            "engine_version": "1.0.0"}
