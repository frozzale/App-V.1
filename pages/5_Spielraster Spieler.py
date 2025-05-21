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
import streamlit as st
from utils.data_manager import DataManager
from utils import helpers
import pandas as pd

st.title("Flexibles Spielraster: Spieler")
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

st.info("Speichere zuerst deine Daten mit 'Spiel beenden', bevor du die Ergebnisse ansiehst.")
# Button zum Beenden der Runde
if st.button("Spiel beenden"):
    # Hole die Kategorien aus der Kopfzeile
    kategorien = [st.session_state.get(f"zeile_{j}", f"Kategorie {j+1}") for j in range(anzahl_spalten)]
    daten = []
    for i in range(anzahl_zeilen):
        eintraege = []
        for j, kategorie in enumerate(kategorien):
            wort = st.session_state.get(f"wort_{i}_{j}", "")
            punkte = st.session_state.get(f"punkte_{i}_{j}", 0)
            # Kombiniere Wort und Punkte als String, z.B. "Stadt: Zürich (5)"
            eintrag = f"{kategorie}: {wort} ({punkte})"
            eintraege.append(eintrag)
        zeile = {
            "timestamp": helpers.ch_now(),
            "Runde": i + 1,
            "Kategorien": ", ".join(eintraege),
            "Total": sum(st.session_state.get(f"punkte_{i}_{j}", 0) for j in range(anzahl_spalten))
        }
        daten.append(zeile)
    df = pd.DataFrame(daten)
    # Speichere jede Zeile als Record
    from utils.data_manager import DataManager
    for _, row in df.iterrows():
        DataManager().append_record(session_state_key="data_df", record_dict=row.to_dict())
    st.success("Die Spieldaten wurden gespeichert! Gehe zur nächsten Seite, um die Ergebnisse zu sehen.")


if st.button("Ergebnisse anzeigen"):
    st.switch_page("pages/3_Ergebnisse.py")
if st.button("Modus wechseln"):
    st.switch_page("pages/1_Verschiedene Modi.py")
if st.button("Home"):
    st.switch_page("Start.py")