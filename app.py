import streamlit as st
from io import BytesIO
import qrcode

# App setup
st.set_page_config(page_title="Organic Chemistry Tutor", page_icon="🧪", layout="wide")

# Sidebar setup
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Chemical_structure.svg/1024px-Chemical_structure.svg.png", width=100)
st.sidebar.title("🧪 Chemistry Tutor")
menu = st.sidebar.selectbox("Choose a topic", [
    "🏠 Home",
    "🧬 Functional Groups",
    "🔤 IUPAC Naming",
    "📈 Homologous Series",
    "🔀 Isomers",
    "🧠 Quiz",
    "📩 Feedback"
])

# 🏠 HOME PAGE
if menu == "🏠 Home":
    st.title("🏠 Welcome to Organic Chemistry Tutor")
    st.markdown("""
This app helps SS2 students master key concepts in organic chemistry:

- 🧬 Functional Groups  
- 🔤 IUPAC Naming  
- 📈 Homologous Series  
- 🔀 Isomers  
- 🧠 Quiz  
- 📩 Feedback

Use it to study, revise, or explore chemical structures interactively!
""")
    st.subheader("📱 Scan to open this app:")
    qr = qrcode.make("https://org-chem-tutor-f9xcxbghjkvxkyutiwixwr.streamlit.app/")
    buf = BytesIO(); qr.save(buf, format="PNG")
    st.image(buf.getvalue(), width=200)

# 🧬 FUNCTIONAL GROUPS
elif menu == "🧬 Functional Groups":
    st.title("🧬 Functional Groups")

    groups = {
        "Alkane": ["C–C", "Ethane (C2H6)", "https://chem.libretexts.org/@api/deki/files/11080/alkane.png"],
        "Alkene": ["C=C", "Ethene (C2H4)", "https://chem.libretexts.org/@api/deki/files/11081/alkene.png"],
        "Alkyne": ["C≡C", "Ethyne (C2H2)", "https://chem.libretexts.org/@api/deki/files/11082/alkyne.png"],
        "Alcohol": ["-OH", "Ethanol (C2H5OH)", "https://www.chemguide.co.uk/organicprops/alcohols/ethanolmolec.png"],
        "Aldehyde": ["-CHO", "Ethanal (CH3CHO)", "https://chem.libretexts.org/@api/deki/files/11084/aldehyde.png"],
        "Ketone": ["C=O", "Propanone (CH3COCH3)", "https://chem.libretexts.org/@api/deki/files/11085/ketone.png"],
        "Carboxylic Acid": ["-COOH", "Ethanoic acid (CH3COOH)", "https://chem.libretexts.org/@api/deki/files/11086/carboxylicacid.png"],
        "Ester": ["-COO-", "Methyl ethanoate", "https://chem.libretexts.org/@api/deki/files/11087/ester.png"],
        "Amine": ["-NH2", "Methylamine (CH3NH2)", "https://chem.libretexts.org/@api/deki/files/11088/amine.png"]
    }

    for name, (group, example, img_url) in groups.items():
        with st.expander(name):
            st.image(img_url, width=300, caption=f"{example} structure")
            st.markdown(f"**Group:** `{group}`")
            st.markdown(f"**Example:** {example}")

# 🔤 IUPAC NAMING
elif menu == "🔤 IUPAC Naming":
    st.title("🔤 IUPAC Naming of Compounds")
    st.markdown("Enter a common organic compound formula to identify its IUPAC name.")

    examples = {
        "CH3CH2OH": "Ethanol – Alcohol with two carbon atoms.",
        "CH3COOH": "Ethanoic Acid – Carboxylic acid with two carbon atoms.",
        "CH4": "Methane – Simplest alkane.",
        "C2H4": "Ethene – Two-carbon alkene.",
        "C2H2": "Ethyne – Two-carbon alkyne.",
        "CH3CHO": "Ethanal – Aldehyde with two carbon atoms."
    }

    user_input = st.text_input("Enter formula (e.g. CH3COOH):")
    if user_input:
        st.info(examples.get(user_input.strip(), "❌ Not in database. Try a common organic compound."))

# 📈 HOMOLOGOUS SERIES
elif menu == "📈 Homologous Series":
    st.title("📈 Homologous Series")
    st.markdown("Homologous series share the same functional group and follow a pattern.")

    n = st.slider("Select the number of carbon atoms (n):", 1, 10, 1)
    st.markdown(f"- **Alkane** → C{n}H{2*n + 2}")
    st.markdown(f"- **Alkene** → C{n}H{2*n}")
    st.markdown(f"- **Alkyne** → {'Invalid for n < 2' if n < 2 else f'C{n}H{2*n - 2}'}")
    st.markdown(f"- **Alcohol** → C{n}H{2*n + 1}OH")

# 🔀 ISOMERS
elif menu == "🔀 Isomers":
    st.title("🔀 Meet the Twins: Isomers Explained")
    st.markdown("""
**Isomers** have the **same molecular formula** but **different structures or arrangements**.

### 🧱 Structural Isomers:
- **Chain Isomers** – Butane vs Isobutane
- **Position Isomers** – Butan-1-ol vs Butan-2-ol
- **Functional Isomers** – Alcohol vs Ether

![Chain Isomers](https://chem.libretexts.org/@api/deki/files/11070/clipboard_e0d7a06c176445c5ef94eec70d233c259.png)

---

### 🔄 Stereoisomers:
- **Geometric Isomers** – cis-but-2-ene vs trans-but-2-ene
- **Optical Isomers** – Lactic acid mirror images

![Cis-Trans](https://www.chemistrysteps.com/wp-content/uploads/2020/07/Cis-and-Trans-Isomers.png)

| Type       | Description                  | Example                 |
|------------|------------------------------|--------------------------|
| Chain      | Carbon skeleton differences   | Butane vs Isobutane      |
| Position   | Group position changes        | Butan-1-ol vs Butan-2-ol |
| Functional | Functional group differences  | Alcohol vs Ether         |
| Geometric  | Spatial arrangement (double bond) | Cis vs Trans Butene  |
| Optical    | Non-superimposable mirror images | Lactic acid isomers  |
""")

# 🧠 QUIZ
elif menu == "🧠 Quiz":
    st.title("🧠 Organic Chemistry Quiz")

    questions = [
        {"q":"General formula for alkanes?", "a":"CₙH₂ₙ₊₂", "opts":["CₙH₂ₙ", "CₙH₂ₙ₊₂", "CₙH₂ₙ₋₂"]},
        {"q":"Functional group in ethanol?", "a":"Alcohol", "opts":["Alkane", "Alcohol", "Ester"]},
        {"q":"Triple bond compound?", "a":"Alkyne", "opts":["Alkane", "Alkene", "Alkyne"]},
        {"q":"Suffix for aldehyde?", "a":"-al", "opts":["-ol", "-al", "-one"]},
        {"q":"Which is a carboxylic acid?", "a":"CH3COOH", "opts":["CH3OH", "CH3CH3", "CH3COOH"]},
    ]

    score = 0
    for i, q in enumerate(questions):
        st.subheader(f"{i+1}. {q['q']}")
        user_answer = st.radio("Choose one:", q["opts"], key=i, index=None)
        if user_answer:
            if user_answer == q["a"]:
                st.success("✅ Correct!")
                score += 1
            else:
                st.error(f"❌ Wrong. Correct answer: {q['a']}")

    st.markdown(f"### 🏁 Final Score: **{score}/{len(questions)}**")

# 📩 FEEDBACK
elif menu == "📩 Feedback":
    st.title("📩 Feedback & Suggestions")
    st.markdown("We’d love to hear from you. Please fill out this short form:")
    st.components.v1.iframe(
        "https://docs.google.com/forms/d/e/1FAIpQLSdZrs0rEmICl64s8OebmvbB4T-6qf4V8O4T2vKo2CFqFi6sjw/viewform?embedded=true",
        height=700
    )
