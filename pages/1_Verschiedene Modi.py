# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st


st.title("Verschiedene Modi")
st.subheader("Hier kannst du dir einen Überblick über die verschiedenen Modi verschaffen und dich für einen Modus entscheiden.")

st.write("Folgende Modi stehen dir zur Verfügung:")
st.badge("Manueller Modus", color="primary")
st.write("Wichtige Punkte zu diesem Modus:")
st.markdown("""
            - In diesem Modus spielst du das Spiel mit Stift und Papier. Also ganz klassisch.
            - Zeichne dir auf ein Blatt Papier ein Raster mit den gewählten Kategorien, die gewünschte Anzahl Runden und eine Spalte für die Punkte.
            - Es werden insgesamt 6 Kategorien ausgewählt und ein Buchstabe generiert. 
            - 
            - Die Punkte pro Runde kannst du dann manuell eingeben und es wird dir am Ende des Spiels das Total angezeigt.
""")
if st.button("Zum manuellen Modus"):
    st.switch_page("pages/2_Manueller Modus.py")

if st.button("Home"):
    st.switch_page("Start.py")