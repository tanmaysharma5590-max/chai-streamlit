import streamlit as st
st.title("Chai maker App")
if st.button("Make Chai"):
    st.success("Your Chai is ready! Enjoy! ☕") 
add_masala = st.checkbox("Add Masala")
if add_masala:
    st.write("Masala added to your Chai! Enjoy the rich flavor! 🌿")
tea_type = st.radio("Select Tea Type", ["Black Tea", "Green Tea", "Milk Tea"])
st.write(f"You selected: {tea_type}. Your Chai will be made with {tea_type.lower()}!")
flavor = st.selectbox("Select Flavor", ["Cardamom", "Ginger", "Saffron", "Rose","adrak","Kesar","Gulab","Tulsi"])
st.write(f"You selected: {flavor}. Your Chai will have a delightful {flavor.lower()} flavor!")
suger=st.slider("Select Sugar Level(spoons)", 0, 5, 2)
st.write(f"You selected: {suger} spoons of sugar.")
