import numpy as np
import speech_recognition as sr
from gtts import gTTS
import os
import datetime
import transformers
from dotenv import load_dotenv
# import time
from pydub import AudioSegment
from pydub.playback import play
import logging
import wikipediaapi
import requests

# Load environment variables
load_dotenv()


logging.getLogger("transformers").setLevel(logging.ERROR)

# Suppress TensorFlow logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # 0 = all logs, 1 = filter out INFO logs, 2 = filter out WARNING logs, 3 = filter out INFO & WARNING logs

import tensorflow as tf
tf.get_logger().setLevel('ERROR')

# Set the cache directory for transformers
os.environ['TF_HOME'] = './transformers_cache'

class ChatBot():
    def __init__(self, name):
        print(f"--------Starting UP {name}--------")
        self.name = name
        self.text = ""
        self.nlp = None
        self.load_model()
        self.wiki_wiki = wikipediaapi.Wikipedia(user_agent=f'Friday/0.4 ({os.getenv("USER_EMAIL")})')
        self.api_key = os.getenv('GOOGLE_API_KEY')
        self.cse_id = os.getenv('GOOGLE_CSE_ID')


    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("Listening...")
            audio = recognizer.listen(mic)
        try:
            self.text = recognizer.recognize_google(audio)
            print(f"me ---> {self.text}")
        except sr.UnknownValueError:
            print("me ---> Sorry, I did not understand that.")
            self.text = "ERROR"
        except sr.RequestError as e:
            print(f"me ---> Could not request results; {e}")
            self.text = "ERROR"

    def wake_up(self, text):
        return self.name.lower() in text.lower()

    @staticmethod
    def text_to_speech(text):
        if not text.strip():
            print("No text provided for text-to-speech.")
            return

        print("AI --> ", text)
        speaker = gTTS(text=text, lang="en", slow=False)
        speaker.save("res.mp3")
        sound = AudioSegment.from_file("res.mp3")
        play(sound)
        os.remove("res.mp3")

    def action_time(self):
        return datetime.datetime.now().time().strftime('%H:%M')
    
    def fetch_wikipedia_summary(self, query):
        page = self.wiki_wiki.page(query)
        if page.exists():
            return page.summary[:500]  # Limit the summary to 500 characters
        else:
            return "Sorry, I couldn't find information on that topic."
    
    def fetch_google_summary(self, query, num_results=5):
        url = f"https://www.googleapis.com/customsearch/v1?key={self.api_key}&cx={self.cse_id}&q={query}"
        response = requests.get(url)
        data = response.json()
        if "items" in data and len(data["items"]) > 0:
            return data["items"][0]["snippet"]
        else:
            return "Sorry, I couldn't find information on that topic."

        
    def respond(self, text):
        if "tell me about" in text.lower():
            parts = text.lower().split("tell me about")
            if len(parts) > 1:
                topic = parts[1].strip()
                return self.fetch_wikipedia_summary(topic)
            else:
                return "Sorry, I didn't understand the topic you want to know about."
        elif "search google for" in text.lower():
            parts = text.lower().split("search google for")
            if len(parts) > 1:
                topic = parts[-1].strip()
                return ai.fetch_google_summary(topic) 
            else:
                return "Sorry, I didn't understand the topic you want to search for."
        elif "time" in text:
            return self.action_time()
        elif any(i in text for i in ["thank", "thanks"]):
            return np.random.choice(
                ["you're welcome!", "anytime!", "no problem!", "cool!", "I'm here if you need me!", "peace out!"]
            )
        elif any(i in text for i in ["exit", "close"]):
            return np.random.choice(["Tata", "Have a good day", "Bye", "Goodbye", "Hope to meet soon", "peace out!"])
        else:
            chat = self.nlp(transformers.Conversation(text), pad_token_id=tokenizer.eos_token_id)
            return chat.generated_responses[-1].strip()


    
    def load_model(self):
        print("Loading model...")
        tokenizer = transformers.AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium", padding_side='left')
        model = transformers.AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
        self.nlp = transformers.pipeline("conversational", model=model, tokenizer=tokenizer)
        os.environ["TOKENIZERS_PARALLELISM"] = "true"
        print("Model loaded.")


if __name__ == '__main__':
    ai = ChatBot('Fawks')
    tokenizer = transformers.AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium", padding_side="left")

    ex = True
    while ex:
        ai.speech_to_text()
        res = ""
        if ai.text == "ERROR":
            res = "Sorry, come again?"
        elif ai.wake_up(ai.text):
            res = "Hello, I am Fawks the AI, what can I do for you?"
        elif "time" in ai.text:
            res = ai.action_time()
        elif any(i in ai.text for i in ["thank", "thanks"]):
            res = np.random.choice(
                ["you're welcome!", "anytime!", "no problem!", "cool!", "I'm here if you need me!", "peace out!"]
            )
        elif any(i in ai.text for i in ["exit", "close"]):
            res = np.random.choice(["Tata", "Have a good day", "Bye", "Goodbye", "Hope to meet soon", "peace out!"])
            ex = False
        elif any(i in ai.text for i in ["google", "wikipedia", "tell me about", "Google"]):
            print("Searching...")
            res = ai.respond(ai.text)
            ai.text_to_speech(res) 
            continue
        else:
            print("Using DialogPT model...")
            chat = ai.nlp(transformers.Conversation(ai.text), pad_token_id=tokenizer.eos_token_id)
            res = chat.generated_responses[-1].strip()
            print("DialogPT response:", res)

        print("Response:", res)
        ai.text_to_speech(res)

    
    print(f"--------Closing DOWN Friday--------")
