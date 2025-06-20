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


st.title("Verschiedene Modi:crossed_swords:")
st.subheader("Hier kannst du dir einen Überblick über die verschiedenen Modi verschaffen und dich für einen Modus entscheiden.")

st.write("Folgende Modi stehen dir zur Verfügung:")
st.badge("Manueller Modus", color="primary")
st.write("Wichtige Punkte zu diesem Modus:")
st.markdown("""
            - In diesem Modus spielst du das Spiel mit Stift und Papier. Also ganz klassisch.
            - Zeichne dir auf ein Blatt Papier ein Raster mit den gewählten Kategorien, die gewünschte Anzahl Runden und eine Spalte für die Punkte.
            - Wähle aus, mit wie vielen Kategorien du spielen möchtest und wähle sie aus. Wenn ihr bereit seid, dann generiere den Buchstaben. 
            - Die Punkte pro Runde kannst du dann direkt in die App eingeben und es wird dir am Ende des Spiels das Total angezeigt.
            - Nach dem Eintragen der Punkte kannst du die Daten speichern und grafisch darstellen lassen.
""")
if st.button("Zum manuellen Modus"):
    st.switch_page("pages/2_Manueller Modus.py")
st.divider()
st.badge("Leader und Spieler Modus", color="blue")
st.write("Wichtige Punkte zu diesen Modi:")
st.markdown("""
            - In diesem Modus kannst du das Spiel entweder als Spieler oder als Leader spielen.
            - Der Leader hat alle wichtigen Funktionen, um das Spiel zu starten und leiten. Es braucht daher nur einen Leader.
                 - Die Funktionen sind:
                    - Kategorien auswählen
                    - Buchstaben generieren
                    - Raster erstellen/ anpassen
                    - Punkte eingeben
            - Der Spieler hingegen hat nur das Raster, um die Kategorien, Antworten und Punkte einzugeben. 
            - Auch hier kannst du die Daten speichern und graphisch darstellen lassen.
""")
if st.button("Zum Leader Modus"):
    st.switch_page("pages/5_Spielraster Leader.py")
st.subheader("oder")
if st.button("Zum Spieler Modus"):
    st.switch_page("pages/4_Spielraster Spieler.py")

if st.button("Home"):
    st.switch_page("Start.py")