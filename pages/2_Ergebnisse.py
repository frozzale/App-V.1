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

    # Konvertiere die Spieldaten in ein DataFrame
    daten = []
    for spiel, daten_spiel in enumerate(spieldaten, start=1):
        if "Kategorien" in daten_spiel and "Punkte" in daten_spiel:
            for kategorie, punkt in zip(daten_spiel["Kategorien"], daten_spiel["Punkte"]):
                daten.append({"Spiel": spiel, "Kategorie": kategorie, "Punkte": punkt})
    if daten:
        df = pd.DataFrame(daten)

        # Punkte pro Kategorie (Balkendiagramm)
        st.subheader("Punkte pro Kategorie")
        fig, ax = plt.subplots()
        df.groupby("Kategorie")["Punkte"].sum().plot(kind="bar", ax=ax, color="skyblue", edgecolor="black")
        ax.set_title("Punkte pro Kategorie")
        ax.set_xlabel("Kategorie")
        ax.set_ylabel("Punkte")
        st.pyplot(fig)

        # Punkte pro Spiel (Liniendiagramm)
        st.subheader("Punkte pro Spiel")
        fig, ax = plt.subplots()
        df.groupby("Spiel")["Punkte"].sum().plot(kind="line", ax=ax, marker="o", color="green", linewidth=2)
        ax.set_title("Punkte pro Spiel")
        ax.set_xlabel("Spiel")
        ax.set_ylabel("Punkte")
        ax.grid(True, linestyle="--", alpha=0.7)
        st.pyplot(fig)

        # Punkteverteilung (Kreisdiagramm)
        st.subheader("Punkteverteilung nach Kategorien")
        fig, ax = plt.subplots()
        df.groupby("Kategorie")["Punkte"].sum().plot(
            kind="pie", ax=ax, autopct='%1.1f%%', startangle=90, cmap="Pastel1", legend=False
        )
        ax.set_ylabel("")
        ax.set_title("Punkteverteilung nach Kategorien")
        st.pyplot(fig)
    else:
        st.warning("Es gibt keine Daten, um Grafiken zu erstellen.")
else:
    st.info("Es wurden noch keine Spieldaten gespeichert.")
