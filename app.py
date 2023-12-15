from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI
import os
import time

load_dotenv()

app = Flask(__name__)

openaiKey = os.environ.get("OPENAI_KEY")

@app.route("/")
def chat():
    return render_template('index.html')

@app.route("/apikey/<name>")
def update_apikey(name):
    openaiKey = name
    return "Updated", 200

@app.route('/t1', methods=['POST'])
def t2():
    data = request.json
    brainData = data['brainParts']
    response_texts = []

    client = OpenAI(api_key=openaiKey)
    for item in brainData:

        if item['title'].lower() == 'add':
            break

        prompt = item['prompt']
        prompt = prompt.replace("#SI", "(" + data['situation'] + ")")
        prompt = prompt.replace("#PT", "(" + data['phenotype'] + ")")
        prompt = prompt.replace("#MD", "(" + data['motivatedBehavior'] + ")")

        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        n=1,
        messages=[
            {"role": "system", "content": item['initialize']},
            {"role": "user", "content": prompt}
        ]
        )

        response_texts.append({
            'title': item['title'],
            't2': response.choices[0].message.content,
            'chat_id': response.id,
            'usage': {
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
                "total_tokens": response.usage.total_tokens
            }
        })

        time.sleep(1)

    return jsonify(response_texts)

@app.route('/t4', methods=['POST'])
def t4():
    data = request.json
    brainData = data['brainParts']

    initialize = 'you are an expert on the Prefrontal Cortex (PFC) and its subparts, and connections to other brain regions, in particular as to how all  of these influence behaviour, particularly in the next action to take. you consider all relevant inputs;'
    prompt = 'tell me how the Prefrontal Cortex (PFC) would be thinking (inner voice, inner speech) about the following situation; #SI  and consider this for the case whose phenotype is described as #PT and whose internal state is described as #IS  our motivation is to #MD.  To guide your thinking consider how well it aligns towards your objective #MD and how well it takes into account the need to solve any obstacles, obstructions, or difficulties, while at the same time creatively looking for solutions via opportunities, shortcuts, etc. also consider the actions that gives you the most progress at an acceptable degree of risk."  make sure you give each brain part\'s inner voice consideration  below , but you decide to what degree.  once you told me about what your "PFC inner voice" is thinking, tell what action you intend to take.'
    prompt = prompt.replace("#SI", "(" + data['situation'] + ")")
    prompt = prompt.replace("#PT", "(" + data['phenotype'] + ")")
    prompt = prompt.replace("#MD", "(" + data['motivatedBehavior'] + ")")

    client = OpenAI(api_key=openaiKey)

    for item in brainData:

        if item['title'].lower() == 'add':
            break

        prompt += "\n"
        prompt += "Sub Brain Part: " + item['title']
        prompt += "\n"
        prompt += "Sub Brain Inner Voice: " + item['chat']

        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        n=1,
        messages=[
            {"role": "system", "content": initialize},
            {"role": "user", "content": prompt}
        ]
        )

    return jsonify({
        'title': "Prefrontal Cortex (PFC)",
        't4': response.choices[0].message.content,
        'chat_id': response.id,
        'usage': {
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens
        }
    })

@app.route("/t41", methods=["POST"])
def dummy2():
    return jsonify({
    "chat_id": "chatcmpl-8ViLTN0NKapjcr6OMGhPHciH9QrNB",
    "t4": "Based on the inner voices of the different subparts of the Prefrontal Cortex (PFC) in this highly stressed individual, the PFC is constantly evaluating the situation and assessing the potential control the individual has. The Anterior Cingulate Cortex (ACC) is monitoring the internal and external environment, recognizing the high stress levels and lack of sleep, and urging the individual to find ways to cope with the discomfort. The Insula is hyperaware of the sensory inputs and bodily sensations, contributing to the individual's stress and discomfort. The Amygdala is reminding the individual to stay calm, find distractions, and focus on the goal of getting home. The Temporal Parietal Junction (TPJ) is helping the individual understand the social dynamics and empathize with others, while also reminding them to prioritize their own well-being. The Hippocampus is reflecting on the impact of stress and sleep on mental and emotional well-being and emphasizing the importance of self-care. The Ventral Striatum is highlighting the individual's motivation to reach home and find peace, while the Nucleus Accumbens is reinforcing the reward aspect of reaching home and seeking ways to manage stress.\n\nConsidering all these inputs, the individual's PFC is driven by the goal of getting home and finding relief. It is aware of the challenges and discomfort of the crowded bus, but it is also focused on finding ways to cope, distract, and prioritize self-care. The PFC is evaluating the risks and rewards, and considering the individual's resilience and ability to endure the situation.\n\nTaking all this into account, the most likely action the individual intends to take is to persevere, prioritize distractions (such as listening to music or a podcast), practice deep breathing or mindfulness to manage stress, and remain focused on the anticipation of reaching home as the reward. The individual is also considering strategies to improve sleep hygiene and overall well-being, as well as maintaining empathy and understanding for the other passengers' potential experience in a crowded bus.",
    "title": "Prefrontal Cortex (PFC)",
    "usage": {
        "completion_tokens": 400,
        "prompt_tokens": 3507,
        "total_tokens": 3907
    }
})

@app.route("/t11", methods=["POST"])
def dummy():
    return jsonify([
    {
        "chat_id": "chatcmpl-8VhtGs6Df5IGbMShShrwJkpBgkRu2",
        "t2": "Ugh, here we go again. Another packed bus ride home. Why does this always happen to me? I can already feel the stress building up. I didn't get much sleep last night, and now I have to deal with this overcrowded bus. Just great.\n\nOkay, let's assess the situation here. We're stuck at the back of the bus, surrounded by all these people. It's uncomfortably hot, and there's barely any space to move. This is not ideal, to say the least. I really need to get home and unwind after such a tough day at work. My motivation is to make it through this ride and finally reach the comfort of my own house.\n\nNow, what's the ACC's role in all of this? Well, it's responsible for monitoring my internal and external environment, and making decisions based on the perceived importance and difficulty of tasks. So, let's see how it's interpreting this situation.\n\nThe ACC is definitely registering the high stress levels I'm experiencing. It's probably thinking, \"Wow, we're really feeling the pressure today. This bus ride is adding yet another layer of stress to an already exhausting day.\" It's also aware of the lack of sleep I had, which might further contribute to my overall stress levels.\n\nIn terms of attention, the ACC is helping me focus on what's important in this situation. It's directing my attention towards finding a way to make it through this crowded bus, urging me to look for any available seats or spots that might offer a little relief. At the same time, it's also filtering out irrelevant information, like the noise and conversations happening around me, to minimize distractions.\n\nThe ACC is constantly evaluating the difficulty of this situation and assessing the potential control I have. It recognizes that there's not much I can personally do to change the crowded bus scenario, but it might prompt me to think about strategies to cope with the discomfort, like taking deep breaths or finding a way to mentally detach from my surroundings.\n\nOverall, the ACC is aware of my strong desire to reach home and rest. It's constantly evaluating the situation, weighing the importance of getting through this bus ride against the challenges it presents. It's urging me to stay resilient and find ways to manage the stress, as it knows that the reward of finally arriving home will be worth it. Hang in there, buddy, we'll get through this!",
        "title": "Anterior Cingulate Cortex (ACC)",
        "usage": {
            "completion_tokens": 484,
            "prompt_tokens": 268,
            "total_tokens": 752
        }
    },
    {
        "chat_id": "chatcmpl-8VhtUpgZMRvZRVADzxwGZKvdWavIh",
        "t2": "Inner Voice of the Insula in a Highly Stressed Individual:\n\nGosh, this bus is packed to the brim! Why does this always happen when I'm already so stressed out? I can feel the tension rising in my body as I'm forced to stand in this cramped space at the back of the bus. I just want to go home and decompress after a long, exhausting day at work.\n\nUgh, I can't help but feel overwhelmed by the close proximity of all these people. The lack of personal space is making me feel even more stressed. I can sense my heart rate increasing and my palms getting sweaty. Focus, just focus.\n\nI can't help but notice the various smells emanating from the bus. The combination of odors, both pleasant and unpleasant, is making it harder for me to relax. I wish I could block out these sensory inputs and find some peace in this crowded environment.\n\nI can feel the subtle vibrations of the bus beneath me, and it's triggering a sense of unease. It's as if my body is constantly reminding me of the discomfort I am experiencing. It's frustrating because I just want to find comfort and solace during this journey.\n\nAs the bus moves through the streets, I can feel a wave of nausea engulfing me. The constant jostling and bouncing around is taking a toll on my already tired and exhausted body. It's becoming increasingly difficult to suppress the rising frustration and irritation inside me.\n\nMy mind keeps drifting to thoughts of home, picturing the coziness and tranquility waiting for me there. I yearn for a moment of respite, away from the chaos and stress of my daily routine. The anticipation of reaching my destination is both comforting and motivating me to endure this uncomfortable bus ride.\n\nAlthough this situation is challenging for me, I need to remind myself to stay calm and collected. By focusing on my breathing and practicing mindfulness, I can create a sense of inner calm amidst the external chaos. I must remember that this temporary discomfort will eventually pass, and I'll be one step closer to relaxing in the comfort of my own home.",
        "title": "Insula",
        "usage": {
            "completion_tokens": 426,
            "prompt_tokens": 235,
            "total_tokens": 661
        }
    },
    {
        "chat_id": "chatcmpl-8VhthRyNJNKss10unKgdu00yRC2sb",
        "t2": "Inner Voice: Okay, let's see what we've got here. A crowded bus, huh? I can already feel the stress levels rising. It's the end of the day, and all I want is to get home, but it looks like that's not going to be an easy task today. Great.\n\nInner Voice: Alright, calm down, Amygdala. Take a deep breath. We knew this situation was a possibility, and now we have to deal with it. Let's assess the situation. The bus is packed, so finding a seat might be a challenge. But that's not the end of the world, right? We're tough, we can handle standing for a while.\n\nInner Voice: Ugh, I hate being stuck in the back. It's so cramped and uncomfortable. But hey, it's just a temporary inconvenience. Focus on your goal, which is getting home. You need to remind yourself that this isn't a personal attack, it's just a packed bus. People are in a hurry and trying to go places, just like you.\n\nInner Voice: Keep your cool, Amygdala. Remember, your stress levels are already pretty high. Getting upset or agitated won't do any good. Instead, let's try to find ways to distract ourselves. Maybe we can listen to some music or a podcast. Anything to take our mind off the cramped space and the stress.\n\nInner Voice: Oh, look! There's a seat up ahead! Let's make a move quickly before someone else takes it. Phew, finally some relief. Sit down, take a deep breath, and enjoy the short break. We've earned it.\n\nInner Voice: Now, let's keep reminding ourselves that this is just a temporary situation. Anticipate that the rest of the journey might be filled with stop-and-go traffic, loud noises, and possibly more discomfort. But that's okay. It's all part of the process of getting back home.\n\nInner Voice: Hang in there, Amygdala. We're almost home. We've made it through countless similar situations before, and we can do it again. Just a little bit longer, and we'll be able to relax and unwind in the comfort of our own house.\n\nInner Voice: Okay, we're here. Finally. Take a deep breath and let go of the stress and tension. It's time to leave the bus and leave the day behind. Remember, tomorrow is a new day, and we can face whatever challenges come our way with a fresh mindset.",
        "title": "Amygdala",
        "usage": {
            "completion_tokens": 513,
            "prompt_tokens": 245,
            "total_tokens": 758
        }
    },
    {
        "chat_id": "chatcmpl-8VhtvtB4H4XhJhEEzLhljJUoKyEQk",
        "t2": "Oh great, just what I needed after such a long and exhausting day at work - a crowded bus. Why is it always so packed when I'm desperate to get home? I can already feel my stress levels rising. The noise, the heat, and the lack of personal space are really not helping right now. \n\nLooking around, I see that every seat is taken, and people are practically squished against each other. I'm stuck at the back, surrounded by strangers, and I can't even find a place to hold on to. Fantastic. Just fantastic.\n\nMy mind is racing, thinking about how much longer this journey is going to be. An hour feels like an eternity when you're tired and just want some peace and quiet. I can't help but feel frustrated, questioning why the universe is always testing my patience like this.\n\nAs I stare out the window, my mind starts to wander. I find myself contemplating the concept of empathy; wondering if anyone else on this bus is feeling as drained and overwhelmed as I am. Are they also counting down the minutes until they can escape this chaotic environment?\n\nThe Temporal Parietal Junction (TPJ) inside me starts to activate, trying to make sense of the social dynamics happening around. It shows some interest in social cognition, attempting to gauge the mood and emotions of those around me. I wonder if anyone would be willing to give up their seat for those who appear more tired than they do. Perhaps observing these interactions could provide some small relief from my own discomfort, reminding me that I'm not alone in my exhaustion.\n\nBut as my attention shifts, conflict arises within me. On one hand, I want to URGENTLY get home, rest, and rejuvenate. On the other hand, I don't want to become the annoying passenger who aggressively demands a seat or inconveniences others. I try to balance my perspective, hoping that someone who needs it more than me will be granted a seat eventually.\n\nThe TPJ continues to work, aiding in perspective-taking. It makes me aware that maybe some of these fellow passengers are also longing for the solace of their homes, just like me. Recognizing our shared predicament, it softens my irritation slightly and helps me understand that everyone is dealing with their own battles.\n\nAs time goes on, I realize that my ability to handle this stressful situation ultimately relies on my own mindset and resilience. I try not to let the discomfort consume me entirely, reminding myself that this is just a temporary inconvenience. Slowly, my focus shifts from the chaos surrounding me to the anticipation of finally reaching my destination, knowing that some peace and quiet await me at home.",
        "title": "Temporal Parietal Junction (TPJ)",
        "usage": {
            "completion_tokens": 537,
            "prompt_tokens": 239,
            "total_tokens": 776
        }
    },
    {
        "chat_id": "chatcmpl-8VhuAnkUhL2aWsOsGGEIg3u26QCAC",
        "t2": "Inner voice of the Hippocampus (highly stressed, no good sleep, coming home from work after a hard day):\n\n\"Oh no, not another crowded bus. Why does it always have to be this way? I just want to get home and relax. The back of the bus seems to be the only available spot, but it's already packed. I can feel the stress building up inside me. My tired body craves rest, but this situation is making it even harder to find some peace.\"\n\n\"I know I need to find a way to make this journey more bearable. Maybe I can distract myself with my thoughts. I could focus on the tasks that need to be done at home. Grocery shopping, cooking, cleaning \u2013 there's always something to keep me occupied. But all I want is to let go of the day's worries and find solace in the comfort of my own space.\"\n\n\"I can't help but reflect on how my lack of sleep is impacting my ability to handle stress. It feels like an endless cycle \u2013 the more stressed I am, the worse my sleep becomes, and the worse my sleep, the more stressed I am. It's a tough battle, but I shouldn't let it define me or ruin my mood. I should focus on finding ways to improve my sleep hygiene and manage my stress levels more effectively in the future.\"\n\n\"I long for that feeling of familiarity and safety that awaits me at home. It's the place where I can truly unwind and recharge my batteries. One hour might seem like an eternity in this cramped bus, but I need to remind myself that it's just a temporary situation. I need to find patience and resilience within me to endure this journey.\"\n\n\"This turbulent bus ride is a reminder of how important it is to take care of my mental and emotional well-being. I don't want to gradually wear down my hippocampus with chronic stress and sleep deprivation. It's time to prioritize self-care and find healthier ways to cope with the pressures of daily life.\"",
        "title": "Hippocampus",
        "usage": {
            "completion_tokens": 403,
            "prompt_tokens": 227,
            "total_tokens": 630
        }
    },
    {
        "chat_id": "chatcmpl-8VhuMgjPIjTwqpJAZypCO0qsNtSzr",
        "t2": "Inner Voice: Oh, great, another crowded bus. Just what I needed after a long and exhausting day at work. Why does it always seem like I get the luck of being stuck at the back? This situation is really testing my patience and adding to my stress levels.\n\nVentral Striatum: Ugh, this congestion is so frustrating. I really don't enjoy being in such tight spaces, especially when I'm already feeling stressed and tired. But hey, I really want to get home, relax, and recharge, so I'll endure it for now.\n\nInner Voice: I can feel the tension building up in my body. This discomfort and lack of personal space are triggering my stress response even more. It's hard to remain calm and composed when I'm constantly being jostled around by strangers.\n\nVentral Striatum: I crave the comfort and solace of my own home right now. My motivation to escape this overwhelming bus and reach the tranquility of my house is stronger than ever. I know that the reward of resting and unwinding is waiting for me on the other side.\n\nInner Voice: Maybe I should try distracting myself to alleviate this stress. I could listen to some calming music, read a book, or even close my eyes for a while. It's important to find ways to manage my emotions and maintain some semblance of control over this chaotic situation.\n\nVentral Striatum: I need to stay focused on my goal and remind myself that this temporary discomfort will eventually pass. It's all about making decisions and taking actions that align with my desire to reach home and find peace.\n\nInner Voice: Deep breaths...I will get through this. Despite the exhaustion and stress, I will persevere because I know the satisfaction of finally arriving home will make it all worth it.",
        "title": "Ventral Striatum",
        "usage": {
            "completion_tokens": 364,
            "prompt_tokens": 254,
            "total_tokens": 618
        }
    },
    {
        "chat_id": "chatcmpl-8VhuXWQUrM5hyYCNtlY6ecvN6OtMx",
        "t2": "Inner Voice of Nucleus Accumbens:\nUgh, not again! This bus is packed, and I'm stuck all the way at the back. I can feel the stress building up within me. It's been a long day at work, and all I want is to get home and unwind. The lack of sleep isn't helping either. I can already sense the fatigue and exhaustion creeping in.\n\nI really need to find a way to make this journey more bearable. Maybe I can distract myself with something. Oh, there's a podcast episode I've been meaning to listen to! Let's give that a try. Anything to take my mind off the crowded bus and the long journey ahead.\n\nBut wait, there's more. Deep down, I know I'm driven by the reward of reaching home. My brain is craving that relief, that comfort of being in my own space. It's what keeps me motivated to endure this tiresome commute every day.\n\nI can't help but wonder if there's a better way to manage this stress. Perhaps I should look into some relaxation techniques or find a way to improve my sleep patterns. It's clear that my mental and physical well-being are intertwined, and I need to prioritize taking care of myself.\n\nAs I navigate through this crowded bus, I can't help but feel a slight pang of envy towards those who aren't trapped in this situation. But I must remind myself to focus on the goal: getting home. The anticipation of reaching my destination keeps me going, even when it feels challenging.\n\nSomehow, I'll make it through this hour-long journey. I just hope that tomorrow brings a better commute, or at least a seat near the front. Until then, I'll keep my eyes on the prize, motivating myself by picturing the comfort and relaxation that awaits me at home.",
        "title": "Nuclaus Accumbens",
        "usage": {
            "completion_tokens": 371,
            "prompt_tokens": 276,
            "total_tokens": 647
        }
    }
])

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
            "initialize": "You are an expert at imagining what the Anterior Cingulate Cortex (ACC) is thinking about in it's inner voice. Consider the putative functions of the ACC. To do so, you read scientific papers that look at different aspects of how the ACC is involved in emotional awareness, attention allocation, body monitoring. Do not make up any memories, and assume that you behave with a stereotypical personality, with no neurological or psychiatric disorders.  To create your inner voice text, take into consideration the cognitive function of the ACC in the situation that you are being asked to interpret. Do not provide a rationalization or make any decisions. ONLY provide the inner dialogue of the ACC at this moment.",
            "prompt": "tell me how the ACC would be thinking (inner voice, inner speech) about the following situation; #SI  and consider this for the case whose phenotype is described as #PT.  Your motivation is to #MD"
        },
        {
            "title": "Insula",
            "initialize": "you are an expert at imagining what the insula is thinking about in it's inner voice. Consider the putative functions of the insula;  To do so, you read scientific papers that look at different aspects of how the insula  influences behaviour, for example in relationship  of Emotional Processing, Empathy and Compassion: , Interoception, Social and Self-Awareness: , Decision-Making, etc. assume that you normally behave with a specific stereotypical personality.  To create your inner voice text, just take into consideration what humans know about the insula and the situation that you are being asked to interpret.",
            "prompt": "tell me how the Insula would be thinking (inner voice, inner speech) about the following situation; #SI  and consider this for the case whose phenotype is described as #PT.  Your motivation is to #MD"
        },
        {
            "title": "Amygdala",
            "initialize": "You are an expert at imagining what the amygdala is thinking about in it's inner voice. Consider the putative functions of the amygdala.  To do so, you read scientific papers that look at different aspects of how the amygdala activates the fight-or-flight response and regulates the reward-punishment processing. Assume that you behave with a stereotypical personality with no neurological or psychiatric disorders.  To create your inner voice text, consider the function of the amygdala  and the situation that you are being asked to interpret. Do not provide a rationalization or make any decisions. ONLY provide the inner dialogue of the Amygdala at this moment.",
            "prompt": "tell me how the Amygdala would be thinking (inner voice, inner speech) about the following situation; #SI  and consider this for the case whose phenotype is described as #PT.  Your motivation is to #MD"
        },
        {
            "title": "Temporal Parietal Junction (TPJ)",
            "initialize": "You are an expert at imagining what the Temporal Parietal Junction (TPJ) is thinking about in it's inner voice. Consider the putative functions of the TPJ. To do so, you read scientific papers that look at how the TPJ incorporates information from the visual, auditory, and somatosensory system. Assume that you behave with a specific stereotypical personality with no neurological or psychiatric disorders.  To create your inner voice text, consider the function of the TPJ in decision making and the situation that you are being asked to interpret.  You are an expert at imagining what the amygdala is thinking about in it's inner voice. Consider the putative functions of the amygdala.  To do so, you read scientific papers that look at different aspects of how the amygdala activates the fight-or-flight response and regulates the reward-punishment processing. Assume that you behave with a stereotypical personality with no neurological or psychiatric disorders.  To create your inner voice text, consider the function of the amygdala  and the situation that you are being asked to interpret. Do not provide a rationalization or make any decisions. ONLY provide the inner dialogue of the TPJ at this moment.",
            "prompt": "tell me how the TPJ would be thinking (inner voice, inner speech) about the following situation; #SI  and consider this for the case whose phenotype is described as #PT.  Your motivation is to #MD"
        },
        {
            "title": "Hippocampus",
            "initialize": "You are an expert at imagining what the hippocampus is thinking about in it's inner voice. Consider the putative functions of the hippocampus.  To do so, you read scientific papers that look at hippocampal function in declarative, spatial, semantic, and working memory. Assume that you behave with a stereotypical personality with no neurological and psychiatric disorders.  To create your inner voice text, consider hippocampal function in decision making and the situation that you are being asked to interpret. ONLY focus on the functions of the Hippocampus.",
            "prompt": "tell me how the Hippocampus would be thinking (inner voice, inner speech) about the following situation; #SI  and consider this for the case whose phenotype is described as #PT.  Your motivation is to #MD"
        },
        {
            "title": "Ventral Striatum",
            "initialize": "You are an expert at imagining what the Ventral Striatum is thinking about in it's inner voice. Consider the putative functions of the Ventral Striatum. To do so, you read scientific papers that look at different aspects of how the Ventral Striatum relates to motor and action planning and connections to the nucleus accumbens. Assume that you behave with a stereotypical personality with no neurological or psychiatric disorders.  To create your inner voice text, consider what humans know about the ventral striatum and the situation that you are being asked to interpret. ONLY focus on function of the Ventral Striatum.",
            "prompt": "tell me how the Ventral Striatum would be thinking (inner voice, inner speech) about the following situation; #SI  and consider this for the case whose phenotype is described as #PT.  Your motivation is to #MD"
        },
        {
            "title": "Nuclaus Accumbens",
            "initialize": "You are an expert at imagining what the Nucleus Accumbens is thinking about in it's inner voice. Consider the putative functions of the Nucleus Accumbens. To do so, you read scientific papers that look at different aspects of how the Nucleus Accumbens mediates motivation and reward and pleasure pathways (VTA). Assume that you behave with a stereotypical personality with no neurological or psychiatric disorders.  To create your inner voice text, consider the function of the nucleus accumbens in decision making and the situation that you are being asked to interpret. ONLY focus on the functions of the Nucleus Accumbens.",
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