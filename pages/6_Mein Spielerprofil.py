import streamlit as st
import pandas as pd

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

from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')

st.title("👤 Mein Spielerprofil")

# --- Profilinformationen anzeigen und bearbeiten ---
st.subheader("Profilinformationen")

# Name bearbeiten
name = st.session_state.get("name", "")
new_name = st.text_input("Dein Name", value=name)
if st.button("Name speichern"):
    st.session_state["name"] = new_name
    st.success("Name wurde aktualisiert!")

# Interessen/Kategorien (optional)
if "interessen" not in st.session_state:
    st.session_state["interessen"] = []

st.subheader("Lieblingskategorien")

# --- Lieblingskategorien auswählen, speichern, anzeigen und entfernen ---

alle_kategorien = [
    "Stadt", "Land", "Fluss", "Tier", "Marke", "Beruf", "Instrument", "Film", "Getränk", "Süßigkeit",
    "Olympische Disziplin", "Jugendwort", "Superkraft", "Haustiernamen", "Reiseziel", "Babynamen"
]

# Multiselect für Auswahl
auswahl = st.multiselect(
    "Wähle deine Lieblingskategorien aus:",
    options=alle_kategorien,
    default=st.session_state["interessen"]
)

col1, col2 = st.columns(2)
with col1:
    if st.button("Kategorien speichern"):
        st.session_state["interessen"] = auswahl
        st.success("Kategorien wurden gespeichert!")

with col2:
    if st.button("Alle Lieblingskategorien entfernen"):
        st.session_state["interessen"] = []
        st.success("Alle Lieblingskategorien wurden entfernt!")

# Anzeige der gespeicherten Lieblingskategorien als Tabelle mit Löschen-Button
if st.session_state["interessen"]:
    st.markdown("**Deine gespeicherten Lieblingskategorien:**")
    for idx, kategorie in enumerate(st.session_state["interessen"]):
        cols = st.columns([3, 1])
        cols[0].write(kategorie)
        if cols[1].button("Löschen", key=f"del_{kategorie}_{idx}"):
            st.session_state["interessen"].pop(idx)
            st.experimental_rerun()
else:
    st.markdown("_Noch keine Lieblingskategorien gespeichert._")

st.subheader("Deine Spielerlebnisse")

# Callback-Funktionen für automatisches Speichern
def save_lustigstes():
    st.session_state["lustigstes_erlebnis"] = st.session_state["lustigstes_erlebnis_input"]

def save_liebstes():
    st.session_state["liebstes_erlebnis"] = st.session_state["liebstes_erlebnis_input"]

lustigstes = st.text_area(
    "Was war dein lustigstes Erlebnis im Spiel?:rolling_on_the_floor_laughing:",
    value=st.session_state["lustigstes_erlebnis"],
    placeholder="Erzähle hier dein lustigstes Erlebnis ...",
    key="lustigstes_erlebnis_input",
    on_change=save_lustigstes
)
liebstes = st.text_area(
    "Was war dein liebstes Spielerlebnis?:two_hearts:",
    value=st.session_state["liebstes_erlebnis"],
    placeholder="Beschreibe hier dein schönstes Spielerlebnis ...",
    key="liebstes_erlebnis_input",
    on_change=save_liebstes
)

# --- Statistiken zu gespielten Spielen ---
st.subheader("Deine Spielstatistiken")

data_df = st.session_state.get("data_df", pd.DataFrame())
if not data_df.empty:
    st.write(f"**Anzahl gespielter Spiele:** {len(data_df)}")
    if "Total" in data_df.columns:
        st.write(f"**Durchschnittliche Punktzahl:** {round(data_df['Total'].mean(), 2)}")
    if "Kategorien" in data_df.columns:
        from collections import Counter
        alle_kategorien = []
        for eintrag in data_df["Kategorien"].dropna():
            kategorien_liste = [k.strip() for k in eintrag.split(",")]
            alle_kategorien.extend(kategorien_liste)
        if alle_kategorien:
            haeufigste = Counter(alle_kategorien).most_common(3)
            st.write("**Deine 3 meistgespielten Kategorien:**")
            rang_emojis = ["🥇", "🥈", "🥉"]
            for i, (k, n) in enumerate(haeufigste):
                st.write(f"{rang_emojis[i]} **{k}** ({n}x)")
else:
    st.info("Du hast noch keine Spiele gespielt.")

# --- Navigation ---
st.divider()
if st.button("Zurück zur Startseite"):
    st.switch_page("Start.py")