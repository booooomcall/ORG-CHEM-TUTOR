import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Organic Chemistry Tutor", page_icon="🧪", layout="wide")

# Sidebar navigation
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Chemical_structure.svg/1024px-Chemical_structure.svg.png", width=100)
    st.markdown("## 🧪 Chemistry Tutor")
    st.page_link("app.py", label="🏠 Home")
    st.page_link("pages/2_Functional_Groups.py", label="🧬 Functional Groups")
    st.page_link("pages/3_IUPAC_Naming.py", label="📖 IUPAC Naming")
    st.page_link("pages/4_Homologous_Series.py", label="📈 Homologous Series")
    st.page_link("pages/5_Quiz.py", label="🧠 Quiz")

# Load styles
style_path = Path("assets/styles.css")
if style_path.exists():
    with open(style_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Welcome message
st.title("Welcome to Organic Chemistry Tutor 👨‍🔬")
st.write("Use the sidebar to explore lessons and activities.")
