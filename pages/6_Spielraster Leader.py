# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
from utils.data_manager import DataManager
from utils import helpers
from Code.kategorien import kategorien
import random
import string
import pandas as pd

# Initialisiere den Session State für die Kategorien
if "ausgewaehlte_kategorien" not in st.session_state:
    st.session_state["ausgewaehlte_kategorien"] = []

# Initialisiere den Session State für den Buchstaben
if "buchstabe" not in st.session_state:
    st.session_state["buchstabe"] = ""

# Auswahl der Kategorien
st.subheader("Wähle 6 Kategorien aus:")
ausgewaehlte_kategorien = st.multiselect(
    "Kategorien auswählen:",
    options=[f"{uebertitel}: {kategorie}" for uebertitel, kategorien_liste in kategorien.items() for kategorie in kategorien_liste],
    default=st.session_state["ausgewaehlte_kategorien"],  # Lade die gespeicherten Kategorien
    max_selections=6
)

# Button zum Übernehmen der Auswahl
if st.button("Kategorien übernehmen"):
    st.session_state["ausgewaehlte_kategorien"] = ausgewaehlte_kategorien

# Speichere die manuell ausgewählten Kategorien im Session State
#st.session_state["ausgewaehlte_kategorien"] = ausgewaehlte_kategorien

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

st.title("Flexibles Spielraster: Leader")
st.subheader("Erstelle dein eigenes Raster für Stadt, Land, Fluss")
st.write("Starte damit, die gewählten Kategorien in die Zeilen des Rasters einzutragen.")

# Eingabe für Zeilen und Spalten
anzahl_zeilen = st.number_input("Anzahl Zeilen. Wie viele Runden willst du spielen?", min_value=1, max_value=20, value=5, step=1)
anzahl_spalten = st.number_input("Anzahl Spalten. Nehme so viele Spalten, wie Kategorien gewählt wurden.", min_value=1, max_value=10, value=5, step=1)

st.subheader("**Raster:**")

# Kopfzeile
header_cols = st.columns(anzahl_spalten + 1)
for j in range(anzahl_spalten):
    with header_cols[j]:
        st.markdown(f"**Kategorie {j+1}**")
# Eine Zeile mit so vielen Zellen wie angegeben
cols = st.columns(anzahl_spalten)
for j in range(anzahl_spalten):
    with cols[j]:
        #st.text_area(f"Kategorie {j+1}", key=f"zeile_{j}")
        st.text_area(f"", key=f"zeile_{j}")
with header_cols[-1]:
    st.markdown("**Total**")

# Raster mit Wort- und Punkteingabe
for i in range(anzahl_zeilen):
    cols = st.columns(anzahl_spalten + 1)
    zeilen_total = 0
    for j in range(anzahl_spalten):
        with cols[j]:
            wort = st.text_input(f"Wort {i+1},{j+1}", key=f"wort_{i}_{j}")
            punkte = st.number_input(f"Punkte {i+1},{j+1}", min_value=0, max_value=100, step=1, key=f"punkte_{i}_{j}")
            zeilen_total += punkte
    with cols[-1]:
        st.markdown(f"**{zeilen_total}**")

# Gesamttotal aller Punkte berechnen und anzeigen
gesamt_total = 0
for i in range(anzahl_zeilen):
    for j in range(anzahl_spalten):
        gesamt_total += st.session_state.get(f"punkte_{i}_{j}", 0)

st.markdown(f"### Deine aktuelle totale Punktzahl lautet: **{gesamt_total}**")

if st.button("Home"):
    st.switch_page("Start.py")