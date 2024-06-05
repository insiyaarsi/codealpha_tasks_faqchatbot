# app/chatbot.py
from app.faq_data import FAQData

class ChatBot:
    def __init__(self):
        self.faq_data = FAQData()

    def get_response(self, user_query):
        return self.faq_data.get_response(user_query)
