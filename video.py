import streamlit as st
st.header("Working with Video file",anchor=False)
st.divider()

videos=st.file_uploader("Upload your videos here",type=['mp4','mkv'])

if videos:
    st.success("Video uploaded successfully")
    st.video(videos)
    
else :
    st.error("No video provided")