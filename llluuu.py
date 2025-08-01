import streamlit as st

st.title("Ooo Munu")
st.write("_")  # just replicating your underscore divider

name = st.text_input("Ktha eta kng? ( 'ko' / nkbi):")

if name:  # only react once the user types something
    if name.strip().lower() == "ko":
        st.success("I love you nuu..!!")
    else:
        st.warning("De hb ja")