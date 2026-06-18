import streamlit as st

st.title("Hello Chai App")
st.subheader("This is a simple Chai app built with Streamlit.")
st.text("Welcome to your first interactive Chai app.")
st.write("Choose your favorite variety of Chai:")
chai=st.selectbox("Select Chai", ["Masala Chai", "Ginger Chai", "Cardamom Chai", "Tulsi Chai"])
st.write(f"You selected: {chai}")
st.write("Enjoy your cup of Chai! ☕")