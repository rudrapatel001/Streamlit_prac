import streamlit as st

st.title("Video Game Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Action Games")
    st.image("https://images.unsplash.com/photo-1580128637421-c477fa0cda5d?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", width=200)
    vote1 = st.button("Vote Action Games")

with col2:
    st.header("Adventure Games")
    st.image("https://images.unsplash.com/photo-1613336026701-7c6fdd7982a0?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", width=200)
    vote2 = st.button("Vote Adventure Games")

if vote1:
    st.success("Thanks for voting Action Games")
elif vote2:
    st.success("Thanks for voting Adventure Games")

# Sidebar inputs
name = st.sidebar.text_input("Enter your gamer tag")
game = st.sidebar.selectbox("Choose your favorite genre", ["Action", "Adventure", "RPG", "Sports", "Strategy"])
if name:
    st.write(f"Welcome **{name}**! Your favorite genre is **{game}**.")

# Instructions section
with st.expander("📜 Show Game Setup Instructions"):
    st.write("""
    1. Choose your gaming platform.
    2. Install your favorite game.
    3. Configure settings and controls.
    4. Enjoy and level up!
    """)

# Some Markdown fun
st.markdown('# Welcome to the GameZone Portal')
st.markdown('> "Gaming is not just a hobby, it’s a lifestyle."')