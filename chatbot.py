import google.generativeai as ai

# API Key
API_KEY = 'Enter your API Key here'          # Enter your API Key here

# Configure the API
ai.configure(api_key=API_KEY)

# Create a new model
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

# Start the chat
while True:
    message = input("You: ")
    if message.lower() == "exit":
        print('Chatbot: Goodbye!')
        break
    response = chat.send_message(message)
    print("Chatbot:", response.text)