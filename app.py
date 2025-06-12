import streamlit as st
from pathlib import Path
import json

# Page config and styles
st.set_page_config(page_title="Organic Chemistry Tutor", page_icon="🧪", layout="wide")

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

# Pages
if page == "🏠 Home":
    st.title("🏠 Home")
    st.write("Welcome to the Organic Chemistry Tutor App!")

elif page == "🧬 Functional Groups":
    st.title("🧬 Functional Groups")
    with open("data/functional_groups.json") as f:
        groups = json.load(f)
    for group in groups:
        with st.expander(group["name"]):
            st.markdown(f"**Symbol:** `{group['symbol']}`")
            st.markdown(f"**Example:** {group['example']}")
            st.caption(group['description'])

elif page == "📖 IUPAC Naming":
    st.title("📖 IUPAC Naming")
    examples = {
        "CH3COOH": "Ethanoic Acid – 2-carbon carboxylic acid.",
        "C2H5OH": "Ethanol – 2-carbon alcohol.",
        "CH3CH2CH3": "Propane – 3-carbon alkane.",
        "CH3CH=CH2": "Propene – 3-carbon alkene."
    }
    formula = st.text_input("Enter a compound formula:")
    if formula:
        st.info(examples.get(formula.strip(), "Compound not found. Try a simpler formula."))

elif page == "📈 Homologous Series":
    st.title("📈 Homologous Series Calculator")
    n = st.slider("Number of carbon atoms (n):", 1, 10, 1)
    st.subheader("Alkanes (CnH2n+2)")
    st.code(f"C{n}H{2*n + 2}")
    st.subheader("Alkenes (CnH2n)")
    st.code(f"C{n}H{2*n}")
    st.subheader("Alkynes (CnH2n-2)")
    st.code(f"C{n}H{2*n - 2}" if n >= 2 else "Not valid for n < 2")
    st.subheader("Alcohols (CnH2n+1OH)")
    st.code(f"C{n}H{2*n + 1}OH")

elif page == "🧠 Quiz":
    st.title("🧠 Quick Quiz")
    questions = [
        {"q": "What is the formula of ethanol?", "a": "C2H5OH", "options": ["CH4", "C2H5OH", "C2H4"]},
        {"q": "Which functional group is -COOH?", "a": "Carboxylic Acid", "options": ["Alcohol", "Ketone", "Carboxylic Acid"]}
    ]
    score = 0
    for i, q in enumerate(questions):
        answer = st.radio(q["q"], q["options"], key=f"q{i}")
        if answer == q["a"]:
            st.success("✅ Correct!")
            score += 1
        else:
            st.error(f"❌ Answer: {q['a']}")
    st.markdown(f"### Final Score: {score}/{len(questions)}")
