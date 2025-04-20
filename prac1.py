import streamlit as st

st.title("Hello world")

st.subheader("Streamlit App")

st.text("Welcome to your first interative app")

st.write("Chooose your fav. Game")

Game = st.selectbox("Your fav game: ", ["Gta v", "Elden Rings", "Minecraft", "Genshin Impact"])

st.write(f"Your choose {Game}. Excellent choise")
if Game:
    st.success("Your Game is Starting...")