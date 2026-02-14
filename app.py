import streamlit as st
import google.generativeai as genai

# -------------------------------
# 🔐 Add Your Gemini API Key Here
# -------------------------------
genai.configure(api_key="AIzaSyADk25-xXGgRgCYpwAFKZuVt8RkPS17Xbc")


# Load Gemini Model
model = genai.GenerativeModel("gemini-pro")


# -------------------------------
# 🌟 Streamlit UI
# -------------------------------

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄")

st.title("📄 AI Resume Analyzer")
st.write("Paste your resume below and get AI-powered feedback instantly!")

# Resume Input
resume_text = st.text_area("📌 Paste your Resume Here:", height=300)

# Analyze Button
if st.button("🚀 Analyze Resume"):

    if resume_text.strip() == "":
        st.warning("⚠ Please paste your resume first.")
    
    else:
        with st.spinner("Analyzing your resume..."):

            prompt = f"""
            You are a professional HR recruiter.

            Analyze the following resume and provide:

            1. Missing skills
            2. Strengths
            3. Areas of improvement
            4. Overall score out of 10
            5. Final recommendation

            Resume:
            {resume_text}
            """

            response = model.generate_content(prompt)

            st.success("✅ Analysis Complete!")
            st.write(response.text)

