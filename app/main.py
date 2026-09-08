from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def accueil():
    return {"message": "chocapik!"}

@app.get("/health")
def health():
    return {"status": "online", "game_title": "Votre Titre",
            "engine_version": "1.0.0"}
