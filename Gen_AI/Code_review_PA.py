import google.generativeai as genai
import streamlit as st

# Setting up the API key
key = "AIzaSyBcvw-InpN6tRFqLmwZV8VV4TVRwIYIDUk"  # Replace this with your secure API key
genai.configure(api_key=key)

# Setting up the headers
st.title("👨‍💻 Your Code Review Buddy 🈂")
st.subheader("Issues with your Python code? Review your codebase now!")

# Taking user input
user_prompt = st.text_area("Enter your code...")

# If the button is clicked, generate responses
if st.button("Review") == True:
    model = genai.GenerativeModel(
        model_name="models/gemini-1.5-pro-latest",
        system_instruction="""
            You are a friendly AI assistant.
            Given a Python code to review, analyze the submitted code and identify bugs, errors, or areas of improvement.
            Provide the fixed code snippets.
            Explain the reasoning behind code corrections or suggestions.
            If the code is not in Python, politely remind the user that you are a Python code review assistant.
        """,
    )

    # If the prompt is provided
    if user_prompt:
        response = model.generate_content(user_prompt)
        
        # Printing the response on the webpage
        st.write(response.text)
