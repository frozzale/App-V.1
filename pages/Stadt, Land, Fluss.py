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