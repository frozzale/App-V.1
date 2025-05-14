# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
from utils.data_manager import DataManager
from utils import helpers
import pandas as pd
import matplotlib.pyplot as plt


data_df = st.session_state['data_df'] 
# Überprüfen, ob Spieldaten vorhanden sind
if "spieldaten" in st.session_state and st.session_state["spieldaten"]:
    spieldaten = st.session_state["spieldaten"]

    # Konvertiere die Spieldaten in ein DataFrame
    daten = []
    for spiel, daten_spiel in enumerate(spieldaten, start=1):
        if "Total" in daten_spiel:
            daten.append({"Spiel": spiel, "Gesamtpunkte": daten_spiel["Total"]})
    
    if daten:
        df = pd.DataFrame(daten)

        # Liniendiagramm für die Gesamtpunktzahl
        st.subheader("Gesamtpunktzahl pro Spiel")
        fig, ax = plt.subplots()
        ax.plot(df["Spiel"], df["Gesamtpunkte"], marker="o", linestyle="-", color="b")
        ax.set_xlabel("Spiel")
        ax.set_ylabel("Gesamtpunkte")
        ax.set_title("Gesamtpunktzahl pro Spiel")
        ax.grid(True)
        st.pyplot(fig)
    else:
        st.warning("Es gibt keine Daten, um ein Diagramm zu erstellen.")
else:
    st.info("Es wurden noch keine Spieldaten gespeichert.")

#df = pd.read_csv("data.csv")  # Hier wird die CSV-Datei geladen
#df = st.session_state.get("df")
#st.markdown(f"**Durchschnittliche Punkte:** {df['Gesamtpunkte'].mean():.2f}")
#st.markdown(f"**Höchste Punktzahl:** {df['Gesamtpunkte'].max()}")

#csv = df.to_csv(index=False).encode("utf-8")
#st.download_button("Ergebnisse als CSV herunterladen", data=csv, file_name="spieldaten.csv", mime="text/csv")