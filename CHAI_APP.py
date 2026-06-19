import streamlit as st
st.markdown("<h1 style='color: #8B4513; font-family: Arial, sans-serif;'>Welcome to Tanmay's Chai App! ☕</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #A0522D; font-family: Arial, sans-serif;'>Discover the art of making the perfect cup of Chai and share your preferences with us!</p>", unsafe_allow_html=True)
col1,col2=st.columns(2)
with col1:
    st.header("Masala Chai")
    st.image(r"C:\Users\ACER\Downloads\ChatGPT Image Jun 20, 2026, 12_55_06 AM.png")
    vote1=st.button("Vote for Masala Chai")
with col2:
    st.header("Adrak chai")
    st.image(r"C:\Users\ACER\Downloads\ChatGPT Image Jun 20, 2026, 12_53_05 AM.png")
    vote2=st.button("Vote for Adrak chai")
if vote1:
    st.success("Thank you for voting for Masala Chai! Your vote has been counted. ☕")
elif vote2:
    st.success("Thank you for voting for Adrak Chai! Your vote has been counted. ☕")

st.markdown("<style>.stApp{background-color:#D2B48C;}</style>", unsafe_allow_html=True)

name=st.sidebar.text_input("Enter your name")
tea=st.sidebar.selectbox("Select your favorite tea", ["Masala Chai", "Adrak Chai"])
st.write(f"Hello, {name}! Your favorite tea is {tea}. Thank you for sharing your preference! ☕")

with st.expander("Show Chai Making Instructions"):
    st.write("1. Boil water and add tea leaves.")
    st.write("2. Add milk and sugar to taste.")
    st.write("3. Let it simmer for a few minutes.")
    st.write("4. Strain the tea into cups and serve hot. Enjoy your delicious Chai! ☕")