
import re
from datetime import datetime
import random

def chatbot():
    print("ChatBot: Hello! I'm a smarter chatbot. Ask me anything or type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

        # Greeting
        if re.search(r'\b(hi|hello|hey|good morning|good evening|good afternoon)\b', user_input):
            print("ChatBot: Hi there! How can I help you?")
        
        # Asking name
        elif re.search(r'\b(your name|who are you|what is your name)\b', user_input):
            print("ChatBot: I'm ChatBot 101, your friendly AI assistant.")

        # Asking how are you
        elif re.search(r'\b(how are you|how are things|how do you do)\b', user_input):
            print("ChatBot: I'm doing well, thank you! How about you?")

        # Asking what can you do
        elif re.search(r'\b(what can you do|help|services)\b', user_input):
            print("ChatBot: I can chat, tell you the time/date, tell jokes, and more!")

        # Asking time
        elif re.search(r'\b(time|current time|what time)\b', user_input):
            print("ChatBot: The current time is", datetime.now().strftime("%I:%M %p"))

        # Asking date
        elif re.search(r'\b(date|today|what day is it)\b', user_input):
            print("ChatBot: Today's date is", datetime.now().strftime("%A, %d %B %Y"))

        # Asking for a joke
        elif re.search(r'\b(joke|make me laugh|funny)\b', user_input):
            jokes = [
                "Why don’t scientists trust atoms? Because they make up everything!",
                "Why did the computer go to therapy? It had too many bytes.",
                "I told my computer I needed a break, and it said 'No problem, I’ll go to sleep.'"
            ]
            print("ChatBot:", random.choice(jokes))

        # Emotion support
        elif re.search(r'\b(sad|unhappy|depressed|upset)\b', user_input):
            print("ChatBot: I'm here for you. Sometimes talking helps. You're not alone.")
        
        elif re.search(r'\b(happy|excited|great)\b', user_input):
            print("ChatBot: That's wonderful to hear! Keep smiling 😊")

        # Thank you
        elif re.search(r'\b(thank you|thanks|thx)\b', user_input):
            print("ChatBot: You're welcome!")

        # Exit
        elif re.search(r'\b(bye|exit|quit|see you)\b', user_input):
            print("ChatBot: Goodbye! Take care!")
            break

        # Fallback response
        else:
            print("ChatBot: Hmm, I didn’t get that. Can you rephrase or ask something else?")

chatbot()
