from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

# Create chatbot instance
tax_bot = ChatBot('TaxBot')

# Train the chatbot with general English
trainer = ChatterBotCorpusTrainer(tax_bot)
trainer.train('chatterbot.corpus.english')

# Train with custom tax-related responses
custom_trainer = ListTrainer(tax_bot)
custom_trainer.train([
    "What is the income tax rate?",
    "The income tax rate depends on your country and income bracket.",
    "When is the tax filing deadline?",
    "The tax filing deadline is usually April 15th in the USA.",
    "How do I file taxes?",
    "You can file taxes online using your country's official tax website."
])

# Chat with the bot
print("Hi, I am TaxBot. Ask me anything about taxes!")
while True:
    query = input("You: ")
    if query.lower() in ['exit', 'quit']:
        print("TaxBot: Goodbye!")
        break
    response = tax_bot.get_response(query)
    print(f"TaxBot: {response}")
