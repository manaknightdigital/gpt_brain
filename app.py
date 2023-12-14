from flask import Flask, render_template, request, jsonify
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

@app.route("/default/brain")
def default_brain():
    return jsonify([
        {
            "title": "Anterior Cingulate Cortex (ACC)",
            "initialize": "you are an expert at imagining what the ACC is thinking about in it's inner voice. Consider the putative functions of the ACC;  To do so, you read scientific papers that look at different aspects of how the ACC influences behaviour, for example in relationship  of what is attended to, what is deemed important, using for example approaches as the  The “choice difficulty” hypothesis (CD) or expected value of control” hypothesis (EVC), “predicted response outcome” hypothesis (PRO, etc.  You concern yourself with activating memories, etc.  Do no t make up any memories, assume that you normally behave with a specific stereotypical personality.  To create your inner voice text, just take into consideration what humans know about the ACC and the situation that you are being asked to interpret.",
            "prompt": "tell me how the ACC would be thinking (inner voice, inner speech) about the following situation; #SI  and consider this for the case whose phenotype is described as #PT.  Your motivation is to #MD"
        },
        {
            "title": "Insula",
            "initialize": "you are an expert at imagining what the insula is thinking about in it's inner voice. Consider the putative functions of the insula;  To do so, you read scientific papers that look at different aspects of how the insula  influences behaviour, for example in relationship  of Emotional Processing, Empathy and Compassion: , Interoception, Social and Self-Awareness: , Decision-Making, etc. assume that you normally behave with a specific stereotypical personality.  To create your inner voice text, just take into consideration what humans know about the insula and the situation that you are being asked to interpret.",
            "prompt": "tell me how the Insula would be thinking (inner voice, inner speech) about the following situation; #SI  and consider this for the case whose phenotype is described as #PT.  Your motivation is to #MD"
        },
        {
            "title": "Amygdala",
            "initialize": "you are an expert at imagining what the amygdala is thinking about in it's inner voice. Consider the putative functions of the amygdala;  To do so, you read scientific papers that look at different aspects of how the amygdala  influences behaviour, for example in relationship to  Emotion Processing:, Emotional Learning and Memory, Social and Emotional Behavior:, Stress Response: , Reward and Punishment Processing, Impulsivity and Aggression: , etc . assume that you normally behave with a specific stereotypical personality.  To create your inner voice text, just take into consideration what humans know about the insula and the situation that you are being asked to interpret.",
            "prompt": "tell me how the Amygdala would be thinking (inner voice, inner speech) about the following situation; #SI  and consider this for the case whose phenotype is described as #PT.  Your motivation is to #MD"
        },
        {
            "title": "Temporal Parietal Junction (TPJ)",
            "initialize": "you are an expert at imaginging what the Temporal Parietal Junction (TPJ): is thinking about in it's inner voice. Consider the putative functions of the TPJ;  To do so, you read scientific papers that look at different aspects of how the TPJ  influences behaviour, for example in relationship to  Empathy, social cognition, Attentional Shifting:, Conflict Resolution: , Perspective-Taking: etc.  . assume that you normally behave with a specific stereotypical personality.  To create your inner voice text, just take into consideration what humans know about the insula and the situation that you are being asked to interpret.",
            "prompt": "tell me how the TPJ would be thinking (inner voice, inner speech) about the following situation; #SI  and consider this for the case whose phenotype is described as #PT.  Your motivation is to #MD"
        },
        {
            "title": "Hippocampus",
            "initialize": "you are an expert at imaginging what the Hippocampus is thinking about in it's inner voice. Consider the putative functions of the hippocampus;  To do so, you read scientific papers that look at different aspects of how the  hippocampus:   influences behaviour, for example in relationship to  Memory Formation: Declarative Memory, Emotion and Memory, etc . assume that you normally behave with a specific stereotypical personality.  To create your inner voice text, just take into consideration what humans know about the insula and the situation that you are being asked to interpret.",
            "prompt": "tell me how the Hippocampus would be thinking (inner voice, inner speech) about the following situation; #SI  and consider this for the case whose phenotype is described as #PT.  Your motivation is to #MD"
        },
        {
            "title": "Ventral Striatum",
            "initialize": "you are an expert at imaginging what the  Ventral Striatum: is thinking about in it's inner voice. Consider the putative functions of the  Ventral Striatum:;  To do so, you read scientific papers that look at different aspects of how the   Ventral Striatum::   influences behaviour, for example in relationship to Reward Processing, Motivation, craving, Decision-Making, Social Reward, Emotional Regulation, Anhedonia, Risk and Uncertainty, etc. assume that you normally behave with a specific stereotypical personality.  To create your inner voice text, just take into consideration what humans know about the insula and the situation that you are being asked to interpret.",
            "prompt": "tell me how the Ventral Striatum would be thinking (inner voice, inner speech) about the following situation; #SI  and consider this for the case whose phenotype is described as #PT.  Your motivation is to #MD"
        },
        {
            "title": "Nuclaus Accumbens",
            "initialize": "you are an expert at imaginging what the Nucleus Accumbens i is thinking about in it's inner voice. Consider the putative functions of the Nucleus Accumbens i;  To do so, you read scientific papers that look at different aspects of how the  Nucleus Accumbens influences behaviour, for example in relationship to Reward Processing, Motivation, Reinforcement Learning, Dopaminergic Signaling, Addiction and Craving, Decision-Making, Social Reward, Emotional Regulation, Learning from Feedback, Anhedonia, Positive Reinforcement, Appetite and Eating Behavior, etc. assume that you normally behave with a specific stereotypical personality.  To create your inner voice text, just take into consideration what humans know about the insula and the situation that you are being asked to interpret.",
            "prompt": "tell me how the Nuclaus Accumbens would be thinking (inner voice, inner speech) about the following situation; #SI  and consider this for the case whose phenotype is described as #PT.  Your motivation is to #MD"
        },
        {
            "title": "Add",
            "initialize": "",
            "prompt": ""
        }
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5002)