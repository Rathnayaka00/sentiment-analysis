import streamlit as st
import requests

st.title("Sentiment Analysis Web App")

st.write("""
This application analyzes the sentiment of a given text. 
It returns one of the following results:
- **Positive**
- **Negative**
""")

user_input = st.text_area("Enter your review or tweet here:")

if st.button('Analyze Sentiment'):
    if user_input:
        url = 'http://127.0.0.1:5000/predict' 
        response = requests.post(url, json={'review': user_input})
        
        if response.status_code == 200:
            data = response.json()
            sentiment = data.get('sentiment')
            
            if sentiment == "Positive":
                st.markdown(f'<p style="color:green; font-size: 30px;">😊 <strong>{sentiment}</strong></p>', unsafe_allow_html=True)
            elif sentiment == "Negative":
                st.markdown(f'<p style="color:red; font-size: 30px;">😞 <strong>{sentiment}</strong></p>', unsafe_allow_html=True)
            else:
                st.markdown(f'<p style="font-size: 30px;">The sentiment of the given text is: <strong>{sentiment}</strong></p>', unsafe_allow_html=True)
        else:
            st.error("Error: Unable to analyze sentiment.")
    else:
        st.error("Please enter some text to analyze.")
