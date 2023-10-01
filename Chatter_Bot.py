from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import os

# Create a ChatBot instance
chatbot = ChatBot('MyChatBot')

# Create a new trainer for the chatbot
corpus_trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
corpus_trainer.train('chatterbot.corpus.english')

# Create a list trainer to add custom responses
list_trainer = ListTrainer(chatbot)

# Define custom responses
custom_responses = [
    "Hi there!",
    "Hello!",
    "How can I assist you today?",
    "What's on your mind?",
    "I'm just a bot, but I'm here to help!",
    "Tell me more about that...",
]

# Train the chatbot with custom responses
list_trainer.train(custom_responses)

# Define a function to interact with the chatbot
def chat_with_bot():
    print("Hello! I'm your chatbot. You can start a conversation with me by typing a message.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print("Chatbot:", response)

# Start the chat with the bot
chat_with_bot()
