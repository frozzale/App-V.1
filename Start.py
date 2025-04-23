# ====== Start Init Block ======
# This needs to copied on top of the entry point of the app (Start.py)

import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="AppV1")  # switch drive 

# initialize the login manager
login_manager = LoginManager(data_manager)
login_manager.login_register()  # open login/register page

# load the data from the persistent storage into the session state
data_manager.load_user_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )
# ====== End Init Block ======

# ------------------------------------------------------------
# Here starts the actual app, which was developed previously
import streamlit as st

st.title('Stadt, Land, Fluss')
name = st.session_state.get('name')
st.markdown(f"✨ Hallo {name}! ✨")
st.write("In der ersten Version dieser App kannst du den Buchstaben für's Spiel generieren und deine Punkte pro Runde eintragen. Die Punkte werden dann automatisch zusammengezählt.")

        
# Add some advice
st.info("""Diese App ist noch in der Entwicklung und deshalb nicht abschliessend.""")
st.markdown("""
        Informationen zum Spiel: 
        - Das Spiel wird auf Papier gespielt.
        - Es gibt 5 Kategorien: Stadt, Land, Fluss, Tier und Marke.
        - Der Buchstabe wird zufällig generiert.
        - Der Spieler, der am schnellsten alles ausgefüllt hat, ruft "Stopp!".
        - Versuche so schnell wie möglich zu sein und einzigartige Worte zu finden.
        - Die Punkteverteilung ist wie folgt:
            - 5 Punkte für ein einzigartiges Wort
            - 1 Punkt für ein Wort, das auch andere Spieler:innen haben
            - 0 Punkte für kein Wort
        """)

# Initialisiere den Schlüssel "page" in st.session_state, falls er nicht existiert
if "page" not in st.session_state:
    st.session_state["page"] = "main"

# Aktuelle Seite aus dem Session State abrufen
page = st.session_state["page"]

# Button zur Unterseite "Stadt, Land, Fluss"
if page == "main":
    if st.button("Zur Unterseite 'Stadt, Land, Fluss'"):
        st.session_state["page"] = "Stadt, Land, Fluss"

# Logik für die Unterseite
if page == "Stadt, Land, Fluss":
    st.write("Willkommen auf der Unterseite 'Stadt, Land, Fluss'!")
    if st.button("Zurück zur Hauptseite"):
        st.session_state["page"] = "main"

st.write("Diese App wurde von Alessia Frozzi (frozzale@students.zhaw.ch), Alicia Cardoso (cardoali@students.zhaw.ch) und Elena Müller (muellel3@students.zhaw.ch) entwickelt.")