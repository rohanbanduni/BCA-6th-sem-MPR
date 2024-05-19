import streamlit as st

def app():
    # Custom CSS for styling
    st.markdown("""
    <style>
        .main-title {
            text-align: center;
            font-size: 48px;
            color:  #011f4b ;
            margin-bottom: 20px;
            font-family: 'Arial Black', sans-serif;
        }
        .sub-title {
            text-align: center;
            font-size: 24px;
            color: #011f4b;
            margin-bottom: 40px;
            font-family: 'Arial', sans-serif;
        }
        .info-section {
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 20px 0;
            padding: 20px;
            background-color: #f9f9f9;
            border: 2px solid #2E86C1;    
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .info-section img {
            max-width: 200px;
            border-radius: 10px;
            margin-right: 20px;
        }
        .info-section .text {
            max-width: 600px;
        }
        .info-section .text h3 {
            font-size: 24px;
            color: #011f4b;
            margin-bottom: 10px;
            font-family: 'Arial Black', sans-serif;
        }
        .info-section .text p {
            font-size: 16px;
            margin-bottom: 10px;
            font-family: 'Arial', sans-serif;
        }
    </style>
    """, unsafe_allow_html=True)

    # Main title
    st.markdown('<h1 class="main-title">Welcome to PlantCare</h1>', unsafe_allow_html=True)

    # Information Sections
    st.markdown("""
    <div class="info-section">
        <img src="https://images.pexels.com/photos/5876425/pexels-photo-5876425.jpeg?auto=compress&cs=tinysrgb&w=600" alt="Plant Disease">
        <div class="text">
            <h3>Understanding Plant Diseases</h3>
            <p>Plant diseases are caused by fungi, bacteria, and viruses. Diseases may harm crops and undermine food security. Early identification and classification are essential for management and control. PlantCare diagnoses plant diseases from leaf pictures using strong machine learning.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-section">
        <div class="text">
            <h3>Best Practices for Plant Care</h3>
            <p>Healthy plants require frequent attention and maintenance. This includes regular watering, sufficient sunlight, and ideal soil conditions. By following best practices for plant care, you may enhance plant health and productivity.</p>
        </div>
        <img src="https://images.pexels.com/photos/8280933/pexels-photo-8280933.jpeg?auto=compress&cs=tinysrgb&w=600" alt="Plant Care">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-section">
        <img src="https://images.pexels.com/photos/1108572/pexels-photo-1108572.jpeg?auto=compress&cs=tinysrgb&w=600" alt="Plant Monitoring">
        <div class="text">
            <h3>The Future of Plant Monitoring</h3>
            <p>With advancements in technology, the future of plant monitoring looks bright. Tools like PlantCare can integrate with IoT devices to provide real-time tracking and insights into plant health. By adopting these technologies, we can better manage plant health and improve agricultural productivity.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    app()
