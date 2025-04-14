from PIL import Image
import streamlit as st
from moondream_lib import MoondreamHelper

# Some initial page configuration for style

st.set_page_config(
    page_title="Moondream Dashboard",
    page_icon="🌕"
)

@st.cache_resource
def get_moondream():
    return MoondreamHelper(api_key=st.secrets["moondream_api_key"])

moondream = get_moondream()

def upload_image():
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"], key=page)
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="This is the image you uploaded", use_column_width=True)
        return image
    return None

# Sidebar nav
st.sidebar.title("🌕 Moondream Vision API")
page = st.sidebar.radio("Select the page you want to visit", ["Describe Image", "Caption Image"])

if page == "Describe Image":
    st.title("🖼️ Describe Image")
    st.write("Upload an image to get an automatic description of it")
    image = upload_image()
    if image:
        detail = st.radio("Select the description detail", ["Short", "Normal", "Long"], horizontal=True).lower()
        if st.button("Generate description"):
            with st.spinner("Analyzing image..."):
                description = moondream.describe(image, detail)
                st.success("Description generated!")
                st.write(description)        

elif page == "Caption Image":
    st.title("Ask questions")
    st.write("Query the image as you like")
    image = upload_image()
    if image:
        question = st.text_input("Ask something about the image", placeholder="How many objects are on the image")

        if question and st.button("Get answer"):
            with st.spinner("Thinking..."):
                answer = moondream.query(image, question)
                st.success("Answer generated!")
                st.write(answer)

