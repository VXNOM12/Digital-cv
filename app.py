from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "main.css"
resume_file = current_dir  / "Harsh KatalkarCV.pdf"
profile_pic = current_dir  / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Harsh Katalkar"
PAGE_ICON = ":wave:"
NAME = "Harsh Katalkar"
DESCRIPTION = """
Mastering Data Science and AI | Proficient in SQL, Python, Power BI, HTML, CSS and Data Analytics.
"""
EMAIL = "harshkatlkar67@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/harshkatalkar",
    "GitHub": "https://github.com/VXNOM12",
}
PROJECTS = {
    "🏆 StrokePredict ": "https://github.com/VXNOM12/StrokePredict/tree/main",
    "🏆 chatbot": "https://github.com/VXNOM12/chatbot",
    "🏆 COVID-19_Global_Tracker_and_Analysis": "https://github.com/VXNOM12/COVID-19_Global_Tracker_and_Analysis",
    "🏆 Sentiment-Analysis": "https://github.com/VXNOM12/Sentiment-Analysis",

}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 1 Years experience extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Power BI
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Seaborn), SQL.
- 📊 Data Visulization: PowerBi, Plotly, Matplotlib.
- 📚 Modeling: Logistic regression, linear regression.
- 🗄️ Databases: MongoDB, MySQL
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
