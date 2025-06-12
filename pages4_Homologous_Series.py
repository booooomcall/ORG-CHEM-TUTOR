import streamlit as st

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
