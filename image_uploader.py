import streamlit as st
st.header("Upload your Images below",anchor=False)
st.divider()

images=st.file_uploader("Upload your image here",type=['jpg','png','jpeg'],accept_multiple_files=True)

if(images):
    col=st.columns(len(images))
    
    for i,img in enumerate(images):
        with col[i]:
            st.image(img)
