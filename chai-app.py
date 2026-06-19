import os
import streamlit as st

st.set_page_config(page_title="Tanmay's Chai App", page_icon="☕", layout="wide")

st.markdown(
    "<h1 style='color: #8B4513; font-family: Arial, sans-serif;'>Welcome to Tanmay's Chai App! ☕</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='color: #A0522D; font-family: Arial, sans-serif;'>Discover the art of making the perfect cup of Chai and share your preferences with us!</p>",
    unsafe_allow_html=True,
)

image1 = r"C:\Users\ACER\Downloads\ChatGPT Image Jun 20, 2026, 12_55_06 AM.png"
image2 = r"C:\Users\ACER\Downloads\ChatGPT Image Jun 20, 2026, 12_53_05 AM.png"


def show_image(image_path: str, caption: str) -> None:
    if os.path.exists(image_path):
        st.image(image_path, caption=caption, use_column_width=True)
    else:
        st.warning(f"Image not found: {image_path}")

col1, col2 = st.columns(2)
with col1:
    st.header("Masala Chai")
    show_image(image1, "Masala Chai")
    vote1 = st.button("Vote for Masala Chai", key="vote1")
with col2:
    st.header("Adrak Chai")
    show_image(image2, "Adrak Chai")
    vote2 = st.button("Vote for Adrak Chai", key="vote2")

if vote1:
    st.success("Thank you for voting for Masala Chai! Your vote has been counted. ☕")
elif vote2:
    st.success("Thank you for voting for Adrak Chai! Your vote has been counted. ☕")

st.markdown("<style>.stApp{background-color:#D2B48C;}</style>", unsafe_allow_html=True)

name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Select your favorite tea", ["Masala Chai", "Adrak Chai"])

if name:
    st.write(f"Hello, {name}! Your favorite tea is {tea}. Thank you for sharing your preference! ☕")
else:
    st.write("Hello! Please enter your name in the sidebar and select your favorite tea. ☕")

with st.expander("Show Chai Making Instructions"):
    st.write("1. Boil water and add tea leaves.")
    st.write("2. Add milk and sugar to taste.")
    st.write("3. Let it simmer for a few minutes.")
    st.write("4. Strain the tea into cups and serve hot. Enjoy your delicious Chai! ☕")