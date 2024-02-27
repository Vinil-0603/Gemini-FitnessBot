import google.generativeai as genai
import gradio as gr

# Replace 'YOUR_API_KEY' with your actual Gemini Advanced API key
genai.configure(api_key='YOUR-API-KEY')
model = genai.GenerativeModel('gemini-pro')

def chatbot_response(user_input):
    response = model.generate_content(user_input)
    return response.text

# Create the Gradio interface
interface = gr.Interface(
    fn=chatbot_response,
    inputs="textbox",  
    outputs="textbox",
    title="Gemini Chatbot"
)

interface.launch() 
