import logging
from flask import Flask, render_template, request, jsonify
from app.chatbot import ChatBot

app = Flask(__name__)
chatbot = ChatBot()

# Configure logging
logging.basicConfig(filename='chatbot.log', level=logging.INFO, 
                    format='%(asctime)s %(levelname)s:%(message)s')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_query = request.form['query']
    response = chatbot.get_response(user_query)
    
    # Log the query and response
    app.logger.info(f"User query: {user_query}")
    app.logger.info(f"Bot response: {response}")
    
    return jsonify({'response': response})

if __name__ == "__main__":
    port = 5000
    print(f"Running Flask app on http://127.0.0.1:{port}")
    app.run(debug=True, host='0.0.0.0', port=port)
