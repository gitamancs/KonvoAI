import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from django.shortcuts import render
from AI_service_backend.healthcare.chatbots.Health_FAQs import MedicalChatbot

# Create your views here.
def index(request):
    return render(request, 'base/index.html')

def login_view(request):
    # Add your login logic or template here
    return render(request, 'base/login.html')

def healthcare(request):
    return render(request, 'base/healthcare.html')

def chatbot(request):
    if 'history' not in request.session:
        request.session['history'] = []

    if request.method == 'POST':
        query = request.POST.get('query', '')
        bot = MedicalChatbot()
        bot.history = request.session['history']
        response = bot.run(query)
        request.session['history'] = bot.history
        return render(request, 'base/chatbot.html', {'history': bot.history})
    else:
        return render(request, 'base/chatbot.html', {'history': request.session['history']})