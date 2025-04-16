# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

import streamlit as st
from utils.data_manager import DataManager
from utils import helpers
import random
import string

# Funktion des Buchstabengenerators
def generiere_buchstabe():
    return random.choice(string.ascii_uppercase)

# Streamlit App
st.subheader("Buchstabengenerator")

if st.button("Buchstaben generieren"):
    buchstabe = generiere_buchstabe()
    st.write(f"Der zufällig generierte Buchstabe ist: {buchstabe}")