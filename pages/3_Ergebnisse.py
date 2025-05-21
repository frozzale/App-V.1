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
#from utils.data_manager import DataManager
#from utils import helpers
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Daten vorhanden. Bitte zuerst ein Spiel spielen.') 
    st.stop()

# --- Liniengrafik: Totalpunkte pro Spiel (alle Modi) ---
st.subheader("Verlauf der Totalpunkte (alle Modi)")

if "Total" in data_df.columns:
    df_plot = data_df.copy()
    if "timestamp" in df_plot.columns:
        df_plot = df_plot.sort_values("timestamp")
    # Die X-Achse ist die Spielnummer, die Y-Achse die Gesamtpunkte
    st.line_chart(df_plot["Total"].reset_index(drop=True))
else:
    st.info("Keine Totalpunkte vorhanden.")

if "Modus" not in data_df.columns:
    data_df["Modus"] = ""
anzeige_df = data_df[data_df["Modus"].isin(["Leader", "Spieler"])]
st.subheader("Alle eingegebenen Wörter und Punkte (nur Leader & Spieler)")
st.dataframe(anzeige_df)

# ---- NUR Spielraster Leader & Spieler für die Tabelle ----
anzeige_df = data_df[data_df["Modus"].isin(["Leader", "Spieler"])]

st.subheader("Alle eingegebenen Wörter und Punkte (nur Leader & Spieler)")
st.dataframe(anzeige_df)

# ---- Häufigkeit der gespielten Kategorien ----
st.subheader("Häufigkeit der gespielten Kategorien (nur Manuell & Leader)")

# Nur Daten aus Manuell & Leader
kategorien_df = data_df[data_df["Modus"].isin(["Manuell", "Leader"])]

alle_kategorien = []
for eintrag in kategorien_df["Kategorien"].dropna():
    kategorien_liste = [k.strip() for k in eintrag.split(",")]
    alle_kategorien.extend(kategorien_liste)

kategorie_counter = Counter(alle_kategorien)
if kategorie_counter:
    kategorie_df = pd.DataFrame.from_dict(kategorie_counter, orient='index', columns=['Anzahl'])
    kategorie_df = kategorie_df.sort_values('Anzahl', ascending=False)
    st.bar_chart(kategorie_df)
else:
    st.info("Es wurden noch keine Kategorien gespielt.")

if "Buchstabe" in data_df.columns:
    st.subheader("Häufigkeit der gezogenen Buchstaben")
    st.bar_chart(data_df["Buchstabe"].value_counts().sort_index())

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Daten vorhanden. Bitte zuerst ein Spiel spielen.') 
    st.stop()

st.subheader("Alle eingegebenen Wörter und Punkte")
st.dataframe(data_df)

if st.button("Home"):
    st.switch_page("Start.py")
if st.button("Zurück zu den Spielmodi"):
    st.switch_page("pages/1_Verschiedene Modi.py")
# Überprüfen, ob Spieldaten vorhanden sind
#if "spieldaten" in st.session_state and st.session_state["spieldaten"]:
    #spieldaten = st.session_state["spieldaten"]

    # Konvertiere die Spieldaten in ein DataFrame
    #daten = []
    #for spiel, daten_spiel in enumerate(spieldaten, start=1):
        #if "Total" in daten_spiel:
            #daten.append({"Spiel": spiel, "Gesamtpunkte": daten_spiel["Total"]})


