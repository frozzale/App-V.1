import streamlit as st
import pandas as pd
from utils.data_manager import DataManager

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

# Profildaten laden (eigene Datei)
DataManager().load_user_data(
    session_state_key='profil_df',
    file_name='profil.csv',
    initial_value=pd.DataFrame(),
    parse_dates=['timestamp'],
    encoding='latin-1'
)
profil_df = st.session_state.get("profil_df", pd.DataFrame())

st.title("👤 Mein Spielerprofil")

# --- Profilinformationen anzeigen und bearbeiten ---
st.subheader("Profilinformationen")

data_df = st.session_state.get("data_df", pd.DataFrame())

# Hole das zuletzt gespeicherte Profil aus profil_df
if not profil_df.empty:
    profil_row = profil_df.sort_values("timestamp", ascending=False).iloc[0]
    name = profil_row["name"] if "name" in profil_row else ""
    interessen = profil_row["interessen"].split(", ") if "interessen" in profil_row and pd.notna(profil_row["interessen"]) and profil_row["interessen"] else []
    lustigstes_erlebnis = profil_row["lustigstes_erlebnis"] if "lustigstes_erlebnis" in profil_row and pd.notna(profil_row["lustigstes_erlebnis"]) else ""
    liebstes_erlebnis = profil_row["liebstes_erlebnis"] if "liebstes_erlebnis" in profil_row and pd.notna(profil_row["liebstes_erlebnis"]) else ""
else:
    name = ""
    interessen = []
    lustigstes_erlebnis = ""
    liebstes_erlebnis = ""

# Name bearbeiten
name = st.session_state.get("name", "")
new_name = st.text_input("Dein Name", value=name)


# Interessen/Kategorien (optional)
#interessen = st.session_state.get("interessen", [])

st.subheader("Lieblingskategorien")

# --- Lieblingskategorien auswählen, speichern, anzeigen und entfernen ---

alle_kategorien = [
    "Stadt", "Land", "Fluss", "Tier", "Marke", "Beruf", "Instrument", "Film", "Getränk", "Süßigkeit",
    "Olympische Disziplin", "Jugendwort", "Superkraft", "Haustiernamen", "Reiseziel", "Babynamen"
]

# Multiselect für neue Auswahl (wird erst beim Speichern übernommen)
neue_auswahl = st.multiselect(
    "Wähle deine Lieblingskategorien aus:",
    options=alle_kategorien,
    default=interessen
)

# Anzeige der aktuell gespeicherten Lieblingskategorien mit Löschen-Button
if interessen:
    st.markdown("**Deine gespeicherten Lieblingskategorien:**")
    for idx, kategorie in enumerate(interessen):
        cols = st.columns([3, 1])
        cols[0].write(kategorie)
        if cols[1].button("Löschen", key=f"del_{kategorie}_{idx}"):
            neue_interessen = interessen.copy()
            neue_interessen.pop(idx)
            profil_dict = {
                "timestamp": pd.Timestamp.now(),
                "name": name,
                "interessen": ", ".join(neue_interessen),
                "lustigstes_erlebnis": lustigstes_erlebnis,
                "liebstes_erlebnis": liebstes_erlebnis
            }
            DataManager().append_record(session_state_key="profil_df", record_dict=profil_dict)
            st.rerun()
else:
    st.markdown("_Noch keine Lieblingskategorien gespeichert._")

st.subheader("Deine Spielerlebnisse")

lustigstes = st.text_area(
    "Was war dein lustigstes Erlebnis im Spiel?:rolling_on_the_floor_laughing:",
    value=lustigstes_erlebnis,
    placeholder="Erzähle hier dein lustigstes Erlebnis ..."
)
liebstes = st.text_area(
    "Was war dein liebstes Spielerlebnis?:two_hearts:",
    value=liebstes_erlebnis,
    placeholder="Beschreibe hier dein schönstes Spielerlebnis ..."
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

st.badge("Vergiss nicht dein Profil zu speichern, bevor du die Seite verlässt!", icon="💾", color="violet")


#Alle Änderungen im profil.csv speichern
if st.button("Profil speichern"):
    profil_dict = {
        "timestamp": pd.Timestamp.now(),
        "name": new_name,
        "interessen": ", ".join(neue_auswahl),
        "lustigstes_erlebnis": lustigstes,
        "liebstes_erlebnis": liebstes
    }
    DataManager().append_record(session_state_key="profil_df", record_dict=profil_dict)
    st.success("Das Profil wurde gespeichert!")
    st.rerun()  # Seite neu laden, um Änderungen anzuzeigen

# --- Navigation ---
st.divider()
if st.button("Zurück zur Startseite"):
    st.switch_page("Start.py")