# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
from utils.data_manager import DataManager
from utils import helpers
import random
import string

# Funktion des Buchstabengenerators
def generiere_buchstabe():
    return random.choice(string.ascii_uppercase)

# Streamlit App
st.subheader("Buchstabengenerator")

if st.button("Buchstaben generieren"):
    buchstabe = generiere_buchstabe()
    st.write(f"Der zufällig generierte Buchstabe ist: {buchstabe}")

# Punkte-Tabelle
st.subheader("Punkte-Tabelle")

# Eingabefelder für Punkte
punkte = []
for i in range(1, 6):  # Beispiel: 5 Spieler:innen
    punkt = st.number_input(f"Punkte für Spieler:in {i}", min_value=0, step=1, key=f"punkte_{i}")
    punkte.append(punkt)

# Total berechnen
total = sum(punkte)
st.write(f"**Total der Punkte:** {total}")