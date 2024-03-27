import streamlit as st
import random
import time

# Function to get a random choice for the gnome
def gnome_choice():
    options = ["rock", "fire", "ice"]
    random.seed(time.time())
    return random.choice(options)

# Function to check the outcome of the game
def check_winner(user_choice, gnome_choice):
    outcomes = {
        ("rock", "fire"): True,
        ("fire", "ice"): True,
        ("ice", "rock"): True
    }
    if user_choice == gnome_choice:
        return "tie"
    return outcomes.get((user_choice, gnome_choice), False)

# Main game function
def play_game():
    st.title("Rock, Fire, Ice")

    if 'name' not in st.session_state:
        st.session_state['name'] = ''

    if st.session_state['name']:
        st.write(f"Welcome back, {st.session_state['name']}!")
    else:
        name = st.text_input("What name will you use on this quest?")
        if name:
            st.session_state['name'] = name
            st.write(f"Welcome, {name}!")

    if st.button("Play Rock, Fire, Ice"):
        user_choice = st.radio("Choose your throw:", ["rock", "fire", "ice"])
        gnome_throw = gnome_choice()
        st.write(f"The gnome threw {gnome_throw}")

        if user_choice:
            result = check_winner(user_choice, gnome_throw)
            if result == "tie":
                st.write("It's a tie! Try again.")
            elif result:
                st.balloons()
                st.write("\"You won fair and square. I release you from my lair. By the following decree, reunited you will be.\"\n૮ ˆﻌˆ ა")
            else:
                st.write("You lost. You and your dog will stay forever in the gnome's meadow.")

# Display introductory message and play game button
st.write(
    "You are sitting at home coding when a gnome breaks into your room through the air vent and disappears with your dog."
    "\nWould you like to chase the gnome and save your dog?"
)

if st.button("Embark on an Adventure"):
    play_game()
else:
    st.write("Waiting for you to start the adventure...")
