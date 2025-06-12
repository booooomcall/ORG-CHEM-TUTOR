import streamlit as st
from pathlib import Path
import modules.page_home as home
import modules.page_functional_groups as fg
import modules.page_iupac_naming as naming
import modules.page_homologous_series as series
import modules.page_quiz as quiz

st.set_page_config(page_title="Organic Chemistry Tutor", page_icon="🧪", layout="wide")

# Load CSS
style_path = Path("assets/styles.css")
if style_path.exists():
    with open(style_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Chemical_structure.svg/1024px-Chemical_structure.svg.png", width=100)
st.sidebar.markdown("## 🧪 Chemistry Tutor")

page = st.sidebar.selectbox("📚 Select a Topic", [
    "🏠 Home",
    "🧬 Functional Groups",
    "📖 IUPAC Naming",
    "📈 Homologous Series",
    "🧠 Quiz"
])

# Page routing
if page == "🏠 Home":
    home.show()
elif page == "🧬 Functional Groups":
    fg.show()
elif page == "📖 IUPAC Naming":
    naming.show()
elif page == "📈 Homologous Series":
    series.show()
elif page == "🧠 Quiz":
    quiz.show()
