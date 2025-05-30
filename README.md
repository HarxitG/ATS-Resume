# ATS Resume App

A resume analysis tool built with Streamlit and powered by the Google Gemini API. This app compares your resume with a job description and provides an ATS-style evaluation, including match percentage and suggestions for improvement.

---

## Features

- Upload a resume in PDF format
- Paste a job description
- Get AI-generated feedback on strengths, weaknesses, and match percentage
- ATS-style evaluation using Gemini

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ats-resume-app.git
cd ats-resume-app
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

## Environment Setup

```bash
GOOGLE_API_KEY=your_google_api_key_here
```

## Running the App

```bash
streamlit run app.py
```

## Requirements

Python 3.8+

Poppler (required by pdf2image)

Windows: Poppler for Windows

Add the /bin folder from the Poppler zip to your system PATH

## Technologies Used

Python

Streamlit

Google Gemini API (gemini-1.5-flash)

pdf2image

Pillow (PIL)


