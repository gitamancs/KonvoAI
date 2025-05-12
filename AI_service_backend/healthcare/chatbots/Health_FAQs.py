from .databricks_utils import score_model

class MedicalChatbot:
    def __init__(self):
        self.history = []
 
    def run(self, query):
        self.history.append(f"Patient: {query}")
    
        try:
            response = score_model([query])
            print("Databricks response:", response)
            
            if 'predictions' in response:
                if isinstance(response['predictions'], list):
                    answer = response['predictions'][0]
                elif isinstance(response['predictions'], dict):
                    answer = response['predictions'].get('response', "⚠️ No 'response' key in predictions")
                else:
                    answer = f"⚠️ Unexpected type for 'predictions': {type(response['predictions'])}"
            elif 'outputs' in response:
                answer = response['outputs'][0] if isinstance(response['outputs'], list) else response['outputs']
            elif isinstance(response, list) and len(response) > 0:
                answer = response[0]
            else:
                answer = f"⚠️ Unexpected response format: {response}"
            
            self.history.append(f"Chatbot: {answer}")
            return answer
        except Exception as e:
            error_msg = f"⚠️ Error: {str(e)}"
            self.history.append(f"Chatbot: {error_msg}")
            return error_msg