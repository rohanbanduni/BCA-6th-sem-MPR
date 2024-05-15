import streamlit as st
import os
def app():
    working_dir = os.path.dirname(os.path.abspath(__file__))

    st.subheader('PlantCare - Plant disease classification.')
    st.write('This project has been developed for our BCA 6th semester MPR (Major Project Report). In this project, we are focusing on plant disease classification for more accurate identification and classification of diseases affecting plants. Our aim is to develop a model that can efficiently classify different plant diseases by there leaf images. This project utilizes python, tensorflow and streamlit for implementation. Through this project, we aim to contribute to the field of agriculture by providing a tool that can assist farmers in early detection and management of plant diseases. Our Plant Disease Classifier is a cutting-edge tool designed to assist farmers, agronomists, and gardeners in identifying and managing plant diseases efficiently. By harnessing the power of machine learning, our classifier can accurately recognize various diseases that affect crops and plants, enabling timely intervention and effective disease management strategies.')
    st.write("---")
    st.subheader("##")

    st.image(f"{working_dir}/assets/aboutproject.png")
    st.subheader("##")
    st.write("---")

    st.subheader('How it works')
    st.subheader("##")

    st.write('Using machine learning algorithms, our classifier analyzes images of plant leaves to identify symptoms associated with different plant diseases. Users simply upload a clear photo of the affected plant, and our classifier quickly provides a diagnosis.')
    st.subheader("##")


    st.image(f"{working_dir}/assets/howitworks.png")
    st.subheader("##")

    st.write("---")

    st.subheader('Techstack of the project')
    st.subheader("##")
    st.image(f"{working_dir}/assets/tools.png")
