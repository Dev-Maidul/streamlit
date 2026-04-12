import streamlit as st

st.title("Input Element Learining",anchor=False)
st.divider()
name=st.text_input("Please Enter your name:",placeholder="Write your name")
age=st.number_input("Enter your age:",placeholder="Write your age",value=None)
password=st.text_input("Enter your password: ",type="password",placeholder="Type your password")

options=st.selectbox("What is your procession ?",("Student","Business man","Others"),index=None,accept_new_options=True)

is_clicked=st.button("Submit",type="primary")

if is_clicked:
    st.write(f"Your name is {name}, age: {age} and you are a {options}")