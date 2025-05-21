# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
#from utils.data_manager import DataManager
#from utils import helpers
import pandas as pd
import matplotlib.pyplot as plt

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine Daten vorhanden. Bitte zuerst ein Spiel spielen.') 
    st.stop()

st.line_chart(data_df, x='timestamp', y='Total', use_container_width=True)

# --- Grafik: Häufigkeit der gespielten Kategorien ---
st.subheader("Häufigkeit der gespielten Kategorien")

# Alle Kategorien aus allen Spielen extrahieren und zählen
from collections import Counter

# Die Spalte "Kategorien" enthält Strings wie "Geografie: Stadt, Tiere: Säugetier, ..."
# Wir splitten sie und zählen die einzelnen Kategorien
alle_kategorien = []
for eintrag in data_df["Kategorien"].dropna():
    # Splitte an Kommas und entferne Leerzeichen
    kategorien_liste = [k.strip() for k in eintrag.split(",")]
    alle_kategorien.extend(kategorien_liste)

# Zähle die Häufigkeit jeder Kategorie
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

#if data_df:
    #df = pd.DataFrame(daten)

    # Liniendiagramm für die Gesamtpunktzahl
        #st.subheader("Gesamtpunktzahl pro Spiel")
        #fig, ax = plt.subplots()
        #ax.plot(df["Spiel"], df["Gesamtpunkte"], marker="o", linestyle="-", color="b")
        #ax.set_xlabel("Spiel")
        #ax.set_ylabel("Gesamtpunkte")
        #ax.set_title("Gesamtpunktzahl pro Spiel")
        #ax.grid(True)
        #st.pyplot(fig)
#else:
    #st.warning("Es gibt keine Daten, um ein Diagramm zu erstellen.")
#else:
    #st.info("Es wurden noch keine Spieldaten gespeichert.")


