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
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import altair as alt

if st.button("Home"):
    st.switch_page("Start.py")
if st.button("Zurück zu den Spielmodi"):
    st.switch_page("pages/1_Verschiedene Modi.py")

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Daten vorhanden. Bitte zuerst ein Spiel spielen.') 
    st.stop()

# --- Liniengrafik: Totalpunkte pro Spiel, gruppiert nach Modus ---
st.subheader("Verlauf der Totalpunkte pro Modus:chart_with_upwards_trend:")

if "Total" in data_df.columns and "Modus" in data_df.columns:
    df_plot = data_df.copy()
    if "timestamp" in df_plot.columns:
        df_plot = df_plot.sort_values("timestamp")
    df_plot = df_plot.reset_index(drop=True)
    df_plot["Spielnummer"] = df_plot.index + 1  # Für X-Achse

    chart = alt.Chart(df_plot).mark_line(point=True).encode(
        x=alt.X("Spielnummer", title="Spielnummer"),
        y=alt.Y("Total", title="Gesamtpunkte"),
        color=alt.Color("Modus", title="Modus"),
        tooltip=["Modus", "Total", "Spielnummer"]
    ).properties(width=600, height=350)

    st.altair_chart(chart, use_container_width=True)
else:
    st.info("Keine Totalpunkte oder Modus-Informationen vorhanden.")

if "Modus" not in data_df.columns:
    data_df["Modus"] = ""
anzeige_df = data_df[data_df["Modus"].isin(["Leader", "Spieler"])]
st.subheader("Alle eingegebenen Wörter und Punkte (nur Leader & Spieler)")
st.dataframe(anzeige_df)

# ---- NUR Spielraster Leader & Spieler für die Tabelle ----
#anzeige_df = data_df[data_df["Modus"].isin(["Leader", "Spieler"])]

#st.subheader("Alle eingegebenen Wörter und Punkte (nur Leader & Spieler)")
#st.dataframe(anzeige_df)

# ---- Häufigkeit der gespielten Kategorien ----
st.subheader("Häufigkeit der gespielten Kategorien (nur Manuell & Leader):bar_chart:")

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
    st.subheader("Häufigkeit der gezogenen Buchstaben:bar_chart:")
    st.bar_chart(data_df["Buchstabe"].value_counts().sort_index())

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Daten vorhanden. Bitte zuerst ein Spiel spielen.') 
    st.stop()

st.subheader("Alle eingegebenen Wörter und Punkte:pencil:")
st.dataframe(data_df)




