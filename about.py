import streamlit as st
def app():

    # CSS styling
    st.markdown("""
    <style>
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }
    .member {
        display: flex;
        align-items: center;
        margin: 20px 0;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 10px;
    }
    .member img {
        max-width: 150px;
        border-radius: 50%;
        margin-right: 20px;
    }
    .member div {
        text-align: left;
    }
    .member h3 {
        margin: 10px 0 5px 0;
    }
    .member p {
        margin: 5px 0;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title of the webpage
    st.title("About Us")

    # Project Description
    st.write("""
    Welcome to the website for our BCA final semester MPR project, PlantCare. Our project focuses on identifying and classifying plant diseases using machine learning techniques. We aim to help farmers and gardeners quickly diagnose issues and take necessary actions to ensure healthy plant growth.
    """)

    # Team Members Section
    st.write("## Meet the Team")

    # Member A
    st.markdown("""
    <div class="member">
        <img src="https://rohan-healthup-q5gjw.ondigitalocean.app/static/images/nishant.png" alt="Nishant Singh">
        <div>
            <h3>Nishant Singh</h3>
            <p><strong>Role:</strong> Machine Learning Model Developer</p>
            <p>Nishant Singh was responsible for developing the machine learning model that powers the PlantCare application. This involved data collection, preprocessing, model selection, training, and evaluation to ensure accurate and reliable disease classification.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Member B
    st.markdown("""
    <div class="member">
        <img src="https://rohan-healthup-q5gjw.ondigitalocean.app/static/images/rohan.png" alt="Rohan Banduni">
        <div>
            <h3>Rohan Banduni</h3>
            <p><strong>Role:</strong> Website Developer</p>
            <p>Rohan Banduni designed and developed the PlantCare website. This includes creating a user-friendly interface, integrating the machine learning model into the website, and ensuring that users can easily navigate and use the application.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Member C
    st.markdown("""
    <div class="member">
        <img src="https://rohan-healthup-q5gjw.ondigitalocean.app/static/images/sumit.png" alt="Sumit Yadav">
        <div>
            <h3>Sumit Yadav</h3>
            <p><strong>Role:</strong> Documentation Specialist</p>
            <p>Sumit Yadav worked on the documentation of the PlantCare project. This includes writing detailed reports, user manuals, and technical documentation to ensure that every aspect of the project is well-documented and easily understood by users and future developers.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Member D
    st.markdown("""
    <div class="member">
        <img src="https://rohan-healthup-q5gjw.ondigitalocean.app/static/images/mam.png" alt="Dr. Tarunim Sharma">
        <div>
            <h3>Dr. Tarunim Sharma</h3>
            <p><strong>Role:</strong> Project Guide</p>
            <p>Dr. Tarunim Sharma was the guide for our project. They provided valuable insights, guidance, and support throughout the development of PlantCare. Their expertise and feedback were crucial in shaping the direction and success of our project.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Footer
    st.write("""
    ## Acknowledgements
    We would like to express our heartfelt gratitude to our guide, Member D, for their constant support and guidance. Special thanks to our institution for providing us with the resources and opportunities to work on this project. Lastly, we thank all the members of our team for their dedication and hard work in making PlantCare a reality.
    """)

# Run the app
if __name__ == "__main__":
    app()
