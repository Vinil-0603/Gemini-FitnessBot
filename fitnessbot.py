import google.generativeai as genai
import gradio as gr

# Replace 'YOUR_API_KEY' with your actual Gemini Advanced API key
genai.configure(api_key='YOUR-API-KEY')
model = genai.GenerativeModel('gemini-pro')  

def chatbot_response(user_input):
    prompt = f"As a fitness and nutrition expert, answer the following question: {user_input}"  
    response = model.generate_content(prompt)
    return response.text

# Create the Gradio interface (no changes needed here)
interface = gr.Interface(
    fn=chatbot_response,
    inputs="textbox",  
    outputs="textbox",
    title="Gemini Fitness & Nutrition Chatbot" 
)

interface.launch() 