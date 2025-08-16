def respond(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"
    elif "name" in user_input:
        return "I am your friendly chatbot."
    elif "how are you" in user_input:
        return "I'm doing well, thank you!"
    else:
        return "Sorry, I didn't understand that."

print("Chatbot: Hello! Type 'exit' to end the chat.")
while True:
    user_query = input("You: ")
    if user_query.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = respond(user_query)
    print("Chatbot:", response)
