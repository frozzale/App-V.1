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

# Funktion des Buchstabengenerators
def generiere_buchstabe():
    return random.choice(string.ascii_uppercase)

# Streamlit App
st.subheader("Buchstabengenerator")

if st.button("Buchstaben generieren"):
    buchstabe = generiere_buchstabe()
    st.write(f"Der zufällig generierte Buchstabe ist: {buchstabe}")

st.subheader("Deine Kategorien lauten:")
st.write("Stadt, Land, Fluss, Tier und Marke.")

# Punkte-Tabelle für einen Spieler und mehrere Runden
st.subheader("Meine Punkte pro Runde")

# Anzahl der Runden
anzahl_runden = st.number_input("Anzahl der Runden", min_value=1, step=1, value=5, key="anzahl_runden")

# Erstelle eine Tabelle mit Auswahlmöglichkeiten für die Punkte
punkte = []
for runde in range(1, anzahl_runden + 1):
    punkt = st.selectbox(
        f"Punkte für Runde {runde}",
        options=[0, 1, 5],  # Nur 0, 1 oder 5 Punkte erlaubt
        key=f"punkte_runde_{runde}"
    )
    punkte.append(punkt)

# Berechne das Total der Punkte
total = sum(punkte)
st.write(f"**Total der Punkte:** {total}")