from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
chatbot = ChatBot('ZomatoBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot using the English corpus
trainer.train('chatterbot.corpus.english')

# Function to get the chatbot's response
def get_chatbot_response(user_input):
    if 'hours of operation' in user_input.lower():
        return 'Our restaurant is open from 9:00 AM to 10:00 PM every day.'

    if 'status of my order' in user_input.lower():
        return 'Please provide your order ID, and I will check the status for you.'

    if 'most popular dish' in user_input.lower():
        return 'Our most popular dish is our signature Zesty Zomato Special.'

    # Add more rules and responses for other common questions

    response = chatbot.get_response(user_input)
    return str(response)

