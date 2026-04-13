import streamlit as st

import streamlit as st

st.title(":smirk_cat: Creating calculator App",anchor=False)
st.divider()

number1 = st.number_input("Enter first number", key="num1",value=None,placeholder="Enter first Number",step=1)
number2 = st.number_input("Enter second number", key="num2",value=None,placeholder="Enter Second Number",step=1)

options=st.selectbox("Select your calculation types: ",["Addition","Substraction","Multiplication","Division"])
isCalculate=st.button("Calculate",type="primary")
if isCalculate:
    if number1 is None:
        st.error("⚠️ Please enter first number")
    if number2 is None:
        st.error("You did not provide 2nd Number")
    if len(options)==0:
        st.error("Select calculation method")
    if(options=="Addition"):
        ans=number1+number2
        st.write(f"Your answer={number1}+{number2}={ans}")
    if options=="Substraction":
        ans=number1-number2
        st.write(f"Your answer= {number1}-{number2}={ans}")
    if options=="Multiplication":
        ans=number1*number2
        st.write(f"Your answer= {number1}*{number2}={ans}")
    else:
        ans=number1/number2
        st.write(f"Your answer= {number1}/{number2}={ans}")
    
