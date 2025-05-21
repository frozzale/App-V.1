import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {display: none !important;}
        [data-testid="collapsedControl"] {display: none !important;}
    </style>
    """,
    unsafe_allow_html=True,
)
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

# Streamlit App
st.header("Stadt, Land, Fluss - Manueller Modus")

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
st.write(f"**Total der Punkte im Spiel:** {total}")

st.info("Speichere zuerst deine Daten mit 'Spiel beenden', bevor du die Ergebnisse ansiehst.")
# Button zum Beenden der Runde
if st.button("Spiel beenden"):
    # Erstelle das Dictionary 'result' mit den aktuellen Daten
    result_dict = {
    "timestamp": helpers.ch_now(),
    "Kategorien": ", ".join(ausgewaehlte_kategorien),
    "Punkte": punkte,
    "Total": sum(punkte),
    "Runden": anzahl_runden,
    "Buchstabe": st.session_state["buchstabe"],
    "Modus": "Manuell"
    #"timestamp": pd.Timestamp.now()
}
# Speichere die Daten persistent mit DataManager
    from utils.data_manager import DataManager
    DataManager().append_record(session_state_key="data_df", record_dict=result_dict)

    st.success("Die Spieldaten wurden gespeichert! Gehe zur nächsten Seite, um die Ergebnisse zu sehen.")
    
if st.button("Ergebnisse anzeigen"):
    st.switch_page("pages/3_Ergebnisse.py")

if st.button("Modus wechseln"):
    st.switch_page("pages/1_Verschiedene Modi.py")


