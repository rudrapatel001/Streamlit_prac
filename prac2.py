import streamlit as st

st.title("Video Game Preference App")

if st.button("Start Game Setup"):
    st.success("Loading your game setup...")

add_dlc = st.checkbox("Add DLC/Expansion Pack")

if add_dlc:
    st.write("DLC added to your setup")

platform = st.radio("Choose your gaming platform:", ["PC", "PlayStation", "Xbox", "Nintendo"])
st.write(f"Selected platform: {platform}")

genre = st.selectbox("Choose your favorite genre:", ["Action", "RPG", "Strategy", "Adventure", "Sports"])
st.write(f"Selected genre: {genre}")

difficulty = st.slider("Select difficulty level", 1, 10, 5)
st.write(f"Selected difficulty level: {difficulty}")

hours = st.number_input("How many hours do you play weekly?", min_value=1, max_value=100, step=1)
st.write(f"You play approximately {hours} hours/week")

username = st.text_input("Enter your gamer tag")
if username:
    st.write(f"Welcome, {username}! Let's get you into the game!")

dob = st.date_input("Select your date of birth")
st.write(f"Date of Birth: {dob}")
