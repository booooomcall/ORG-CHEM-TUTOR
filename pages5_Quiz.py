import streamlit as st

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
