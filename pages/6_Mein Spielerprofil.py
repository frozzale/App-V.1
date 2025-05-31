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

data_df = st.session_state.get("data_df", pd.DataFrame())

# Hole das zuletzt gespeicherte Profil (Profil-Einträge erkennen wir z.B. daran, dass 'name' gesetzt ist)
profil_row = None
if not data_df.empty and "name" in data_df.columns:
    profil_row = data_df[data_df["name"].notna()].sort_values("timestamp", ascending=False).head(1)
    if not profil_row.empty:
        profil_row = profil_row.iloc[0]

st.title("👤 Mein Spielerprofil")

# --- Profilinformationen anzeigen und bearbeiten ---
st.subheader("Profilinformationen")

# Name bearbeiten
name = profil_row["name"] if profil_row is not None else ""
new_name = st.text_input("Dein Name", value=name)


# Interessen/Kategorien (optional)
#if "interessen" not in st.session_state:
#    st.session_state["interessen"] = []

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

# Vor dem ersten Zugriff auf die Erlebnisse:
if "lustigstes_erlebnis" not in st.session_state:
    st.session_state["lustigstes_erlebnis"] = ""
if "liebstes_erlebnis" not in st.session_state:
    st.session_state["liebstes_erlebnis"] = ""

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

#Alle Änderungen im data.csv speichern
if st.button("Profil speichern"):
    #Erstelle das Dictionary 'profil' mit den aktuellen Daten
    profil_dict = {
        "timestamp": pd.Timestamp.now(),
        "name": st.session_state.get("name", ""),
        "interessen": ", ".join(st.session_state.get("interessen", [])),
        "lustigstes_erlebnis": st.session_state.get("lustigstes_erlebnis", ""),
        "liebstes_erlebnis": st.session_state.get("liebstes_erlebnis", "")
    }
# Speichere die Daten persistent mit DataManager
    from utils.data_manager import DataManager
    DataManager().append_record(session_state_key="data_df", record_dict=profil_dict)

    st.success("Die Spieldaten wurden gespeichert!")

# --- Navigation ---
st.divider()
if st.button("Zurück zur Startseite"):
    st.switch_page("Start.py")