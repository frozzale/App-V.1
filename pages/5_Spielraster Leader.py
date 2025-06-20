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

# Anzahl der gewünschten Kategorien wählen
anzahl_kategorien = st.number_input(
    "Wie viele Kategorien möchtest du auswählen?", 
    min_value=1, 
    max_value=10, 
    value=6, 
    step=1, 
    key="anzahl_kategorien"
)

# Auswahl der Kategorien
st.subheader("Wähle deine Kategorien aus:")
# Stelle sicher, dass nicht mehr als erlaubt vorausgewählt sind!
default_kategorien = st.session_state.get("ausgewaehlte_kategorien", [])[:anzahl_kategorien]

ausgewaehlte_kategorien = st.multiselect(
    "Kategorien auswählen:",
    options=[f"{uebertitel}: {kategorie}" for uebertitel, kategorien_liste in kategorien.items() for kategorie in kategorien_liste],
    default=default_kategorien,
    max_selections=anzahl_kategorien
)

# Button zum Übernehmen der Auswahl
if st.button("Kategorien übernehmen"):
    st.session_state["ausgewaehlte_kategorien"] = ausgewaehlte_kategorien

st.subheader("oder")

# Zufällige Auswahl von Kategorien
if st.button("Zufällige Kategorien generieren"):
    alle_kategorien = [f"{uebertitel}: {kategorie}" for uebertitel, kategorien_liste in kategorien.items() for kategorie in kategorien_liste]
    st.session_state["ausgewaehlte_kategorien"] = random.sample(alle_kategorien, anzahl_kategorien)

# Anzeige der ausgewählten Kategorien
if st.session_state["ausgewaehlte_kategorien"]:
    st.subheader("Deine ausgewählten Kategorien:")
    for kategorie in st.session_state["ausgewaehlte_kategorien"]:
        st.write(f"- {kategorie}")
else:
    st.info("Bitte wähle deine Kategorien aus oder klicke auf den Button, um zufällige Kategorien zu generieren.")

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

st.title("Flexibles Spielraster: Leader:crown:")
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
        st.text_area("Kategorie", key=f"zeile_{j}", label_visibility="collapsed")
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

st.info("Speichere zuerst deine Daten mit 'Spiel beenden', bevor du die Ergebnisse ansiehst.")
# Button zum Beenden der Runde
if st.button("Spiel beenden"):
    # Erstelle das Dictionary 'result' mit den aktuellen Daten
    result_dict = {
    "timestamp": helpers.ch_now(),
    "Kategorien": ", ".join(ausgewaehlte_kategorien),
    "Punkte": punkte,
    "Total": gesamt_total,
    "Runden": anzahl_zeilen,
    "Buchstabe": st.session_state["buchstabe"],
    "Modus": "Leader"
}
    # Speichere die Daten persistent mit DataManager
    from utils.data_manager import DataManager
    DataManager().append_record(session_state_key="data_df", record_dict=result_dict)

    st.success("Die Spieldaten wurden gespeichert! Gehe zur nächsten Seite, um die Ergebnisse zu sehen.")
if st.button("Ergebnisse anzeigen"):
    st.switch_page("pages/3_Ergebnisse.py")
if st.button("Modus wechseln"):
    st.switch_page("pages/1_Verschiedene Modi.py")
if st.button("Home"):
    st.switch_page("Start.py")