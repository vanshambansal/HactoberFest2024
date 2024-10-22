def chatbot():
    print("ChatBot: Hello! I am a simple chatbot. How can I assist you today?")
    
    while True:
        # Take user input
        user_input = input("You: ").lower()
        
        # Greeting responses
        if "hello" in user_input or "hi" in user_input:
            print("ChatBot: Hi there! How can I help?")
        
        # How are you response
        elif "how are you" in user_input:
            print("ChatBot: I'm just a bunch of code, but I'm doing great! How about you?")
        
        # Exit condition
        elif "bye" in user_input or "exit" in user_input:
            print("ChatBot: Goodbye! Have a nice day!")
            break
        
        # Responding to questions about weather
        elif "weather" in user_input:
            print("ChatBot: Sorry, I can't check the weather right now, but you can ask me something else!")
        
        # Responding to unknown inputs
        else:
            print("ChatBot: I'm sorry, I don't understand that. Could you please ask something else?")
            
# Run the chatbot
chatbot()
