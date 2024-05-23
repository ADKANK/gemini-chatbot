## Chatbot - Gemini

### Description
This is a Gemini chatbot using streamlit python library. Using the chatbot it will perform the task of a personal assistant. It will help you to get the information about the weather, news, and also it will help you to get the information about the stock market. 

### Installation
To install the required libraries and dependencies, run the following command:
```bash
pip install -r requirements.txt
```

### Configuration
To configure the chatbot, you need to create a `.env` file in the root directory and add the following variables:
```bash
GOOGLE_API_KEY='your_google_api_key'
```
API key can be generated from the [Google Cloud](https://cloud.google.com/docs/authentication/api-keys) platform or [AI Studio](https://aistudio.google.com/app/apikey).

### Usage
To run the chatbot, run the following command:
```bash
streamlit run app.py
```
