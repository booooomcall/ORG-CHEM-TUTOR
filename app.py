import streamlit as st
from pathlib import Path
import json
import qrcode
from io import BytesIO

st.set_page_config(page_title="Organic Chemistry Tutor", page_icon="🧪", layout="wide")

# Load styles
style = Path("assets/styles.css")
if style.exists():
    st.markdown(f"<style>{style.read_text()}</style>", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Chemical_structure.svg/1024px-Chemical_structure.svg.png", width=100)
st.sidebar.markdown("## 🧪 Chemistry Tutor")
page = st.sidebar.selectbox("📚 Select a Topic", ["🏠 Home", "🧠 Quiz", "📘 SS2 Resources"])

# Home Page with QR code
if page == "🏠 Home":
    st.title("🏠 Welcome to Organic Chemistry Tutor")
    st.write("Scan the QR code to open this app on mobile or share it:")
    url = st.experimental_get_url()
    img = qrcode.make(url)
    buf = BytesIO(); img.save(buf, format="PNG")
    st.image(buf, width=200, caption="🔗 App Link")

# Quiz Page with 15 questions
elif page == "🧠 Quiz":
    st.title("🧠 SS2 Organic Chemistry Quiz")
    questions = [
        {"q":"Formula of ethanol?", "a":"C2H5OH", "opts":["CH4","C2H5OH","C2H4"]},
        {"q":"Which group is -COOH?", "a":"Carboxylic Acid", "opts":["Alcohol","Ketone","Carboxylic Acid"]},
        {"q":"General formula for alkenes?", "a":"CnH2n", "opts":["CnH2","CnH2n","CnH2n+2"]},
        {"q":"Test for unsaturation?", "a":"Decolours Br₂", "opts":["Gives green ppt","Decolours Br₂","Turns red"]},
        {"q":"Functional group in propanone?", "a":"Ketone", "opts":["Alcohol","Aldehyde","Ketone"]},
        {"q":"Ethanol oxidised gives?", "a":"Ethanoic Acid", "opts":["Ethanal","Ethanoic Acid","Methanol"]},
        {"q":"Homologous difference between members?", "a":"CH₂ group", "opts":["H₂O","CH₂ group","CO group"]},
        {"q":"Markovnikov’s rule applies to?", "a":"Alkenes", "opts":["Alkanes","Alkenes","Alcohols"]},
        {"q":"Test for phenol?", "a":"FeCl₃ gives purple", "opts":["Br₂ gives decolour","FeCl₃ gives purple","KMnO₄ brown"]},
        {"q":"Ester from acid + alcohol is called?", "a":"Esterification", "opts":["Oxidation","Esterification","Hydrolysis"]},
        {"q":"Carboxylic acid equation pH?", "a":"<7", "opts":[">7","7","<7"]},
        {"q":"Alkane general formula?", "a":"CnH2n+2", "opts":["CnH2n+2","CnH2n","CnH2n-2"]},
        {"q":"Which has triple bond?", "a":"Alkyne", "opts":["Alkyne","Alkene","Alkane"]},
        {"q":"Aromatic ring is?", "a":"Benzene", "opts":["Cyclohexane","Benzene","Hexane"]},
        {"q":"IUPAC suffix for aldehyde?", "a":"-al", "opts":["-one","-al","-ol"]},
    ]
    score = 0
    for idx, q in enumerate(questions):
        answer = st.radio(q["q"], q["opts"], key=f"q{idx}")
        if answer:
            if answer == q["a"]:
                st.success("Correct ✅")
                score += 1
            else:
                st.error(f"Wrong ❌ Answer: {q['a']}")
    st.markdown(f"### Total Score: {score} / {len(questions)}")

# SS2 Resources Page
elif page == "📘 SS2 Resources":
    st.title("📘 SS2 Organic Chemistry Resources")
    st.markdown("""
### 🧬 Key Topics Covered:
- **Hydrocarbons** – Alkanes, Alkenes, Alkynes, Aromatics; isomerism, general formulas, tests.
- **Alcohols & Ethers** – properties, uses, hydrogen bonding.
- **Aldehydes & Ketones** – carbonyl chemistry, Tollens’, Brady’s tests.
- **Carboxylic Acids & Esters** – naming, reactions including esterification :contentReference[oaicite:5]{index=5}.
- **Functional Groups** – including amines, amides, nitriles, epoxides :contentReference[oaicite:6]{index=6}.
- **Reactions** – substitution, addition, elimination, oxidation, reduction.
- **Practical Tests** – bromine, ferric chloride, KMnO₄.

#### 🔧 Tips for Students:
- Recognize functional groups by structure and name.
- Understand the difference between *addition* (alkene) and *substitution* (alkane) reactions.
- Learn common lab tests and the expected observations.
- Practice writing balanced equations for ester and dehydration reactions.

---

### 📘 Reference Slide:
1. SS2 Scheme includes: hydrocarbons, nomenclature, preparation, properties :contentReference[oaicite:7]{index=7}.
2. Topics like amides, aromatic chemistry, nitriles appear in curriculum :contentReference[oaicite:8]{index=8}.
3. Esters are formed from alcohols and acids, discussed in depth online :contentReference[oaicite:9]{index=9}.
""")
