import streamlit as st

st.title("📖 IUPAC Naming")

examples = {
    "CH3COOH": "Ethanoic Acid – carboxylic acid with 2 carbons",
    "C2H5OH": "Ethanol – 2-carbon alcohol",
    "CH3CH2CH3": "Propane – 3-carbon alkane",
    "CH3CH=CH2": "Propene – 3-carbon alkene"
}

formula = st.text_input("Enter a compound formula:")
if formula:
    st.info(examples.get(formula.strip(), "Compound not in sample database."))

import streamlit as st

def show():
    st.title("IUPAC")
    st.write("Welcome to Organic Chemistry Tutor.")