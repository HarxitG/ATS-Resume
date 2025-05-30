from dotenv import load_dotenv
load_dotenv()

import base64
import streamlit as st
import os
import io
from PIL import Image
import pdf2image
import google.generativeai as genai 

# Configure Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt, pdf_content, job_description):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_prompt, pdf_content[0], job_description])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert PDF to images (1st page only)
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        # Prepare the PDF part for Gemini
        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")


# --- Streamlit UI ---
st.set_page_config(page_title="ATS Resume Expert")
st.title("ATS Resume Evaluation Tool")

job_description = st.text_area("Job Description:", key="job_desc")
uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

submit1 = st.button("Tell Me About the Resume")
submit3 = st.button("Percentage Match")

# Define prompts
input_prompt1 = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description.
Please share your professional evaluation on whether the candidate's profile aligns with the role.
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality.
Your task is to evaluate the resume against the provided job description.
Give me the percentage of match, then list missing keywords, and finally share overall thoughts.
"""

# Handle Submit 1
if submit1:
    if uploaded_file and job_description:
        with st.spinner("Analyzing resume..."):
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_prompt1, pdf_content, job_description)
        st.subheader("Evaluation Result")
        st.write(response)
    else:
        st.error("Please upload your resume and provide a job description.")

# Handle Submit 3
if submit3:
    if uploaded_file and job_description:
        with st.spinner("Calculating match percentage..."):
            pdf_content = input_pdf_setup(uploaded_file)
            response = get_gemini_response(input_prompt3, pdf_content, job_description)
        st.subheader("Match Result")
        st.write(response)
    else:
        st.error("Please upload your resume and provide a job description.")
               


