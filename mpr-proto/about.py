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
    h1, h2, h3 {
        text-align: center;
        color: #011f4b; /* Heading color */
    }
    .about-us {
        text-align: center;
        margin: 20px auto;
        padding: 20px;
        border: 2px solid #2E86C1; /* Adding a border */
        border-radius: 10px; /* Rounded corners */
        background-color: #f9f9f9; /* Light background */
        max-width: 800px;
    }
    .member {
        display: flex;
        align-items: center;
        margin: 20px 0;
        padding: 10px;
        border: 2px solid #2E86C1;
        border-radius: 10px;
        background-color: #f9f9f9; /* Light background for member sections */
    }
    .member img {
        max-width: 150px;
        border-radius: 50%;
        margin-right: 20px;
        border: 2px solid #2E86C1; /* Border around images */
    }
    .member div {
        text-align: left;
    }
    .member h3 {
        margin: 10px 0 5px 0;
        color: #011f4b; /* Member name color */
    }
    .member p {
        margin: 5px 0;
        color: #333; /* Text color */
    }
    .acknowledgements {
        margin-top: 30px;
        padding: 20px;
        border: 2px solid #2E86C1;
        border-radius: 10px;
        background-color: #e8f4f8; /* Light blue background for acknowledgements */
        color: #333; /* Text color */
    }
    </style>
    """, unsafe_allow_html=True)

    # Title of the webpage
    st.title("About Us")

    # Project Description
    st.markdown("""
    <div class="about-us">
        <p>Welcome to the website for our BCA final semester MPR project, PlantCare. Our project focuses on identifying and classifying plant diseases using machine learning techniques. We aim to help farmers and gardeners quickly diagnose issues and take necessary actions to ensure healthy plant growth.</p>
    </div>
    """, unsafe_allow_html=True)

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
    st.markdown("""
    <div class="acknowledgements">
        <h2>Acknowledgements</h2>
        <p>We would like to express our heartfelt gratitude to our guide, Dr. Tarunim Sharma, for their constant support and guidance. Special thanks to our institution for providing us with the resources and opportunities to work on this project. Lastly, we thank all the members of our team for their dedication and hard work in making PlantCare a reality.</p>
    </div>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    app()
