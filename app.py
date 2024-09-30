import streamlit as st
import requests

# Set your Gemini API key here
API_KEY = 'AIzaSyBX7FjwaAgFT4-kBWw78U8nZ_D1YkyWdWs'  # Replace with your actual API key
API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent'

# Bootstrap-based CSS styling with background image and transparent elements
st.markdown("""
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
    .main {
        background-image: url('https://www.skillnetinc.com/wp-content/uploads/2023/10/AI-Chatbot-implementation-1366X600.webp'); 
        background-size: cover;
        padding: 30px;
        color: white;
        font-family: 'Dancing Script', cursive;
        font-size: 18px; /* Default font size for all text */
    }
    .title {
        font-size: 60px;
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    }
    .stTextArea textarea {
        font-size: 20px;
        padding: 15px;
        border-radius: 5px;
        border: 2px solid rgba(255, 255, 255, 0.7);
        background: grey;
        color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        background-color: grey;
        color: black;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 5px;
        border: 2px solid rgba(255, 255, 255, 0.7);
        margin-top: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: none; /* Remove mouse-over effect */
    }
    .stButton>button:hover {
        background-color: grey;  /* Set the hover color to be the same as the normal color */
        color: black;            /* Ensure text color stays the same */
}
    .stAlert {
        font-size: 18px;
        background: rgba(255, 255, 255, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.7);
        border-radius: 5px;
    }
    .stSpinner {
        color: rgba(0, 123, 255, 0.7);
    }
    </style>
    """, unsafe_allow_html=True)

def generate_content(prompt):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'contents': [{
            'parts': [{
                'text': prompt
            }]
        }]
    }
    
    response = requests.post(f"{'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent'}?key={'AIzaSyBX7FjwaAgFT4-kBWw78U8nZ_D1YkyWdWs'}", headers=headers, json=data)
    
    print("Response Status Code:", response.status_code)
    print("Response Body:", response.json())

    if response.status_code == 200:
        response_data = response.json()
        if 'candidates' in response_data and len(response_data['candidates']) > 0:
            return response_data['candidates'][0]['content']['parts'][0]['text']
        else:
            return 'No candidates found in response.'
    else:
        return f"Error: {response.status_code} - {response.text}"

def main():
    st.markdown("<div class='title'>ThBotX AI</div>", unsafe_allow_html=True)
    st.write("Enter your content topic or prompt below:")
    
    prompt = st.text_area("Prompt", "")
    
    if st.button("Generate Content"):
        if prompt:
            with st.spinner("Generating content..."):
                content = generate_content(prompt)
                st.success("Content generated successfully!")
                st.write(content)
        else:
            st.warning("Please enter a prompt.")

if __name__ == "__main__":
    main()
