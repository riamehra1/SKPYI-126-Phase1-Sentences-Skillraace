import nltk
import random
import string

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')

from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Sample corpus for the chatbot
corpus = """Hello! How can I help you today? I am a simple chatbot created to assist you with basic queries. 
You can ask me about various topics and I will do my best to provide useful information. 
Feel free to ask me anything!"""

# Tokenization and Lemmatization
lemmatizer = WordNetLemmatizer()
corpus_tokens = nltk.word_tokenize(corpus.lower())

# Lemmatize tokens
def LemTokens(tokens):
    return [lemmatizer.lemmatize(token) for token in tokens]

# Normalize text
def Normalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(str.maketrans('', '', string.punctuation))))

# Greeting responses
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
GREETING_RESPONSES = ["hello", "hi", "greetings", "hey", "hi there"]

def greet(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Generate response
def response(user_response):
    user_response = user_response.lower()
    corpus_tokens.extend(Normalize(user_response))
    response = ''
    TfidfVec = nltk.TfidfVectorizer(tokenizer=Normalize, stop_words='english')
    tfidf = TfidfVec.fit_transform([corpus] + [user_response])
    vals = (tfidf * tfidf.T).A[0]
    idx = vals.argsort()[-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    if req_tfidf == 0:
        response = response + "I am sorry! I don't understand you."
    else:
        response = response + corpus.split('\n')[idx]
    return response

# Main chatbot loop
flag = True
print("Chatbot: Hello! How can I help you? Type 'bye' to exit.")

while flag:
    user_response = input("You: ").lower()
    if user_response != 'bye':
        if user_response in ('thanks', 'thank you'):
            flag = False
            print("Chatbot: You're welcome!")
        else:
            if greet(user_response) is not None:
                print("Chatbot: " + greet(user_response))
            else:
                print("Chatbot: " + response(user_response))
    else:
        flag = False
        print("Chatbot: Goodbye! Have a nice day.")
