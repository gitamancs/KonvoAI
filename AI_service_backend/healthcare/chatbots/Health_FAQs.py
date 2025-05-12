import google.generativeai as genai
#from decouple import config

# Load the API key from .env
API_KEY = "AIzaSyBg_0TJ_miX2UHYFjxNp9nH7EYGi9LiOJA"
genai.configure(api_key=API_KEY)

class MedicalChatbot:
    def __init__(self, model_name="gemma-3-27b-it"):  # Default to a supported model
        self.model = genai.GenerativeModel(model_name)
        self.history = []
 
    def run(self, query):
        self.history.append(f"Patient: {query}")
        context = "\n".join(self.history[-5:])  # Last 5 messages
 
        prompt = f"""
        You are a medical assistant chatbot. Respond to the patient’s health-related questions in a simple, friendly, and medically accurate manner.
        Respond with clear, concise, and helpful information. Always provide information in a patient-friendly tone.
        If the query relates to symptoms, diseases, or treatments, provide accurate medical insights.
        Keep the conversation going.
        Give a short and concise answer.
 
        Question: {query}
 
        Conversation so far:
        {context}
 
        Chatbot:
        """
 
        try:
            response = self.model.generate_content(prompt)
            answer = response.text.strip()
            self.history.append(f"Chatbot: {answer}")
            return answer
        except Exception as e:
            return f"⚠️ Error: {str(e)}"