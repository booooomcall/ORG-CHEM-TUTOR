import streamlit as st
from io import BytesIO
import qrcode
import random
import time
import datetime

# App setup
st.set_page_config(page_title="Organic Chemistry Tutor", page_icon="🧪", layout="wide")

# Sidebar setup
st.sidebar.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHSwe3LbY4YbdwAcbM77kkHb4SA45mBrWQ0Q&s", width=100)
st.sidebar.title("🧪 Chemistry Tutor")
menu = st.sidebar.selectbox("Choose a topic", [
    "🏠 Home",
    "🧬 Functional Groups",
    "🔤 IUPAC Naming",
    "📈 Homologous Series",
    "🔀 Isomers",
    "🧠 Quiz",
    "📩 Feedback", 
    "🗕️ Daily Challenge",   
    "📘 SS2 Glossary",      
    "🎮 Name It Fast Game"
])

# Initialize game session state
if 'scoreboard' not in st.session_state:
    st.session_state.scoreboard = []
if 'current_score' not in st.session_state:
    st.session_state.current_score = 0
if 'start_time' not in st.session_state:
    st.session_state.start_time = 0
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
if 'current_question' not in st.session_state:
    st.session_state.current_question = ""

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
- 🗕️ Daily Challenge
- 📘 SS2 Glossary
    
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

![Chain Isomers](https://www.science-revision.co.uk/images/hexane%20and%20branched%20chainv2.jpg)

---

### 🔄 Stereoisomers:
- **Geometric Isomers** – cis-but-2-ene vs trans-but-2-ene
- **Optical Isomers** – Lactic acid mirror images

![Cis-Trans]https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQW-hgq77ZDJEN8DZxSCR92Lf068LewaGpv9Q&s)

| Type       | Description                  | Example                 |
|------------|------------------------------|--------------------------|
| Chain      | Carbon skeleton differences   | Butane vs Isobutane      |
| Position   | Group position changes        | Butan-1-ol vs Butan-2-ol |
| Functional | Functional group differences  | Alcohol vs Ether         |
| Geometric  | Spatial arrangement (double bond) | Cis vs Trans Butene  |
| Optical    | Non-superimposable mirror images | Lactic acid isomers  |
""")

# 🎮 NAME IT FAST GAME
elif menu == "🎮 Name It Fast Game":
    st.title("🎮 Name It Fast: Chemistry Edition")

    mode = st.selectbox("Choose Game Mode:", ["Functional Group Flash", "IUPAC Sprint"])

    questions_data = {
        "Functional Group Flash": [
            {"q": "-OH", "a": "Alcohol"},
            {"q": "-COOH", "a": "Carboxylic Acid"},
            {"q": "-CHO", "a": "Aldehyde"},
            {"q": "-NH2", "a": "Amine"},
            {"q": "C=C", "a": "Alkene"}
        ],
        "IUPAC Sprint": [
            {"q": "CH3COOH", "a": "Ethanoic Acid"},
            {"q": "CH3CH2OH", "a": "Ethanol"},
            {"q": "C2H4", "a": "Ethene"},
            {"q": "CH3CHO", "a": "Ethanal"},
            {"q": "CH4", "a": "Methane"}
        ]
    }

    if st.button("Start Game") or st.session_state.game_started:
        if not st.session_state.game_started:
            st.session_state.game_started = True
            st.session_state.current_score = 0
            st.session_state.start_time = time.time()
            st.session_state.questions = random.sample(questions_data[mode], len(questions_data[mode]))
            st.session_state.current_index = 0

        if st.session_state.current_index < len(st.session_state.questions):
            current = st.session_state.questions[st.session_state.current_index]
            st.subheader(f"What does this represent: **{current['q']}**")
            answer = st.text_input("Your Answer:", key='answer_input')
            if st.button("Submit"):
                if answer.strip().lower() == current['a'].lower():
                    st.success("Correct!")
                    st.session_state.current_score += 1
                else:
                    st.error(f"Wrong! Correct answer: {current['a']}")
                st.session_state.current_index += 1
                st.experimental_rerun()
        else:
            duration = round(time.time() - st.session_state.start_time, 2)
            st.balloons()
            st.success(f"Game Over! Score: {st.session_state.current_score}/{len(st.session_state.questions)} in {duration} seconds")
            st.session_state.scoreboard.append({
                "mode": mode,
                "score": st.session_state.current_score,
                "time": duration
            })
            st.session_state.game_started = False

    if st.session_state.scoreboard:
        st.subheader("🏋️ Your Score History")
        for entry in st.session_state.scoreboard[::-1]:
            st.markdown(f"- Mode: **{entry['mode']}** | Score: **{entry['score']}** | Time: **{entry['time']}s**")

# 📩 FEEDBACK
elif menu == "📩 Feedback":
    st.title("📩 Feedback & Suggestions")
    st.markdown("We’d love to hear from you. Please fill out this short form:")
    st.components.v1.iframe(
        "https://docs.google.com/forms/d/15UDx8Bd7edEzJCh3va_NWxFzkFgxbl6hzt7HBLxrLIs/edit",
        height=700
    )

# 🗕️ DAILY CHALLENGE
elif menu == "🗕️ Daily Challenge":
    st.title("📅 Daily Challenge")
    today = datetime.date.today()
    seed = today.toordinal()
    random.seed(seed)

    daily_questions = [
        {"q": "Which functional group is present in propanoic acid?", "a": "Carboxylic Acid", "opts": ["Alcohol", "Carboxylic Acid", "Ketone"]},
        {"q": "What is the suffix for an alcohol?", "a": "-ol", "opts": ["-one", "-al", "-ol"]},
        {"q": "What is the IUPAC name for CH3CH=CH2?", "a": "Propene", "opts": ["Propane", "Propene", "Propyne"]},
        {"q": "Which group is represented by -COOH?", "a": "Carboxylic Acid", "opts": ["Alcohol", "Carboxylic Acid", "Amine"]},
        {"q": "What type of isomerism involves spatial arrangement around double bonds?", "a": "Geometric", "opts": ["Chain", "Geometric", "Optical"]}
    ]
    challenge = random.choice(daily_questions)
    st.subheader(challenge["q"])
    choice = st.radio("Choose your answer:", challenge["opts"])
    if st.button("Submit Answer"):
        if choice == challenge["a"]:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Incorrect. The correct answer is: {challenge['a']}")

# 📘 SS2 GLOSSARY
elif menu == "📘 SS2 Glossary":
    st.title("📘 SS2 Chemistry Glossary")
    terms = {
        "Homologous Series": "A series of organic compounds with the same functional group and similar chemical properties.",
        "Isomers": "Compounds with the same molecular formula but different structural formulas.",
        "Functional Group": "A specific group of atoms that determines the characteristic reactions of a compound.",
        "Alkane": "A saturated hydrocarbon with single bonds only.",
        "Alkene": "An unsaturated hydrocarbon containing at least one double bond.",
        "Alkyne": "An unsaturated hydrocarbon containing at least one triple bond.",
        "IUPAC": "International Union of Pure and Applied Chemistry – provides naming rules.",
        "Esterification": "A reaction between a carboxylic acid and alcohol to form an ester.",
        "Addition Reaction": "Reaction where atoms are added to a double or triple bond.",
        "Substitution Reaction": "Reaction where one atom or group replaces another in a compound."
    }

    search = st.text_input("Search glossary:")
    for term, definition in terms.items():
        if search.lower() in term.lower():
            with st.expander(term):
                st.write(definition)
