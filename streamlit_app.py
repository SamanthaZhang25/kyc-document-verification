import streamlit as st
import os
from PIL import Image
import easyocr
# from src.ocr.document_processor import DocumentProcessor # Commenting out to prevent potential import errors

st.set_page_config(layout="wide")

st.title("KYC Document Verification Interface")

# Initialize OCR reader
@st.cache_resource
def load_ocr():
    return easyocr.Reader(['en'])

reader = load_ocr()

st.header("Upload Document for Verification")
uploaded_file = st.file_uploader("Choose a document image (JPG, PNG, JPEG)", type=['jpg', 'png', 'jpeg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Document', use_column_width=True)
    
    if st.button('Extract and Verify Text'):
        with st.spinner('Processing...'):
            temp_file_path = 'temp_image.jpg'
            with open(temp_file_path, 'wb') as f:
                f.write(uploaded_file.getvalue())
            
            try:
                result = reader.readtext(temp_file_path)
                extracted_text = ' \n'.join([detection[1] for detection in result])
                
                st.subheader('Extracted Text:')
                st.text_area("OCR Output", extracted_text, height=250)
                
                st.subheader('LLM Validation (Placeholder)')
                st.info('This is a placeholder. In a full implementation, the extracted text would be sent to an LLM for validation.')

                st.subheader('Fraud Detection (Placeholder)')
                st.success('Image forensics check passed (placeholder).')

            except Exception as e:
                st.error(f"An error occurred: {e}")

            finally:
                if os.path.exists(temp_file_path):
                    os.remove(temp_file_path)

else:
    st.info("Please upload an image file to begin.")

st.sidebar.header('How to Use')
st.sidebar.markdown("""1. Upload a document image.\n2. Click 'Extract and Verify Text'.\n3. Review the results.""")
st.sidebar.header('About')
st.sidebar.info("This is a demo for the KYC Document Verification project.")
st.sidebar.warning("Note: Full LLM integration requires an API key.")
