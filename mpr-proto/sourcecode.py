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
    .content {
        display: flex; /* Use flexbox */
        flex-direction: row; /* Arrange content horizontally */
        align-items: center; /* Center align items vertically */
        justify-content: flex-start; /* Align items to the start (left) */
        text-align: left; /* Align text to the left */
        margin: 20px auto; /* Adjusting margin */
        padding: 30px; /* Adjusting padding */
        max-width: 1000px; /* Increase overall width */
        border: 2px solid #2E86C1;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .content h2 {
        margin-top: 0; /* Remove top margin for h2 */
        font-size: 36px;
        color: #011f4b;
        font-weight: bold;        
    }
    .content p {
        margin-top: 15px; /* Adjusting margin */
        font-size: 18px;
    }
    .content img {
        margin-left: 20px; /* Adjusting margin */
        max-width: 200px; /* Limiting image width */
        height: auto; /* Maintain aspect ratio */
    }
    .github-link {
        margin-top: 20px; /* Adjusting margin */
        margin-left: 0; /* Resetting left margin */
        font-size: 18px;
    }
    .github-link a {
        display: inline-block; /* Ensure link behaves as block element */
        margin-top: 10px; /* Adjusting top margin */
        text-decoration: none;
        color: white;
        background-color: #2E86C1;
        padding: 10px 20px;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Page Content
    st.markdown("""
    <div class="content">
        <div>
            <h2>Source Code</h2>
            <p>You can find the complete source code for the PlantCare project on our GitHub repository. The repository includes all the code, data, and resources needed to understand and replicate our work.</p>
            <div class="github-link">
                <a href="https://github.com/rohanbanduni/BCA-6th-sem-MPR" target="_blank">Visit our GitHub Repository</a>
            </div>
        </div>
        <div>
            <img src="https://images.pexels.com/photos/102061/pexels-photo-102061.jpeg?auto=compress&cs=tinysrgb&w=600" alt="code image" />
        </div>
    </div>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    app()
