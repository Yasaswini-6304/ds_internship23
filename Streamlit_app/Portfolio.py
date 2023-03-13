import streamlit as st
import numpy as np
from PIL import Image, ImageDraw
from pathlib import Path

PROJECTS = {
    "🏆 Youtube Video-To-Mp3 Bot (Telegram Bot)": "https://github.com/Yasaswini-6304/Youtube-Video-to-Mp3-Bot"}


st.header(":red[Portfolio] 👏")
st.write("")

col1, col2 = st.columns([10, 7])
with col1:
    st.header("Yasaswini")
    st.caption("UI/UX || Data Science")
with col2:
    st.write(
        "I am Yasaswini Kukunoori Currently Doing My Bachelor's Degree in Vishnu Institute of Technology in the Stream of Artificial Intelligence and Data science . I am Passionate about Web Technologies and I am currently Learning UI/UX and I am Very Much Interested in Machine Learning and Cyber security. Have Good knowledge of Web Technologies -Html , css , Javascript ,Programming Languages - Python , Java. Currently Working on some minor machine learning projects . I am Eager to Learn more and more new technologies in coming days.."
    )


st.subheader("Skills :")
st.write(
    """
  'Programming': ['Python','Java'], \n
  'Data Visualization' : ['Seaborn', 'Matplotlib'], \n
  'Python Library' :  ['numpy', 'pandas'],\n
  'Databases': SQL \n
  'UX Design': Figma \n
    """
)
st.subheader("   }")
st.subheader("Work Experience : ")
st.write("---")
st.write("Oasis Web Development Intern")
st.write(
    """
- ► Worked On Multiple Websites and Created Responsive Web Designs
- ► Got Internship Certificate
"""

)

st.write("\n")
st.subheader("Projects :")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
st.write("\n")
