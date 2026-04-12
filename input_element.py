import streamlit as st

st.title("Input Element Learining",anchor=False)
st.divider()
name=st.text_input("Please Enter your name:",placeholder="Write your name")
age=st.number_input("Enter your age:",placeholder="Write your age")
password=st.text_input("Enter your password: ",type="password",placeholder="Type your password")

is_clicked=st.button("Submit",type="primary")

if is_clicked:
    st.write(f"Your name is {name}, age: {age}")