<h2> FAQ Chatbot </h2>

<b> Project Description </b> <br>
The FAQ Chatbot is a Natural Language Processing (NLP) based chatbot designed to answer frequently asked questions (FAQs) about a particular topic or product. This project leverages pre-built NLP libraries such as NLTK and SpaCy to understand and generate responses to user queries. Additionally, the project features a simple and user-friendly GUI built with HTML and CSS. 


<b> Project Structure </b> <br> <br>
faqchatbot/ <br>
│ <br>
├── app/ <br>
│   ├── __init__.py <br>
│   ├── chatbot.py <br>
│   └── faq_data.py <br>
│ <br>
├── static/ <br>
│   ├── bg.jpg <br>
│   └── style.css <br>
│ <br>
├── templates/ <br>
│   └── index.html <br>
│ <br>
├── faqvenv/ (virtual environment directory) <br>
│ <br>
├── chatbot.log <br>
├── main.py <br>
├── requirements.txt <br>
└── README.md <br>


<b>How It Works</b> <br>
<ul>
<li>User Interaction: The user interacts with the chatbot through a web interface. The user enters a question in the input field and clicks the "Send" button. </li>
<li>Processing Query: The user query is sent to the backend where the chatbot processes it using NLP techniques. </li>
<li>Response Generation: The chatbot searches for the most relevant answer from a pre-defined list of FAQs. If the query matches closely with an FAQ, the corresponding answer is returned. If not, a default response indicating that the query has been noted is returned. </li>
<li>Displaying Response: The response is then displayed on the web interface for the user. </li>
</ul>


<b> Libraries Used </b> <br>
<ul>
<li> Flask: For creating the web server and handling HTTP requests. </li>
<li> NLTK: For basic NLP operations. </li>
<li> SpaCy: For advanced NLP operations and tokenization. </li>
<li>scikit-learn: For vectorization and similarity computation. </li>
<li>Jinja2: For templating in Flask. </li>
</ul>


<b>Installation </b>
Set Up Virtual Environment: <br> 
<pre>python -m venv faqvenv
source faqvenv/bin/activate  # On Windows, use `faqvenv\Scripts\activate`
</pre>
<br> 
Install Dependencies: <br> 
<pre>pip install -r requirements.txt
</pre>
<br> 
Run the Application: <br> 
<pre>python main.py
</pre>
<br>  


<b> Usage </b>
1. Open your web browser and go to http://127.0.0.1:5000. <br>
2. Ask a question in the input field and press "Send".<br>
3. View the response generated by the chatbot. <br>


<b>Files and Their Purpose </b> <br>
1. main.py <br>
This is the main entry point of the application.
It sets up the Flask server, defines routes for the home page and the chatbot response API.
It initializes the chatbot and configures logging.

2. app/__init__.py <br>
This file initializes the app module.
app/chatbot.py
Contains the ChatBot class that processes user queries and returns responses.
Uses SpaCy and scikit-learn for vectorization and similarity computation.

3. app/faq_data.py <br>
Contains the FAQData class that stores FAQs and their corresponding answers.
Performs tokenization and vectorization of questions.

4. static/style.css <br>
Contains the CSS styles for the web interface.
Defines the layout and appearance of the chatbot interface.

5. static/bg.jpg <br>
Background image for the web interface to enhance visual appeal.

6. templates/index.html <br>
HTML template for the web interface.
Uses Jinja2 templating to render dynamic content.

7. requirements.txt <br>
Lists all the Python dependencies required for the project.
Facilitates easy setup of the development environment.

8. chatbot.log <br>
Log file to store logs for debugging and monitoring purposes.
Records user queries and chatbot responses.

9. README.md <br>
This file provides an overview of the project, its structure, how to set it up, and how to use it.