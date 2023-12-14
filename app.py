from flask import Flask, render_template, request
from dotenv import load_dotenv

app = Flask(__name__)

@app.route("/")
def chat():
    return render_template('index.html')

@app.route("/memory")
def memory():
    return "<p>memory</p>"

@app.route("/apikey/<name>")
def update_apikey(name):
    return "<p>memory sectioned</p>"

@app.route("/memory/section/<name>")
def memory_section(name):
    return "<p>memory sectioned</p>"

@app.route("/brain/agent/<name>", methods=["POST"])
def brain_agent(name):
    return "<p>Calling the agent</p>"

@app.route("/chat/input", methods=["POST"])
def chat_input():
    data = request.json
    message = data.get('message')
    # Process the chat message
    return 'Message received', 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5002)