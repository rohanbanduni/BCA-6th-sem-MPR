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
        text-align: center;
        margin: 0 auto;
        max-width: 800px;
    }
    .content h2 {
        margin-top: 30px;
        font-size: 36px;
        color: white;
    }
    .content p {
        margin-top: 20px;
        font-size: 18px;
        color: white;
    }
    .github-link {
        margin-top: 20px;
        font-size: 18px;
    }
    .github-link a {
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
        <h2>Source Code</h2>
        <p>You can find the complete source code for the PlantCare project on our GitHub repository. The repository includes all the code, data, and resources needed to understand and replicate our work.</p>
        <div class="github-link">
            <a href="https://github.com/rohanbanduni/BCA-6th-sem-MPR" target="_blank">Visit our GitHub Repository</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    app()
