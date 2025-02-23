import streamlit as st  

# Page Configuration  
st.set_page_config(
    page_title="mediLAB - AI Health Assistant", 
    page_icon="medilab-square.png", 
    layout="wide"
)

# Sidebar Navigation  
st.sidebar.subheader("🔹 **Navigation**")  
st.sidebar.page_link("pages/Cheap_meds.py", label="💊 Cheap Medicines")  
st.sidebar.page_link("pages/Personalized_treatment.py", label="🩺 Personalized Treatment")  
st.sidebar.page_link("pages/Chatbot.py", label="🦠 Assess Your Symptoms")  

st.sidebar.markdown("---")  

# Sidebar Contact (Clickable but No Underline or Blue Color)  
st.sidebar.subheader("📞 **Contact Us**")  
st.sidebar.markdown(
    """
    <p style="font-size:16px; margin-bottom:4px;">
        📧 <a href="mailto:medilab@gmail.com" style="text-decoration:none; color:black;">medilab@gmail.com</a>
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

st.sidebar.markdown("---") 

# Sidebar Copyright Section
st.sidebar.markdown(
    """
    <p style="text-align: center; font-size: 12px; color: gray;">
        &copy; 2025 MediLab Healthcare. All rights reserved.
    </p>
    """,
    unsafe_allow_html=True
)

# Hero Section  
col1, col2 = st.columns([1, 2])  
with col1:  
    st.image("medilab-rectangle.png", width=250)  
with col2:  
    st.markdown(
        """
        # **Welcome to mediLAB**   
        ### Your AI-powered **Health Companion**  
        Get smarter healthcare insights with AI-driven recommendations for affordable medicines, 
        personalized treatment plans, and symptom assessments.  
        **Healthcare, simplified.**  
        """
    )  
    st.markdown("---")  

# Main Section  
st.header("🩺 **Our Healthcare Services**")  
st.write("Explore AI-powered healthcare solutions tailored for you.")  

col1, col2, col3 = st.columns(3)  

with col1:  
    st.page_link("pages/Cheap_meds.py", label="💊 Find Cheap Medicine Alternatives")  
    st.success("Compare and find cost-effective medicine alternatives from trusted providers.")  

with col2:  
    st.page_link("pages/Personalized_treatment.py", label="🩺 Get a Personalized Treatment Plan")  
    st.success("AI-powered suggestions tailored to your health needs based on symptoms and history.")  

with col3:  
    st.page_link("pages/Chatbot.py", label="🦠 Assess Your Symptoms")  
    st.success("Analyze symptoms and get guidance on potential conditions and next steps.")  

st.markdown("---")  

# How It Works Section  
st.header("⚙️ **How mediLAB Works**")  
st.write("Our AI-driven health assistant follows a simple three-step process to provide personalized recommendations.")  

col1, col2, col3 = st.columns(3)  

with col1:  
    st.markdown("### 1️⃣ **Input Your Symptoms**")  
    st.write("Describe your symptoms, medical history, or health concerns.")  

with col2:  
    st.markdown("### 2️⃣ **AI-Powered Analysis**")  
    st.write("Our smart AI model evaluates your input and compares it with vast medical databases.")  

with col3:  
    st.markdown("### 3️⃣ **Get Recommendations**")  
    st.write("Receive affordable medicine suggestions, treatment plans, or next-step guidance.")  

st.markdown("---")  

# Disclaimer  
st.warning("⚠️ This app provides AI-generated recommendations. Always consult a doctor before making medical decisions.")  

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

