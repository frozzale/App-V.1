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
    parse_dates = ['timestamp'],
    encoding="utf-8"    
    )
# ====== End Init Block ======
# ------------------------------------------------------------
# Here starts the actual app, which was developed previously
import streamlit as st

# Initialisiere den Seitenstatus
if "page" not in st.session_state:
    st.session_state["page"] = "main"


st.title('Stadt, Land, Fluss')
name = st.session_state.get('name', 'Gast')
st.markdown(f"✨ Hallo {name}! ✨")
st.write("In dieser Version der App hast du verschiedene Möglichkeiten, Stadt, Land, Fluss zu spielen.")
st.info("""Diese App ist noch in der Entwicklung und deshalb nicht abschliessend.""")
st.markdown("""
        Informationen zum Spiel: 
        - Das Spiel wird entweder auf Papier oder direkt in der App gespielt.
        - Es gibt viele verschiedene Kategorien. Entweder wählt ihr sie selbst aus, oder ihr lasst sie durch einen Button zufällig generieren. 
        - Der Buchstabe wird ebenfalls durch einen Button zufällig generiert.
        - Der Spieler, der am schnellsten alles ausgefüllt hat, ruft "Stopp!".
        - Versuche so schnell wie möglich zu sein und einzigartige Worte zu finden.
        - Die Punkteverteilung ist wie folgt:
            - 5 Punkte für ein einzigartiges Wort
            - 1 Punkt für ein Wort, das auch andere Spieler:innen haben
            - 0 Punkte für kein Wort oder ein falsches Wort
    """)


if st.button("Zu den verschiedenen Spielmodi"):
    st.switch_page("pages/1_Verschiedene Modi.py")


st.write("Diese App wurde von Alessia Frozzi (frozzale@students.zhaw.ch), Alicia Cardoso (cardoali@students.zhaw.ch) und Elena Müller (muellel3@students.zhaw.ch) entwickelt.")