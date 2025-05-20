# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
import pandas as pd

# Anzeige der ausgewählten Kategorien
if st.session_state["ausgewaehlte_kategorien"]:
    st.subheader("Deine ausgewählten Kategorien:")
    for kategorie in st.session_state["ausgewaehlte_kategorien"]:
        st.write(f"- {kategorie}")

# Anzeige des generierten Buchstabens
st.subheader("Dein zufälliger Buchstabe:")
if st.session_state["buchstabe"]:
    st.write(f"**{st.session_state['buchstabe']}**")

st.header("Kategorien-Punkte-Tabelle")

# Hole die Kategorien aus dem Session State
kategorien = st.session_state.get("ausgewaehlte_kategorien", [])

if not kategorien:
    st.warning("Bitte wähle zuerst Kategorien auf der Hauptseite aus!")
    st.stop()

# Anzahl der Spiele (Tabellen untereinander)
anzahl_spiele = st.number_input("Anzahl Spiele", min_value=1, max_value=10, value=3, step=1)

for spiel in range(1, anzahl_spiele + 1):
    st.markdown(f"### Spiel {spiel}")
    punkte = []
    for kategorie in kategorien:
        punkt = st.number_input(
            f"Punkte für {kategorie}",
            min_value=0, max_value=100, step=1,
            key=f"{kategorie}_spiel_{spiel}"
        )
        punkte.append(punkt)
    # DataFrame für dieses Spiel
    df = pd.DataFrame({
        "Kategorie": kategorien,
        f"Punkte Spiel {spiel}": punkte
    })
    # Total berechnen und anhängen
    total = df[f"Punkte Spiel {spiel}"].sum()
    df.loc[len(df)] = ["Total", total]
    st.dataframe(df, use_container_width=True)