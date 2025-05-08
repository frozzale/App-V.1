# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
from utils.data_manager import DataManager
from utils import helpers
import pandas as pd
import matplotlib.pyplot as plt

# Überprüfen, ob Spieldaten vorhanden sind
if "spieldaten" in st.session_state and st.session_state["spieldaten"]:
    spieldaten = st.session_state["spieldaten"]

    # Debug-Ausgabe der Spieldaten
    st.write("Spieldaten:", spieldaten)

    # Daten in ein DataFrame umwandeln
    daten = []
    for spiel, daten_spiel in enumerate(spieldaten, start=1):
        if "Kategorien" in daten_spiel and "Punkte" in daten_spiel:
            for kategorie, punkt in zip(daten_spiel["Kategorien"], daten_spiel["Punkte"]):
                daten.append({"Spiel": spiel, "Kategorie": kategorie, "Punkte": punkt})
    if daten:
        df = pd.DataFrame(daten)

# Debugging: DataFrame-Inhalt und Datentypen anzeigen
        st.write("DataFrame-Inhalt:", df)
        st.write("Datentypen im DataFrame:", df.dtypes)

        # Sicherstellen, dass die Spalten die richtigen Datentypen haben
        df["Spiel"] = pd.to_numeric(df["Spiel"], errors="coerce")
        df["Punkte"] = pd.to_numeric(df["Punkte"], errors="coerce")

        # Tabelle anzeigen
        st.subheader("Ergebnisse der Spiele")
        st.dataframe(df)

        # Horizontales Balkendiagramm: Punkte pro Runde
        st.subheader("Punkteverteilung pro Spiel")
        fig, ax = plt.subplots(figsize=(8, 5))
        df.groupby("Spiel")["Punkte"].sum().plot(kind="barh", ax=ax, color="skyblue", edgecolor="black")
        ax.set_title("Punkte pro Spiel", fontsize=14)
        ax.set_xlabel("Punkte", fontsize=12)
        ax.set_ylabel("Spiel", fontsize=12)
        st.pyplot(fig)

        # Kreisdiagramm: Punkteverteilung nach Kategorien
        st.subheader("Punkteverteilung nach Kategorien")
        fig, ax = plt.subplots(figsize=(6, 6))
        df.groupby("Kategorie")["Punkte"].sum().plot(
            kind="pie", ax=ax, autopct='%1.1f%%', startangle=90, cmap="Pastel1", legend=False
        )
        ax.set_ylabel("")
        ax.set_title("Punkteverteilung nach Kategorien", fontsize=14)
        st.pyplot(fig)

        # Liniendiagramm: Punkteentwicklung über die Runden
        st.subheader("Punkteentwicklung über die Spiele")
        fig, ax = plt.subplots(figsize=(8, 5))
        df.groupby("Spiel")["Punkte"].sum().plot(kind="line", ax=ax, marker="o", color="green", linewidth=2)
        ax.set_title("Punkteentwicklung über die Spiele", fontsize=14)
        ax.set_xlabel("Spiel", fontsize=12)
        ax.set_ylabel("Punkte", fontsize=12)
        ax.grid(True, linestyle="--", alpha=0.7)
        st.pyplot(fig)
else:
    st.info("Es wurden noch keine Spieldaten gespeichert.")
