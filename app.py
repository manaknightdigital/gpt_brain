from flask import Flask
from dotenv import load_dotenv

app = Flask(__name__)

@app.route("/")
def chat():
    return "<p>chat</p>"

@app.route("/memory")
def memory():
    return "<p>memory</p>"

@app.route("/apikey/<name>")
def update_apikey(name):
    return "<p>memory sectioned</p>"

@app.route("/memory/section/<name>")
def memory_section(name):
    return "<p>memory sectioned</p>"

@app.route("/brain/agent/<name>", method=["POST"])
def brain_agent(name):
    return "<p>Calling the agent</p>"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5002)