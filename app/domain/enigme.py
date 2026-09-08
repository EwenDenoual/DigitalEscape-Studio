from .classes import Enigme
from .classes import Door

import hashlib

def hash_sha256(texte):
    return hashlib.sha256(texte.encode()).hexdigest()


Enigme1 = Enigme ( "Quel pokemon est celui qui possede le plus de formes evolutives ?",
                   hash_sha256("EVOLIE"), 
                   "Son nom est lie a l'evolution et il est de type normal", 
                   "E" )

Enigme2 = Enigme ( "Parmi les pokemons suivants, lequel ne peut pas etre considere comme le premier ? " + "\n" + " a) ARCEUS" + " b) RHINOFEROS" + " c) BULBIZARRE" + " d) NOEUNEUF",
                   hash_sha256("NOEUNEUF"),
                   "Il est de type Plante",
                   "N" )

Enigme3 = Enigme ( " Quel est le pokemon le plus fort du metagame 6v6 1g ?" + "\n" + " a) TAUROS" + " b) DRACOLOSE" + " c) ALAKAZAM" + " d) MACKOGNEUR",
                  hash_sha256("TAUROS"),
                  "Il possede 3 formes regionales a Paldea",
                  "T" )

Enigme4 = Enigme ( "Parmi les pokemons suivants, lequel est le plus lourd ?" + "\n" + " a) PRIMO-GROUDON" + " b) DIANCIE" + " c) COSMOVUM" + " d) RONFLEX",
                  hash_sha256("COSMOVUM"),
                  "Dans les jeux et l'anime, Lili lui a donne le surnom 'doudou'",
                  "C" )

Enigme5 = Enigme ( "En 9g Raikou obtien une forme du passé quel est son nom ?" + "\n" + " a) PETIT-TONNAIRE" + " b) IRE-FOUDRE" + " c) VIEIL-ECLAIRE" + " d) VIOLET-ORAGE", 
                  hash_sha256("IRE-FOUDRE"),
                  "Il est lier a l'attaque Fatale Foudre",
                  "I" )

Enigme6 = Enigme ( "Quel est le pokemon phare du deck si domminant qu'il etait le seul present lors des final TCG 2026 ?",
                  hash_sha256("LANSSORIEN"),
                  "Son attaque signature consiste a lancer ses enfants sur l'adversaire",
                  "L" )

Enigme7 = Enigme ( "Quel est le seul pokemon a avoir une forme cree par l'anime?",
                  hash_sha256("AMPHINOBI"),
                  "Il s'agit d'un ninja",
                  "A" )

Enigme8 = Enigme ( "Quel pokemon completement evolue ne possede techniquement aucune faiblesse ?",
                  hash_sha256("OHMASSACRE"),
                  "IL possede le talent levitation et est de type Electrik",
                  "O" )

Enigme11 = Enigme ( "Quel est le nom Japonais de Pikachu?",
                  hash_sha256("PIKACHU"),
                  "La reponce est dans la question",
                  "A" )

Enigme12 = Enigme ( "En 6g les mega-evolutions font leur apparition quel pokemon en possedais deux ?" + "\n" + " a) FLORIZARRE" + " b) LEVIATOR" + " c) DRACAUFEU" + " d) TORTANK",
                  hash_sha256("DRACAUFEU"),
                  "Il est de type vol",
                  "D" )

Enigme13 = Enigme ( "Quel pokemon ressemblant a une simple carpe pourrai sauter des montage et qu'il ne faudrai pas enerver d'apres les legendes ?",
                  hash_sha256("MAGIKARP"),
                  "Cette carpe semble avoir des pouvoirs magiques",
                  "E" )

Enigme14 = Enigme ( "Quel est le seul pokemon n'ayant pas besoin de Mega Geme pour Mega Evoluer ?",
                  hash_sha256("Rayquaza"),
                  "Emeraude Delta aurait dus etre son jeu",
                  "E" )

Enigme15 = Enigme ( "Quel est le pokemon qui suite a un bug crea les pokemobn chromatiques ?",
                  hash_sha256("LEVIATOR"),
                  "Il est rouge dans le lac Colere",
                  "G" )

Enigme16 = Enigme ( "Quel est le boss final de pokemon donjon mystere explorateur du temps ?",
                  hash_sha256("DIALGA"),
                  "Il est un legendaire de la 4g",
                  "I" )

Enigme17 = Enigme ( "Dans chaque jeu pokemon on peut affronter un rongeur au debut du jeu. Quel est celui de la 4g ?",
                  hash_sha256("KEUNOTOR"),
                  "C'est un castor et il est de type normal",
                  "X" )

Enigme21 = Enigme ( "Parmi les forme du future quelle est celle qui est inspire par deux pokemon ?" + "\n" + " a) ROUE-DE-FER" + " b) VERT-DE-FER" + " c) GARDE-DE-FER" + " d) HOTTE-DE-FER",
                  hash_sha256("GARDE-DE-FER"),
                  "Elle est inspire par les pokemon, GARDEVOIR et GALLAME",
                  "X" )

Enigme22 = Enigme ( "Parmi les pokemons suivent le quel n'est pas un posible starteur de pokemon donjon myster ?" + "\n" + " a) BALIGNON" + " b) RIOLU" + " c) OSSELAIT" + " d) SKITTY",
                  hash_sha256("BALIGNON"),
                  "Il s'agit d'un pokemon champignon",
                  "U" )

Enigme23 = Enigme ( "Quel pokemon n'apprend aucune attaque offensives et a un talent lui permettant de se transformer en l'adversaire et de copier ses capacites et ses statistiques ?",
                  hash_sha256("METAMORPH"),
                  "Sa seule attaque est morphing",
                  "P" )

Enigme24 = Enigme ( "Quel pokemon devait etre la mascotte de pokemon avant d'etre remplace par pikachu car trop mignon et feminin ?" + "\n" + " a) RONDOUDOU" + " b) EVOLIE" + " c) MELOFEE" + " d) STARI",
                  hash_sha256("MELOFEE"),
                  "Il peut evoluer grace a la pierre lune",
                  "O" )

Enigme25 = Enigme ( "Quel est le seul pokemon completement evoluer de type dragon de la 1g ?",
                  hash_sha256("DRACOLOSSE"),
                  "C'est un colosse",
                  "I" )

Enigme26 = Enigme ( "Quel est le seul pokemon qui a perdu en statistiques lord de son evolution ?",
                  hash_sha256("MUNJA"),
                  "Il a un seul point de vie",
                  "G" )

Door1 = Door ( "Quel est le pokemon que tu a obtenus ?",
                hash_sha256("NOCTALIE"),
                "Il aime les tenebre",
                "Rappel toi de la question 1" )

Door2 = Door ( "Quel est le pokemon que tu a obtenus ?",
                hash_sha256("EXAGIDE"),
                "Il est eppee et bouclier",
                "son nom fait croire qu'il est exagonal" )

Door3 = Door ( "Quel est le pokemon que tu a obtenus ?",
                hash_sha256("GOUPIX"),
                "Il evolue avec une pierre feu",
                "Sa forme d'alola est de type glace et fee" )

