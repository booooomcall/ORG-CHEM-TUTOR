import streamlit as st
import time
import random
import pandas as pd

st.title("🎯 Name It Fast!")
st.markdown("**Test your speed and knowledge in different game modes!**")

# Game Mode Selection
game_mode = st.selectbox("Choose a game mode:", [
    "Functional Groups Challenge",
    "IUPAC Naming Race",
    "Structure Matcher"
])

# Timer, Score, and History
if "score" not in st.session_state:
    st.session_state.score = 0
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "attempt_history" not in st.session_state:
    st.session_state.attempt_history = []

def start_game():
    st.session_state.score = 0
    st.session_state.start_time = time.time()
    st.session_state.attempt_history = []

# START button
if st.button("🚀 Start Game"):
    start_game()

# Main Game Logic
if st.session_state.start_time:
    elapsed_time = int(time.time() - st.session_state.start_time)
    st.markdown(f"⏱️ Time: {elapsed_time} seconds")
    st.markdown(f"🏆 Score: {st.session_state.score}")

    # Functional Groups Challenge
    if game_mode == "Functional Groups Challenge":
        fg_data = {
            "Alcohol": "-OH",
            "Carboxylic Acid": "-COOH",
            "Aldehyde": "-CHO",
            "Ketone": "C=O",
            "Ester": "-COO-",
            "Amine": "-NH₂",
        }
        question, answer = random.choice(list(fg_data.items()))
        user_input = st.text_input(f"What is the structure for **{question}**?", key=elapsed_time)
        if user_input:
            correct = user_input.strip().lower() == answer.lower()
            if correct:
                st.success("Correct!")
                st.session_state.score += 1
            else:
                st.error(f"Wrong! Correct answer: {answer}")
            st.session_state.attempt_history.append((game_mode, question, user_input, answer, correct))

    # IUPAC Naming Race
    elif game_mode == "IUPAC Naming Race":
        iupac_data = {
            "CH₄": "Methane",
            "C₂H₆": "Ethane",
            "C₃H₈": "Propane",
            "CH₃CH₂OH": "Ethanol",
            "CH₃COOH": "Ethanoic acid",
        }
        question, answer = random.choice(list(iupac_data.items()))
        user_input = st.text_input(f"Name this compound: **{question}**", key="iupac"+str(elapsed_time))
        if user_input:
            correct = user_input.strip().lower() == answer.lower()
            if correct:
                st.success("Correct!")
                st.session_state.score += 1
            else:
                st.error(f"Wrong! Correct answer: {answer}")
            st.session_state.attempt_history.append((game_mode, question, user_input, answer, correct))

    # Structure Matcher
    elif game_mode == "Structure Matcher":
        structure_data = {
            "Propene": "CH₂=CHCH₃",
            "But-2-yne": "CH₃C≡CCH₃",
            "Ethanoic acid": "CH₃COOH",
            "Methanol": "CH₃OH",
            "Butanone": "CH₃COCH₂CH₃",
        }
        question, answer = random.choice(list(structure_data.items()))
        user_input = st.text_input(f"Which compound has this structure? **{answer}**", key="matcher"+str(elapsed_time))
        if user_input:
            correct = user_input.strip().lower() == question.lower()
            if correct:
                st.success("Correct!")
                st.session_state.score += 1
            else:
                st.error(f"Wrong! Correct answer: {question}")
            st.session_state.attempt_history.append((game_mode, answer, user_input, question, correct))

# Session Score Leaderboard
st.markdown("### 🧠 Leaderboard (Local Session)")
st.markdown(f"**Your Score:** {st.session_state.score}")

# Show Attempt History Table
if st.session_state.attempt_history:
    st.markdown("### 📋 Previous Attempts")
    df = pd.DataFrame(st.session_state.attempt_history, columns=["Mode", "Question", "Your Answer", "Correct Answer", "Result"])
    df["Result"] = df["Result"].apply(lambda x: "✅" if x else "❌")
    st.dataframe(df)

# Reset
if st.button("🔄 Restart Game"):
    st.session_state.start_time = None
    st.session_state.score = 0
    st.session_state.attempt_history = []
