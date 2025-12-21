def get_response(message):
    message = message.lower()

    rules = {
        "hi": "Hello! How can I help you?",
        "hello": "Hi there!",
        "how are you": "I'm doing great!",
        "your name": "I'm a rule-based chatbot.",
        "bye": "Goodbye! Have a nice day!"
    }

    for key in rules:
        if key in message:
            return rules[key]

    return "Sorry, I didn't understand that."
