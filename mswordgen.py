import streamlit as st

st.set_page_config(
    page_title="Microsoft Word Generator",
    page_icon="📝",
    layout="wide",
)

st.title("Microsoft Word Generator")

st.markdown(
    """
    Generate Microsoft Word document (.docx) files, by selecting a series of images
    that will be inserted into the document.
    """
)

uploaded_files = st.file_uploader("Choose images file", accept_multiple_files=True)
if uploaded_files is not None:
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)
