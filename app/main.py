from webbrowser import get

from domain.enigme import Enigme1, Enigme2, Enigme3, Enigme4, Enigme5, Enigme6, Enigme7, Enigme8, Enigme11, Enigme12, Enigme13, Enigme14, Enigme15, Enigme16, Enigme17, Enigme21, Enigme22, Enigme23, Enigme24, Enigme25, Enigme26
from domain.enigme import Door1, Door2, Door3
from fastapi import FastAPI

import hashlib

def hash_sha256(texte):
    return hashlib.sha256(texte.encode()).hexdigest()

enigmes = {
    1: Enigme1,
    2: Enigme2,
    3: Enigme3,
    4: Enigme4,
    5: Enigme5,
    6: Enigme6,
    7: Enigme7,
    8: Enigme8,
    11: Enigme11,
    12: Enigme12,
    13: Enigme13,
    14: Enigme14,
    15: Enigme15,
    16: Enigme16,
    21: Enigme21,
    22: Enigme22,
    23: Enigme23,
    24: Enigme24,
    25: Enigme25,
    26: Enigme26,
}

doors = {
    1: Door1,
    2: Door2,
    3: Door3,
}

app = FastAPI()
i = 1
y = 1

while i <= 26:
    if i == 9:
        i = 11
    elif i == 17:
        i = 21

    @app.get("/Enigme{i}/question")
    def enigme_question(i: int):
        enigme = enigmes.get(i)
        if enigme is None:
            return {"erreur": "Enigme introuvable"}
        return {"question": enigme.question}

    @app.get("/Enigme{i}/indice")
    def enigme_indice(i: int):
        enigme = enigmes.get(i)
        if enigme is None:
            return {"erreur": "Enigme introuvable"}
        return {"indice": enigme.indice}

    @app.get("/Enigme{i}/lettre")
    def enigme_lettre(i: int):
        enigme = enigmes.get(i)
        if enigme is None:
            return {"erreur": "Enigme introuvable"}
        return {"lettre": enigme.lettre}

    @app.get("/Enigme{i}/reponse")
    def enigme_reponse(i: int, tentative: str):
        enigme = enigmes.get(i)
        if enigme is None:
            return {"erreur": "Enigme introuvable"}

        if hash_sha256(tentative.upper()) == enigme.reponse:
            return {"correct": True, "message": "Félicitations ! Vous avez trouvé la bonne réponse. Vous obtenez la lettre : " + enigme.lettre}
        return {"correct": False, "message": "Désolé, ce n'est pas la bonne réponse."}
    i = i + 1

while y <= 3:
    @app.get("/Door{i}/question")
    def door_question(i: int):
        door = doors.get(i)
        if door is None:
            return {"erreur": "Door introuvable"}
        return {"question": door.question}

    @app.get("/Door{i}/reponse")
    def door_reponse(i: int, tentative: str):
        door = doors.get(i)
        if door is None:
            return {"erreur": "Door introuvable"}
        if hash_sha256(tentative.upper()) == door.reponse:
            door.solved = True
            return {"correct": True, "message": "Félicitations ! Vous avez trouvé la bonne réponse pour la porte " + str(i) + ". Vous pouvez maintenant déverrouiller la porte."}
        return {"correct": False, "message": "Désolé, ce n'est pas la bonne réponse pour la porte " + str(i) + "."}

    @app.get("/Door{i}/indice")
    def door_indice(i: int):
        door = doors.get(i)
        if door is None:
            return {"erreur": "Door introuvable"}
        return {"indice": door.indice}

    @app.get("/Door{i}/indice2")
    def door_indice2(i: int):
        door = doors.get(i)
        if door is None:
            return {"erreur": "Door introuvable"}
        return {"indice2": door.indice2}
    @app.get("/Door{i}/unlock")
    def door_unlock(i: int):
        door = doors.get(i)
        if door is None:
            return {"erreur": "Door introuvable"}

        if door.solved:
            door.locked = False
            return {"message": "La porte est maintenant déverrouillée."}
        return {"message": "Vous devez résoudre l'énigme pour déverrouiller la porte."}
    y = y + 1

@app.get("/health")
def health():
    return {"status": "online", "game_title": "Votre Titre",
            "engine_version": "1.0.0"}
