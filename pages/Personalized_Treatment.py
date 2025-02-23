import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load API Key from .env file
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Streamlit App Config
st.set_page_config(page_title="Personalized Treatment Plan", page_icon="medilab-square.png", layout="wide")

# Sidebar Contact
st.sidebar.subheader("📞 **Contact Us**")
st.sidebar.markdown(
    """
    <p style="font-size:16px; margin-bottom:4px;">
        📧 <a href="mailto:medilab@mgmail.com" style="text-decoration:none; color:black;">medilab@mgmail.com</a>
    </p>
    <p style="font-size:16px; margin-bottom:4px;">
        🌐 <a href="https://www.medilab.com" target="_blank" style="text-decoration:none; color:black;">www.medilab.com</a>
    </p>
    <p style="font-size:16px;">
        📍 Location: New Delhi
    </p>
    """,
    unsafe_allow_html=True
)

# Hero Section
img_path = "medilab-rectangle.png"
if os.path.exists(img_path):
    st.image(img_path, width=150)
else:
    st.warning("⚠️ Image not found. Please check the file path.")

st.markdown(
    """
    <h1 style='text-align: center; color: #333;'>🩺 Personalized Treatment Plan Generator</h1>
    <p style='text-align: center; font-size: 18px;'>Fill out the details below to get a tailored treatment plan based on your health data.</p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# User Inputs
st.header("👤 Basic Information")
name = st.text_input("Full Name")
age = st.number_input("Age", min_value=0, max_value=120, step=1)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
height = st.number_input("Height (cm)", min_value=50, max_value=250, step=1)
weight = st.number_input("Weight (kg)", min_value=10, max_value=300, step=1)
bmi = round(weight / ((height / 100) ** 2), 2) if height > 0 else "N/A"
st.write(f"Calculated BMI: **{bmi}**")

st.header("🏥 Medical History")
pre_existing_conditions = st.text_area("List any pre-existing conditions (e.g., Diabetes, Hypertension)")
current_symptoms = st.text_area("Describe your current symptoms")

st.header("💊 Current Medications & Lifestyle")
medications = st.text_area("List any ongoing medications (Name, Dosage, Frequency)")
smoking = st.radio("Do you smoke?", ["Yes", "No"])
alcohol = st.radio("Do you consume alcohol?", ["Yes", "No"])
sleep_hours = st.slider("Average sleep per night (hours)", 0, 12, 7)
stress_level = st.slider("Stress Level (1 - Low, 10 - High)", 1, 10, 5)

st.header("📑 Medical Test Reports (Optional)")
report = st.file_uploader(label="Upload your Medical Report (if any)")

st.header("⚕️ Treatment Preferences")
treatment_type = st.selectbox("Preferred treatment type", ["Allopathic", "Ayurvedic", "Homeopathic", "No preference"])
budget = st.number_input("Budget for treatment (INR/USD)", min_value=0, step=100)

# Load Sample Report Data
sample_report_path = "sample_report.txt"
sample_data = "No sample report found."  # Default message if file is missing

if os.path.exists(sample_report_path):
    with open(sample_report_path, "r", encoding="utf-8") as file:
        sample_data = file.read()

# Submit Button
if st.button("Generate Treatment Plan"):
    llm = ChatGroq(api_key=groq_api_key)
    st.success(f"Thank you, {name}! Your personalized treatment plan is being generated...")

    # Generate AI-based Treatment Plan
    prompt = f"""
    User Name: {name}
    Age of the User: {age}
    Gender: {gender}
    BMI of {name}: {bmi}
    List of any pre-existing conditions: {pre_existing_conditions}
    Current symptoms of the user: {current_symptoms}
    Does the user smoke: {smoking}
    Does the user consume alcohol: {alcohol} 
    Sleep hours of the user: {sleep_hours}
    Stress Level of the user on a scale of 1-10: {stress_level}
    Preferred Treatment type of the user: {treatment_type}
    Budget of the user: {budget}

    Based on the input provided by the user, you have to create a personalized, descriptive and accurate medical report for the user.

    <sample>

    {sample_data}

    </sample>
    """
    report = llm.invoke(prompt)
    st.write(report.content)

    st.warning("⚠️ This is an AI-generated suggestion. Please consult a doctor before making any medical decisions.")

# Footer - Copyright Section
st.markdown("---")
st.markdown(
    """
    <p style="text-align: center; font-size: 14px; color: gray;">
        &copy; 2025 MediLab Healthcare. All rights reserved.
    </p>
    """,
    unsafe_allow_html=True
)
