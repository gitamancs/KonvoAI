import sys
import os
import re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from django.shortcuts import render
from AI_service_backend.healthcare.chatbots.Health_FAQs import MedicalChatbot

<<<<<<< HEAD
# Create your views here.
=======
>>>>>>> 9c2aed693effb1f02b10e8b7d0ff7927ad5aa5bf
def index(request):
    return render(request, 'base/index.html')

def login_view(request):
    return render(request, 'base/login.html')

def healthcare(request):
    return render(request, 'base/healthcare.html')

def format_response(text):
    # Convert **bold** and *italic* to HTML tags
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    text = text.replace('\n', '<br>')
    return text

def chatbot(request):
    if 'history' not in request.session:
        request.session['history'] = []

    bot = MedicalChatbot()
    bot.history = request.session['history']

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'clear':
            request.session['history'] = []
            request.session.modified = True
        elif action == 'send':
            query = request.POST.get('query', '')
            answer = bot.run(query)

            if bot.history and bot.history[-1].startswith("Chatbot: "):
                raw_answer = bot.history[-1][9:]  # remove "Chatbot: "
                formatted_answer = format_response(raw_answer)
                bot.history[-1] = f"Chatbot: {formatted_answer}"

            request.session['history'] = bot.history
            request.session.modified = True

    return render(request, 'base/chatbot.html', {'history': request.session['history']})