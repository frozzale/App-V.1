import random
import string
import streamlit as st

def generiere_buchstabe():
    return random.choice(string.ascii_uppercase)

# Streamlit App
st.title("Buchstabengenerator")

if st.button("Buchstaben generieren"):
    buchstabe = generiere_buchstabe()
    st.write(f"Der zufällig generierte Buchstabe ist: {buchstabe}")