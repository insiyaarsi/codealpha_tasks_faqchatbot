# app/faq_data.py
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

class FAQData:
    def __init__(self):
        self.questions = [
            "What is your return policy?",
            "How do I track my order?",
            "Can I purchase items online?",
            "Do you offer international shipping?",
            "How do I contact customer support?",
            "How can I reset my password?",
            "What payment methods do you accept?",
            "How can I cancel my order?",
            "What is the estimated delivery time?",
            "What should I do if I receive a damaged item?",
            "Do you offer a loyalty program?"
            "How do I unsubscribe from your newsletter?"
        ]
        self.answers = [
            "Our return policy is 30 days no questions asked.",
            "You can track your order using the tracking number provided in your email.",
            "Yes, items can be purchased online through our website.",
            "Yes, we offer international shipping to select countries.",
            "You can contact customer support via email or our support hotline.",
            "You can reset your password by clicking on the 'Forgot Password' link on the login page. Follow the instructions sent to your registered email.",
            "We accept Visa, MasterCard, American Express, PayPal, and bank transfers.",
            "To cancel your order, please contact our customer support team as soon as possible. Orders can only be canceled before they are shipped.",
            "The estimated delivery time is 5-7 business days for domestic orders and 10-15 business days for international orders.",
            "If you receive a damaged item, please contact our customer support team within 48 hours of receiving the package. We will arrange for a replacement or refund.",
            "Yes, we offer a loyalty program. You can earn points on every purchase and redeem them for discounts on future orders. Sign up on our website to join the program.",
            "To unsubscribe from our newsletter, click on the 'Unsubscribe' link at the bottom of any newsletter email you receive from us."
            
        ]
        self.vectorizer = TfidfVectorizer(tokenizer=self.spacy_tokenizer, token_pattern=None)
        self.question_vectors = self.vectorizer.fit_transform(self.questions)

    def spacy_tokenizer(self, text):
        doc = nlp(text)
        return [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]

    def get_response(self, user_query):
        query_vector = self.vectorizer.transform([user_query])
        similarities = cosine_similarity(query_vector, self.question_vectors).flatten()
        best_match_index = similarities.argmax()
        if similarities[best_match_index] < 0.2:  # Threshold for unknown questions
            return "Thank you for your question. It has been noted. We will respond back to you shortly!"
        return self.answers[best_match_index]
