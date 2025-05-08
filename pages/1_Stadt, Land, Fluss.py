# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
from utils.data_manager import DataManager
from utils import helpers
import random
import string
import pandas as pd

def speichere_spieldaten(kategorien, punkte):
    """
    Speichert die Spieldaten in den Session State.

    Args:
        kategorien (list): Die ausgewählten Kategorien.
        punkte (list): Die Punkte der aktuellen Runde.
    """
    if "spieldaten" not in st.session_state:
        st.session_state["spieldaten"] = []

    # Speichere die Daten als Dictionary
    runden_daten = {"Kategorien": kategorien, "Punkte": punkte}
    st.session_state["spieldaten"].append(runden_daten)

# Liste der Kategorien mit Übertiteln
kategorien = {
    "Geografie": ["Stadt", "Land", "Fluss", "Gebirge", "See"],
    "Tiere": ["Säugetier", "Haustier", "Wildtier", "Reptil", "Vogel", "Fisch", "Insekt", "Hunderasse", "Meeresbewohner"],
    "Pflanzen": ["Baum", "Blume", "Gemüse", "Obst", "Kraut"],
    "Berufe": ["Beruf", "Arzt", "Lehrer", "Ingenieur", "Künstler", "Polizist"],
    "Marken": ["Marke", "Auto", "Mode", "Technologie", "Lebensmittel", "Kosmetik"],
    "Sport": ["Sportart", "Olympische Disziplin", "Extremsportarten", "Sportart ohne Ball"],
    "Musik": ["Instrument", "Band", "Sänger", "Genre", "Lied"],
    "Filme & Serien": ["Film", "Serie", "Schauspieler", "Regisseur", "Genre", "Buchtitel"],
    "Essen & Trinken": ["Getränk", "Süßigkeit", "Hauptgericht", "Beilage", "Snack", "Pizzabelag", "Eissorte"],
    "Prominenz": ["Schauspieler", "Sänger", "Fussballspieler", "Politiker", "Historische Persönlichkeit", "Film-/Serie-/Buch-Charakter"],
    "Lustig & ungewöhnlich": ["Scheidungsgrund / Kündigungsgrund", "Jugendwort", "Gegenstände, die die Welt nicht braucht", "Kosenahme", "Superkraft", "Dinge im Haushalt", "Haustiernamen"],
    "Themen zum Kennenlernen": ["Würde ich nie essen", "Reiseziel", "Würde ich kaufen, wenn ich reich wäre", "Hab ich noch nie gemacht", "Mag ich gerne"],
    "Babyparty": ["Babynamen", "Könnte das erste Wort werden", "Geschmacksrichtung für Babybrei", "Hätte ich gerne als Kind gehabt"]
} 

# Initialisiere den Session State für die Kategorien
if "ausgewaehlte_kategorien" not in st.session_state:
    st.session_state["ausgewaehlte_kategorien"] = []

if "buchstabe" not in st.session_state:
    st.session_state["buchstabe"] = None

# Streamlit App
st.header("Stadt, Land, Fluss - Kategorienauswahl")

# Auswahl der Kategorien
st.subheader("Wähle 6 Kategorien aus:")
ausgewaehlte_kategorien = st.multiselect(
    "Kategorien auswählen:",
    options=[f"{uebertitel}: {kategorie}" for uebertitel, kategorien_liste in kategorien.items() for kategorie in kategorien_liste],
    default=st.session_state["ausgewaehlte_kategorien"],  # Lade die gespeicherten Kategorien
    max_selections=6
)

# Speichere die manuell ausgewählten Kategorien im Session State
st.session_state["ausgewaehlte_kategorien"] = ausgewaehlte_kategorien

st.subheader("oder")

# Zufällige Auswahl von 6 Kategorien
if st.button("Zufällige Kategorien generieren"):
    alle_kategorien = [f"{uebertitel}: {kategorie}" for uebertitel, kategorien_liste in kategorien.items() for kategorie in kategorien_liste]
    st.session_state["ausgewaehlte_kategorien"] = random.sample(alle_kategorien, 6)

# Anzeige der ausgewählten Kategorien
if st.session_state["ausgewaehlte_kategorien"]:
    st.subheader("Deine ausgewählten Kategorien:")
    for kategorie in st.session_state["ausgewaehlte_kategorien"]:
        st.write(f"- {kategorie}")
else:
    st.info("Bitte wähle bis zu 6 Kategorien aus oder klicke auf den Button, um zufällige Kategorien zu generieren.")

# Funktion zum Generieren eines zufälligen Buchstabens
def generiere_buchstabe():
    return random.choice(string.ascii_uppercase)

# Button zum Generieren eines Buchstabens
if st.button("Buchstaben generieren"):
    st.session_state["buchstabe"] = generiere_buchstabe()

# Anzeige des generierten Buchstabens
st.write("Dein zufälliger Buchstabe:")
if st.session_state["buchstabe"]:
    st.write(f"**{st.session_state['buchstabe']}**")
else:
    st.info("Drücke auf den Button, um einen Buchstaben zu generieren.")

# Punkte-Tabelle für einen Spieler und mehrere Runden
st.subheader("Meine Punkte pro Runde")

# Anzahl der Runden
anzahl_runden = st.number_input("Anzahl der Runden", min_value=1, step=1, value=5, key="anzahl_runden")

# Erstelle eine Tabelle mit manueller Eingabe der Punkte
punkte = []
for runde in range(1, anzahl_runden + 1):
    punkt = st.number_input(
        f"Punkte für Runde {runde}",
        min_value=0,  # Minimalwert ist 0
        max_value=100,  # Maximalwert ist 100
        step=1,       # Schritte in 1er-Schritten
        key=f"punkte_runde_{runde}"
    )
    punkte.append(punkt)

# Berechne das Total der Punkte
total = sum(punkte)
st.write(f"**Total der Punkte:** {total}")

# Button zum Beenden der Runde
if st.button("Runde beenden"):
    speichere_spieldaten(ausgewaehlte_kategorien, punkte)
    st.success("Die Spieldaten wurden gespeichert! Gehe zur nächsten Seite, um die Ergebnisse zu sehen.")
