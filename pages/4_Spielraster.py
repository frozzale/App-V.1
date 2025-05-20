import streamlit as st

st.title("Flexibles Spielraster")
st.subheader("Erstelle dein eigenes Raster für Stadt, Land, Fluss")
st.write("Starte damit, die gewählten Kategorien in die Zeilen des Rasters einzutragen.")

# Eingabe für Zeilen und Spalten
anzahl_zeilen = st.number_input("Anzahl Zeilen. Wie viele Runden willst du spielen?", min_value=1, max_value=20, value=5, step=1)
anzahl_spalten = st.number_input("Anzahl Spalten. Nehme so viele Spalten, wie Kategorien gewählt wurden.", min_value=1, max_value=10, value=5, step=1)

st.subheader("**Raster:**")

# Erste Zeile: Überschriften
header_cols = st.columns(anzahl_spalten)
for j in range(anzahl_spalten):
    with header_cols[j]:
        st.markdown(f"**Kategorie {j+1}**")
# Eine Zeile mit so vielen Zellen wie angegeben
cols = st.columns(anzahl_spalten)
for j in range(anzahl_spalten):
    with cols[j]:
        #st.text_area(f"Kategorie {j+1}", key=f"zeile_{j}")
        st.text_area(f"", key=f"zeile_{j}")


# Restliche Zeilen: Eingabefelder
for i in range(anzahl_zeilen):
    cols = st.columns(anzahl_spalten)
    for j in range(anzahl_spalten):
        with cols[j]:
            st.text_area(f"Eingabe {i+1},{j+1}", key=f"raster_{i}_{j}")

