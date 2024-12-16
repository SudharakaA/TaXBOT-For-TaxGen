import nltk

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

# Verify that the punkt tokenizer is available
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import yaml

# Create chatbot instance
try:
    tax_bot = ChatBot(
        'TaxBot',
        storage_adapter='chatterbot.storage.MongoDatabaseAdapter',  # Use MongoDB adapter as an alternative
        database_uri='mongodb://localhost:27017/taxbot_db'  # Ensure MongoDB is running and accessible
    )
except Exception as e:
    print(f"Error creating ChatBot instance: {e}")
    print("Please ensure that the MongoDatabaseAdapter is correctly installed and available.")
    exit(1)

def read_corpus(file_path):
    with open(file_path, 'r') as data_file:
        return yaml.load(data_file, Loader=yaml.FullLoader)

# Train the chatbot with general English
trainer = ChatterBotCorpusTrainer(tax_bot)
try:
    trainer.train('chatterbot.corpus.english')
except Exception as e:
    print(f"Error during training: {e}")
    print("Please ensure that all required NLTK data is downloaded and available.")

# Train with custom tax-related responses
custom_trainer = ListTrainer(tax_bot)
try:
    custom_trainer.train([
        "What is the income tax rate?",
        "The income tax rate depends on your country and income bracket.",
        "When is the tax filing deadline?",
        "The tax filing deadline is usually April 15th in the USA.",
        "How do I file taxes?",
        "You can file taxes online using your country's official tax website."
    ])
except Exception as e:
    print(f"Error during custom training: {e}")

# Chat with the bot
print("Hi, I am TaxBot. Ask me anything about taxes!")
while True:
    query = input("You: ")
    if query.lower() in ['exit', 'quit']:
        print("TaxBot: Goodbye!")
        break
    response = tax_bot.get_response(query)
    print(f"TaxBot: {response}")
