import streamlit as st
from moondream_lib import MoondreamHelper

# Some initial page configuration for style

st.set_page_config(
    page_title="Moondream Dashboard",
    page_icon="🌕"
)

st.title("Hello this is a title")

@st.cache_resource
def get_moondream():
    return MoondreamHelper(api_key="")

moondream = get_moondream()

# Sidebar nav
st.sidebar.title("🌕 Moondream Vision API")
page = st.sidebar.radio("Select the page you want to visit", ["Describe Image", "Caption Image"])

if page == "Describe Image":
    st.title("🖼️ Describe Image")
    st.write("Upload an image to get an automatic description of it")
