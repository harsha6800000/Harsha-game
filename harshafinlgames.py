import streamlit as st
import random

# Format the title with spacing (simulating center + bold)
def format_text(text, width=50):
    return f"**{text.center(width)}**"

# Start the game when the app loads
if "number_to_guess" not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.max_guesses = 15
    st.session_state.guess_count = 0
    st.session_state.playing = True
    st.session_state.result = ""

st.write(format_text("NRE A KUNO NRE...PARA NI"))

def reset_game():
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.guess_count = 0
    st.session_state.playing = True
    st.session_state.result = ""

if st.session_state.playing:
    st.write("\n🎯 de 1 r pe 100 r vitrt nmbr eta vabek.")
    st.write(f"tuhak {st.session_state.max_guesses} bar chnch dm vbba...para jdi vbi uilo!")

    guess = st.number_input("👉 Number de ko:", min_value=1, max_value=100, step=1, key="guess_input")

    if st.button("📤 Submit guess"):
        st.session_state.guess_count += 1
        count = st.session_state.guess_count
        guess_val = int(guess)
        secret = st.session_state.number_to_guess

        if count == 5:
            st.warning(f"\nei {count}bar hl a....nhbo a haka tr darai..ko holio aro: ")

        if guess_val < secret:
            st.info("🔻 besi xoru hy gl haka!")
        elif guess_val > secret:
            st.info("🔺 besi vbsa😒!")
        else:
            st.success(f"✅ amr eao sb janne njna ktha ni haka.... {count} bar t holio miloisi.")
            st.session_state.playing = False

        if count >= st.session_state.max_guesses and guess_val != secret:
            st.error(f"😢 nlge ja khelba....ghume thk {secret}bar dlu a kba.")
            st.session_state.playing = False

else:
    again = st.radio("🔁 khlbi na ki aro?", ["Yes", "No"], key="play_again")
    if again.lower() == "yes":
        if st.button("Play Again"):
            reset_game()
    else:
        st.write("👋 ja hb ja kam ni")