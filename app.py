import streamlit as st
from io import BytesIO
import qrcode

# Set app config
st.set_page_config(page_title="Organic Chemistry Tutor", page_icon="🧪", layout="wide")

# Sidebar navigation
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Chemical_structure.svg/1024px-Chemical_structure.svg.png", width=100)
st.sidebar.title("🧪 Chemistry Tutor")

menu = st.sidebar.selectbox("Choose a topic", [
    "🏠 Home",
    "🧬 Functional Groups",
    "🔤 IUPAC Naming",
    "📈 Homologous Series",
    "🔀 Isomers",
    "🧠 Quiz"
])

# 🏠 HOME
if menu == "🏠 Home":
    st.title("🏠 Welcome to Organic Chemistry Tutor")
    st.markdown("""
    This app helps SS2 students master key concepts in organic chemistry:
    - Functional Groups
    - IUPAC Naming
    - Homologous Series
    - Isomers
    - Practice Quiz
    """)
    st.subheader("📱 Scan to access this app on any device:")
    qr = qrcode.make("https://org-chem-tutor-f9xcxbghjkvxkyutiwixwr.streamlit.app/")
    buf = BytesIO()
    qr.save(buf, format="PNG")
    st.image(buf.getvalue(), width=200)

# 🧬 FUNCTIONAL GROUPS
elif menu == "🧬 Functional Groups":
    st.title("🧬 Functional Groups")
    groups = {
        "Alkane": ["C–C", "Ethane (C2H6)", "Single bonds only; saturated hydrocarbon."],
        "Alkene": ["C=C", "Ethene (C2H4)", "Double bond present; unsaturated."],
        "Alkyne": ["C≡C", "Ethyne (C2H2)", "Triple bond; highly reactive."],
        "Alcohol": ["-OH", "Ethanol (C2H5OH)", "Hydroxyl group."],
        "Aldehyde": ["-CHO", "Ethanal (CH3CHO)", "Carbonyl at end of chain."],
        "Ketone": ["C=O", "Propanone (CH3COCH3)", "Carbonyl group in chain."],
        "Carboxylic Acid": ["-COOH", "Ethanoic acid (CH3COOH)", "Acidic; forms esters."],
        "Ester": ["-COO-", "Methyl ethanoate", "Formed from acid + alcohol."],
        "Amine": ["-NH2", "Methylamine (CH3NH2)", "Basic nitrogen group."]
    }
    for name, (group, example, desc) in groups.items():
        with st.expander(name):
            st.markdown(f"**Group:** `{group}`")
            st.markdown(f"**Example:** {example}")
            st.caption(desc)

# 🔤 IUPAC NAMING
elif menu == "🔤 IUPAC Naming":
    st.title("🔤 IUPAC Naming")
    st.markdown("Enter a common compound formula to identify its IUPAC name.")
    examples = {
        "CH3CH2OH": "Ethanol – Alcohol with two carbon atoms.",
        "CH3COOH": "Ethanoic Acid – Carboxylic acid with two carbon atoms.",
        "CH4": "Methane – Simplest alkane.",
        "C2H4": "Ethene – Two-carbon alkene.",
        "C2H2": "Ethyne – Two-carbon alkyne.",
        "CH3CHO": "Ethanal – Aldehyde with two carbon atoms."
    }
    inp = st.text_input("Formula (e.g. CH3COOH):")
    if inp:
        st.info(examples.get(inp.strip(), "❌ Not in database. Try a common organic molecule."))

# 📈 HOMOLOGOUS SERIES
elif menu == "📈 Homologous Series":
    st.title("📈 Homologous Series")
    n = st.slider("Select number of carbon atoms (n):", 1, 10, 1)
    st.subheader("General Formulas:")
    st.markdown(f"- **Alkanes**: C{n}H{2*n + 2}")
    st.markdown(f"- **Alkenes**: C{n}H{2*n}")
    st.markdown(f"- **Alkynes**: {'Invalid for n<2' if n < 2 else f'C{n}H{2*n - 2}'}")
    st.markdown(f"- **Alcohols**: C{n}H{2*n + 1}OH")

# 🔀 ISOMERS
elif menu == "🔀 Isomers":
    st.title("🔀 Meet the Twins: Isomers Explained")
    st.markdown("""
**Isomers** have the **same molecular formula** but **different structures**.

### 🧱 Structural Isomers:
- **Chain** – Butane vs Isobutane
- **Position** – Butan-1-ol vs Butan-2-ol
- **Functional** – Alcohol vs Ether

![Chain Isomers](https://chem.libretexts.org/@api/deki/files/11070/clipboard_e0d7a06c176445c5ef94eec70d233c259.png)

### 🔄 Stereoisomers:
- **Geometric (Cis-Trans)** – cis-but-2-ene vs trans-but-2-ene
- **Optical** – Lactic acid enantiomers

![Cis-Trans](https://www.chemistrysteps.com/wp-content/uploads/2020/07/Cis-and-Trans-Isomers.png)

| Type       | Description                  | Example                 |
|------------|------------------------------|--------------------------|
| Chain      | Carbon skeleton changes       | Butane vs Isobutane      |
| Position   | Group position changes        | Butan-1-ol vs Butan-2-ol |
| Functional | Functional group changes      | Alcohol vs Ether         |
| Geometric  | Spatial around double bond    | Cis vs Trans Butene      |
| Optical    | Mirror image molecules        | Lactic Acid isomers      |
""")

# 🧠 QUIZ
elif menu == "🧠 Quiz":
    st.title("🧠 Organic Chemistry Quiz")
    questions = [
        {"q":"General formula for alkanes?", "a":"CₙH₂ₙ₊₂", "opts":["CₙH₂ₙ", "CₙH₂ₙ₊₂", "CₙH₂ₙ₋₂"]},
        {"q":"Functional group in ethanol?", "a":"Alcohol", "opts":["Alkane", "Alcohol", "Ester"]},
        {"q":"Triple bond compound?", "a":"Alkyne", "opts":["Alkane", "Alkene", "Alkyne"]},
        {"q":"Suffix for aldehyde?", "a":"-al", "opts":["-ol", "-al", "-one"]},
        {"q":"Position isomers differ in?", "a":"Functional group location", "opts":["C-chain length", "Group type", "Functional group location"]},
        {"q":"Which is a carboxylic acid?", "a":"CH3COOH", "opts":["CH3OH", "CH3CH3", "CH3COOH"]},
        {"q":"Butane and Isobutane are?", "a":"Chain Isomers", "opts":["Functional Isomers", "Geometric Isomers", "Chain Isomers"]},
        {"q":"cis and trans forms?", "a":"Geometric Isomers", "opts":["Structural Isomers", "Geometric Isomers", "Optical Isomers"]},
        {"q":"Test for unsaturation?", "a":"Bromine water", "opts":["HCl", "Bromine water", "NaOH"]},
        {"q":"C2H5OH oxidized gives?", "a":"Ethanoic acid", "opts":["Ethene", "Ethanol", "Ethanoic acid"]},
        {"q":"Alkene general formula?", "a":"CₙH₂ₙ", "opts":["CₙH₂ₙ", "CₙH₂ₙ₋₂", "CₙH₂ₙ₊₂"]},
        {"q":"Ethanoic acid belongs to?", "a":"Carboxylic acids", "opts":["Alcohols", "Carboxylic acids", "Ketones"]},
        {"q":"OH group is in?", "a":"Alcohol", "opts":["Aldehyde", "Alkene", "Alcohol"]},
        {"q":"Ketone example?", "a":"Propanone", "opts":["Methane", "Propanone", "Ethanol"]},
        {"q":"CH3NH2 is an?", "a":"Amine", "opts":["Ester", "Amine", "Alcohol"]}
    ]
    score = 0
    for i, q in enumerate(questions):
        st.subheader(f"{i+1}. {q['q']}")
        response = st.radio("Choose:", q["opts"], key=f"q{i}", index=None)
        if response:
            if response == q["a"]:
                st.success("✅ Correct!")
                score += 1
            else:
                st.error(f"❌ Incorrect. Correct answer: {q['a']}")
    st.markdown(f"### 🏁 Final Score: **{score}/{len(questions)}**")
