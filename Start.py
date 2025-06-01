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
    encoding='latin-1'
    )
# ====== End Init Block ======
# ------------------------------------------------------------
# Here starts the actual app, which was developed previously
import streamlit as st

# Initialisiere den Seitenstatus
if "page" not in st.session_state:
    st.session_state["page"] = "main"

# Funktion, um den Hintergrund per Bild-URL zu setzen
def set_background_from_url(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Deine Bild-URL
image_url = "https://i.pinimg.com/736x/8d/fa/70/8dfa704a40f3cf8c8e095321495ca60a.jpg" 
#image_url = "https://i.pinimg.com/736x/17/d8/74/17d87486c848eed7572a22c3c65c3b46.jpg"

# Hintergrund setzen
set_background_from_url(image_url)



st.title('Stadt, Land, Fluss:city_sunrise:')
name = st.session_state.get('name', 'Gast')
st.markdown(f"✨ Hallo {name}! ✨")
st.write("In dieser Version der App hast du verschiedene Möglichkeiten, Stadt, Land, Fluss zu spielen.")
st.info("""In dieser App kannst du dich ausschliesslich über Buttons bewegen.""")
st.markdown("""
        Informationen zum Spiel: 
        - Das Spiel wird entweder auf Papier oder direkt in der App gespielt, je nach dem für welchen Modus du dich entscheidest.
        - Es gibt viele verschiedene Kategorien. Entweder wählt ihr sie selbst aus, oder ihr lasst sie durch einen Button zufällig generieren. 
        - Der Buchstabe wird ebenfalls durch einen Button zufällig generiert.
        - Der Spieler, der am schnellsten alles ausgefüllt hat, ruft "Stopp!".
        - Versuche so schnell wie möglich zu sein und einzigartige Worte zu finden.
        - Die Punkteverteilung ist wie folgt:
            - 5 Punkte für ein einzigartiges Wort
            - 1 Punkt für ein Wort, das auch andere Spieler:innen haben
            - 0 Punkte für kein Wort oder ein falsches Wort
    """)
st.markdown("Du hast ebenfalls die Möglichkeit, dein Spielerprofil anzusehen und zu bearbeiten. Du kannst dort deine Lieblingskategorien auswählen, dein lustigstes Erlebnis und dein liebstes Erlebnis festhalten.")
st.write("Am besten beginnst du einfach mit einem Spiel, um die App kennenzulernen. Viel Spass! :smiley:")

if st.button("Mein Spielerprofil"):
    st.switch_page("pages/6_Mein Spielerprofil.py")

if st.button("Zu den verschiedenen Spielmodi"):
    st.switch_page("pages/1_Verschiedene Modi.py")
#st.divider()
if st.button("Zu meinen Grafiken"):
    st.switch_page("pages/3_Ergebnisse.py")

st.write("Diese App wurde von Alessia Frozzi (frozzale@students.zhaw.ch), Alicia Cardoso (cardoali@students.zhaw.ch) und Elena Müller (muellel3@students.zhaw.ch) entwickelt.")