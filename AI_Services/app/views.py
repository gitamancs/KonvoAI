import sys
import os
import re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from django.shortcuts import render
from AI_service_backend.healthcare.chatbots.Health_FAQs import MedicalChatbot

def index(request):
    return render(request, 'base/index.html')

def login_view(request):
    return render(request, 'base/login.html')

def healthcare(request):
    return render(request, 'base/healthcare.html')

def format_response(text):
    # Convert **text** to <strong>text</strong> for bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # Convert *text* to <em>text</em> for italic
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    # Replace \n with <br> for proper line breaks in HTML
    text = text.replace('\n', '<br>')
    return text

def chatbot(request):
    if 'history' not in request.session:
        request.session['history'] = []

    if request.method == 'POST':
        query = request.POST.get('query', '')
        bot = MedicalChatbot()
        bot.history = request.session['history']
        bot.run(query)
        if bot.history and bot.history[-1].startswith("Chatbot: "):
            plain_response = bot.history[-1][9:]  # Remove "Chatbot: "
            formatted_text = format_response(plain_response)
            formatted_response = f'<p>{formatted_text}</p>'
            bot.history[-1] = f"Chatbot: {formatted_response}"
        request.session['history'] = bot.history
        return render(request, 'base/chatbot.html', {'history': bot.history})
    else:
        return render(request, 'base/chatbot.html', {'history': request.session['history']})
