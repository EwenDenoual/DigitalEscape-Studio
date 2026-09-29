#!/usr/bin/env bash
#
# test.sh — Parcours complet du jeu DigitalEscape-Studio
#
# Pour chaque room :
#   1. GET  /Room{id}                 -> liste des énigmes disponibles
#   2. Pour chaque énigme :
#        POST /Room{id}/choix         -> récupère la question
#        GET  /Enigme{n}/indice       -> affiche l'indice (avant de répondre)
#        GET  /Enigme{n}/reponse      -> envoie la bonne réponse, récupère la lettre
#        GET  /Enigme{n}/lettre       -> vérifie la lettre obtenue
#   3. GET  /Door{id}/question        -> question de la porte
#      GET  /Door{id}/indice          -> indice de la porte
#      GET  /Door{id}/indice2         -> indice2 de la porte
#      GET  /Door{id}/reponse         -> résout la porte
#      GET  /Door{id}/unlock          -> déverrouille -> passe à la room suivante
#
# Room3 = dernière room : si sa porte est résolue -> victoire.
#
# Usage : chmod +x test.sh && ./test.sh
# Prérequis : curl, jq (optionnel mais recommandé pour un affichage propre)

set -uo pipefail

BASE_URL="http://127.0.0.1:8000"

# Utilise jq si dispo pour un affichage lisible, sinon affiche le JSON brut
pretty() {
    if command -v jq >/dev/null 2>&1; then
        jq . 2>/dev/null || cat
    else
        cat
    fi
}

separator() {
    echo "----------------------------------------------------------------------"
}

step() {
    echo ""
    echo "▶ $1"
}

# ---------------------------------------------------------------------------
# Données du jeu : numéros d'énigmes par room + bonnes réponses (en clair)
# Les réponses viennent du fichier enigme.py (avant hash_sha256)
# ---------------------------------------------------------------------------

declare -A ENIGME_REPONSES=(
    [1]="EVOLIE"        [2]="NOEUNEUF"     [3]="TAUROS"       [4]="COSMOVUM"
    [5]="IRE-FOUDRE"    [6]="LANSSORIEN"   [7]="AMPHINOBI"    [8]="OHMASSACRE"
    [11]="PIKACHU"      [12]="DRACAUFEU"   [13]="MAGIKARP"    [14]="Rayquaza"
    [15]="LEVIATOR"     [16]="DIALGA"
    [21]="GARDE-DE-FER" [22]="BALIGNON"    [23]="METAMORPH"   [24]="MELOFEE"
    [25]="DRACOLOSSE"   [26]="MUNJA"
)

# room_id -> liste des numéros d'énigme de cette room
ROOM_ENIGMES_1="1 2 3 4 5 6 7 8"
ROOM_ENIGMES_2="11 12 13 14 15 16"
ROOM_ENIGMES_3="21 22 23 24 25 26"

# room_id -> bonne réponse de la porte
declare -A DOOR_REPONSES=(
    [1]="NOCTALIE"
    [2]="EXAGIDE"
    [3]="GOUPIX"
)

# ---------------------------------------------------------------------------
# Fonction : joue une room entière (toutes ses énigmes puis sa porte)
# ---------------------------------------------------------------------------

jouer_room() {
    local room_id="$1"
    local enigmes="$2"

    separator
    echo "🏠 ROOM $room_id"
    separator

    step "GET /Room${room_id} — liste des énigmes disponibles"
    curl -s -X GET "${BASE_URL}/Room${room_id}" | pretty

    for n in $enigmes; do
        separator
        echo "🧩 Énigme $n"

        step "POST /Room${room_id}/choix — choix de l'énigme $n"
        curl -s -X POST "${BASE_URL}/Room${room_id}/choix" \
            -H "Content-Type: application/json" \
            -d "{\"enigme_number\": ${n}}" | pretty

        step "GET /Enigme${n}/indice — consultation de l'indice"
        curl -s -X GET "${BASE_URL}/Enigme${n}/indice" | pretty

        local reponse="${ENIGME_REPONSES[$n]}"
        step "GET /Enigme${n}/reponse?tentative=${reponse} — envoi de la bonne réponse"
        curl -s -G "${BASE_URL}/Enigme${n}/reponse" \
            --data-urlencode "tentative=${reponse}" | pretty

        step "GET /Enigme${n}/lettre — récupération de la lettre"
        curl -s -X GET "${BASE_URL}/Enigme${n}/lettre" | pretty
    done

    separator
    echo "🚪 Porte de la room $room_id"

    step "GET /Door${room_id}/question"
    curl -s -X GET "${BASE_URL}/Door${room_id}/question" | pretty

    step "GET /Door${room_id}/indice"
    curl -s -X GET "${BASE_URL}/Door${room_id}/indice" | pretty

    step "GET /Door${room_id}/indice2"
    curl -s -X GET "${BASE_URL}/Door${room_id}/indice2" | pretty

    local door_reponse="${DOOR_REPONSES[$room_id]}"
    step "GET /Door${room_id}/reponse?tentative=${door_reponse} — résolution de la porte"
    curl -s -G "${BASE_URL}/Door${room_id}/reponse" \
        --data-urlencode "tentative=${door_reponse}" | pretty

    step "GET /Door${room_id}/unlock — déverrouillage"
    curl -s -X GET "${BASE_URL}/Door${room_id}/unlock" | pretty
}

# ---------------------------------------------------------------------------
# Vérification que le serveur répond avant de commencer
# ---------------------------------------------------------------------------

step "GET /health — vérification que le serveur est up"
curl -s -X GET "${BASE_URL}/health" | pretty

# ---------------------------------------------------------------------------
# Parcours complet : Room1 -> Room2 -> Room3 -> victoire
# ---------------------------------------------------------------------------

jouer_room 1 "$ROOM_ENIGMES_1"
jouer_room 2 "$ROOM_ENIGMES_2"
jouer_room 3 "$ROOM_ENIGMES_3"

separator
echo "🏆 Toutes les rooms ont été résolues — partie terminée !"
separator