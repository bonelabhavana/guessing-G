import streamlit as st
import random

st.title("🎯 Number Guessing Game")

# Initialize or reset session state
if "number_to_guess" not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 100)
if "game_over" not in st.session_state:
    st.session_state.game_over = False

st.write("I'm thinking of a number between 1 and 100. Can you guess it?")

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Guess"):
    if st.session_state.game_over:
        st.warning("Game is already over. Press Reset to play again.")
    else:
        if guess < st.session_state.number_to_guess:
            st.info("Too low!")
        elif guess > st.session_state.number_to_guess:
            st.info("Too high!")
        else:
            st.success("🎉 Congratulations! You guessed the number!")
            st.session_state.game_over = True

if st.button("Reset Game"):
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.game_over = False
    st.rerun()

