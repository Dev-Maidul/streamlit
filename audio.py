import streamlit as st
st.header("Upload you audio file below",anchor=False)
st.divider()

audios=st.file_uploader("Upload your Audio here",type=['mp3'])

if audios:
    st.audio(audios,loop=True)