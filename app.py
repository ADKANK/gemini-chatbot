from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create a generative model
model=genai.GenerativeModel("gemini-1.5-pro-latest") 
# Start a chat with the model
chat = model.start_chat(history=[])

# Function to get response from the model
def get_gemini_response(question):   
    response=chat.send_message(question,stream=True)
    return response

st.set_page_config(page_title="Gemini LLM Application")

st.header("Gemini LLM Application")

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Input: ",key="input") # Input text box
submit=st.button("Ask the question") # Submit button
# If the submit button is clicked and input is not empty
if submit and input:
    response=get_gemini_response(input) # Get response from the model
    st.session_state['chat_history'].append(("You", input)) # Append the user input to chat history
    st.subheader("The Response is") # Display the response
    for chunk in response: 
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))
st.subheader("The Chat History is")

# Display the chat history    
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")