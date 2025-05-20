import streamlit as st

st.title("Flexibles Spielraster")
st.subheader("Erstelle dein eigenes Raster für Stadt, Land, Fluss")
st.write("Starte damit, die gewählten Kategorien in die Zeilen des Rasters einzutragen.")

# Eingabe für Zeilen und Spalten
anzahl_zeilen = st.number_input("Anzahl Zeilen. Wie viele Runden willst du spielen?", min_value=1, max_value=20, value=5, step=1)
anzahl_spalten = st.number_input("Anzahl Spalten. Nehme so viele Spalten, wie Kategorien gewählt wurden.", min_value=1, max_value=10, value=5, step=1)

st.subheader("**Raster:**")

# Kopfzeile
header_cols = st.columns(anzahl_spalten + 1)
for j in range(anzahl_spalten):
    with header_cols[j]:
        st.markdown(f"**Kategorie {j+1}**")
# Eine Zeile mit so vielen Zellen wie angegeben
cols = st.columns(anzahl_spalten)
for j in range(anzahl_spalten):
    with cols[j]:
        #st.text_area(f"Kategorie {j+1}", key=f"zeile_{j}")
        st.text_area(f"", key=f"zeile_{j}")
with header_cols[-1]:
    st.markdown("**Total**")

# Raster mit Wort- und Punkteingabe
for i in range(anzahl_zeilen):
    cols = st.columns(anzahl_spalten + 1)
    zeilen_total = 0
    for j in range(anzahl_spalten):
        with cols[j]:
            wort = st.text_input(f"Wort {i+1},{j+1}", key=f"wort_{i}_{j}")
            punkte = st.number_input(f"Punkte {i+1},{j+1}", min_value=0, max_value=100, step=1, key=f"punkte_{i}_{j}")
            zeilen_total += punkte
    with cols[-1]:
        st.markdown(f"**{zeilen_total}**")

# Gesamttotal aller Punkte berechnen und anzeigen
gesamt_total = 0
for i in range(anzahl_zeilen):
    for j in range(anzahl_spalten):
        gesamt_total += st.session_state.get(f"punkte_{i}_{j}", 0)

st.markdown(f"### Deine aktuelle totale Punktzahl lautet: **{gesamt_total}**")