import streamlit as st

st.title("Flexibles Spielraster")

# Eingabe für Zeilen und Spalten
anzahl_zeilen = st.number_input("Anzahl Zeilen", min_value=1, max_value=20, value=5, step=1)
anzahl_spalten = st.number_input("Anzahl Spalten", min_value=1, max_value=10, value=5, step=1)

st.write("**Raster:**")

for i in range(anzahl_zeilen):
    cols = st.columns(anzahl_spalten)
    for j in range(anzahl_spalten):
        with cols[j]:
            st.text_area(f"Zelle {i+1},{j+1}", key=f"raster_{i}_{j}")