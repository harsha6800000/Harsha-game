import streamlit as st
import random

# Game state variables
if "number_to_guess" not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.guess_count = 0
    st.session_state.max_guesses = 15
    st.session_state.game_over = False
    st.session_state.message = ""
    st.session_state.show_restart = False

st.title("🎯 NRE A KUNO NRE...PARA NI")
st.markdown("de eta nmbr vabek **1 r pe 100** r vitrt")

# Input from user (if game is not over)
if not st.session_state.game_over:
    guess = st.number_input(f"🔢 chnch no {st.session_state.guess_count + 1} de ko:", min_value=1, max_value=100, step=1)
    if st.button("🚀 etut tipi d "):
        st.session_state.guess_count += 1

        if guess < st.session_state.number_to_guess:
            st.session_state.message = "🔻 besi xoru hy gl haka!"
        elif guess > st.session_state.number_to_guess:
            st.session_state.message = "🔺 besi vbsa😒!"
        else:
            st.session_state.message = f"✅ amr eao sb janne njna ktha ni haka.... {st.session_state.guess_count} bar t holio miloisi."
            st.session_state.game_over = True
            st.session_state.show_restart = True

        if st.session_state.guess_count == 5:
            st.info("😨 ei 5 bar hl a....nhbo a haka tr darai..ko holio aro:")

        if st.session_state.guess_count >= st.session_state.max_guesses and not st.session_state.game_over:
            st.session_state.message = f"😢 nlge ja khelba....ghume thk {st.session_state.number_to_guess}bar dlu a kba."
            st.session_state.game_over = True
            st.session_state.show_restart = True

# Show message
if st.session_state.message:
    st.markdown(f"**{st.session_state.message}**")

# Restart option
if st.session_state.show_restart:
    if st.button("🔁 khlbi na ki aro?"):
        # Reset game state
        st.session_state.number_to_guess = random.randint(1, 100)
        st.session_state.guess_count = 0
        st.session_state.game_over = False
        st.session_state.message = ""
        st.session_state.show_restart = False