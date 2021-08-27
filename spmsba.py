import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#streamlit page configuration
st.set_page_config( layout="wide",page_title=None,page_icon=None)

#Streamlit Sidebar
image = Image.open('logo2.png')
st.sidebar.image(image)
txt = '<p style="font-family:georgia;text-align: center;color:black;font-weight: bold; font-size: 23px;">OSB Graduate Program</p>'
st.sidebar.markdown(txt, unsafe_allow_html=True)
st.sidebar.write("#")
st.sidebar.write("#")
txt = '<p style="font-family:georgia;text-align: center;color:black;font-weight: bold; font-size: 25px;">Students Profile Application</p>'
st.sidebar.markdown(txt, unsafe_allow_html=True)
st.sidebar.write("#")
st.sidebar.write("#")
st.sidebar.write("#")
txt = '<p style="font-family:georgia;text-align: center;color:black; font-weight: bold;font-size: 20px;">Capstone Application prepared By Dalal El Khatib</p>'
st.sidebar.markdown(txt, unsafe_allow_html=True)
st.sidebar.write("#")
txt = '<p style="font-family:georgia;text-align: center;color:black; font-size: 15px;">Graduate Assistant at OSB Graduate Office</p>'
st.sidebar.markdown(txt, unsafe_allow_html=True)
txt = '<p style="font-family:georgia;text-align: center;color:black; font-size: 15px;">For further details contact : dme43@mail.aub.edu</p>'
st.sidebar.markdown(txt, unsafe_allow_html=True)
st.sidebar.write("#")
st.sidebar.write("#")
st.sidebar.write("#")
txt = '<p style="font-family:georgia;text-align: left;color:black;font-weight: bold; font-size: 20px;">Dashboard Password</p>'
st.sidebar.markdown(txt, unsafe_allow_html=True)
password=st.sidebar.text_input("",value="", type="password")

def main():
    st.markdown("<h1 style='text-align: center;font-family:georgia;font-weight: bold;font-size: 40px; color:black;'>Student Profile Application</h1>", unsafe_allow_html=True)
    st.write("#")
    st.markdown("<h1 style='text-align: Left;font-family:georgia;font-size: 30px; color:black;'>General Overview of The Application</h1>", unsafe_allow_html=True)
    my_expander = st.beta_expander("GET TO KNOW MORE ABOUT THE APPLICATION", expanded=False)
    with my_expander:
        st.write("OSB Graduate office operates in a very dynamic environments that are constantly changing, whether that means records of new open application, accepted or enrolled. This flux of data produces serious operational challenges that must always be closely monitored. The goal is therefor to create a tool that is automatically updated with the most recent relevant and immediate information of enrolled Students.")
        st.write("The aim of this streamlit application is utlizing existing and fresh data of enrolled students to create an automated tool that reports students information to concerned professors to be able to explores their students’ background,learning engagement and their dispositions to the learning process ")
        pic1 = Image.open('pic1.png')
        st.image(pic1)


    st.write("#")
    st.markdown("<h1 style='text-align: Left;font-family:georgia;font-size: 30px; color:black;'>MSBA Student Profile</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: Left;font-family:georgia; font-size: 25px;color:black;'>1️⃣ Upload Students CSV file Received from Graduate Office 👇 </h1>", unsafe_allow_html=True)

    @st.cache(allow_output_mutation=True)
    def load_data(file):
        df = pd.read_csv(file, encoding='utf-8')
        return df

    uploaded_file = st.file_uploader("", type="csv", key='file_uploader')

    if uploaded_file is not None:
        df = load_data(uploaded_file)
        st.markdown("<h1 style='text-align: Left;font-family:georgia;font-size: 25px;color:black;'>2️⃣ Select Student name 👇 </h1>", unsafe_allow_html=True)
        student = df['StudentName'].drop_duplicates()
        student_choice = st.selectbox('', student)
        name=df['StudentName'].loc[df['StudentName'] == student_choice].to_list()
        name1=name[0]
        LinkedIn = df["LinkedInUrl"].loc[df["StudentName"] == student_choice].tolist()
        LinkedIn1=LinkedIn[0]
        Bio = df["Biography"].loc[df["StudentName"] == student_choice].tolist()
        Bio1=Bio[0]




        figure1,text1 = st.beta_columns(2)
        with figure1:
            #from PIL import Image
            product_img = df['Photo'].loc[df['StudentName'] == student_choice].tolist()
            st.image(product_img, width = 350)

        with text1:
            txt = '<p style="font-family:georgia;text-align: Left;color:black;font-weight: bold; font-size: 25px;"> Name</p>'
            st.markdown(txt, unsafe_allow_html=True)
            st.markdown(name1)
            txt = '<p style="font-family:georgia;text-align: Left;color:black;font-weight: bold; font-size: 25px;"> LinkedIn Account Link</p>'
            st.markdown(txt, unsafe_allow_html=True)
            st.markdown(LinkedIn1)
            txt = '<p style="font-family:georgia;text-align: Left;color:black;font-weight: bold; font-size: 25px;"> Bio</p>'
            st.markdown(txt, unsafe_allow_html=True)
            st.markdown(Bio1)



if password=='aubosb':
    main()
#elif password !='aubosb':
        #st.error("Authentication failed. Please verify your password and try again. ")
        #txt = '<p style="font-family:georgia;text-align: left;color:black; font-weight: bold;font-size: 10px;">Authentication failed. Please verify your password and try again.</p>'
        #st.sidebar.markdown(txt, unsafe_allow_html=True)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
