import streamlit as st

def app():

    # Title of the webpage
    st.title("Contact Us")

    # Description
    st.write("If you have any questions or feedback about PlantCare, please don't hesitate to reach out to us. Please fill out the form below and we'll get back to you as soon as possible.")

    # Custom CSS for the form
    form_css = """
    <style>
        form {
            display: flex;
            flex-direction: column;
        }
        label {
            margin: 5px 0 5px 0;
        }
        input, textarea {
            margin: 5px 0 15px 0;
            padding: 8px;
            width: 100%;
            box-sizing: border-box;
        }
        button {
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
    """

    # Form creation with CSS
    form_html = """
    <form action="https://formsubmit.co/1e432f980c6062411f418d4cf75ca142" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="4" required></textarea>
        <button type="submit">Submit</button>
    </form>
    """

    # Display the form with custom CSS
    st.markdown(form_css + form_html, unsafe_allow_html=True)
