import streamlit as st
st.header("Working with file",anchor=False)
st.divider()
images=st.file_uploader("Upload your images here",type=['jpg','jpeg','png'],accept_multiple_files=True)

if images:
    col=st.columns(len(images))
    
    for i,img in enumerate(images):
        with col[i]:
            st.image(img)