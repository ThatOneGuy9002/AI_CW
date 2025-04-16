def main():
    print("Hello! How can I help you today?")
    
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break

        print(f"Chatbot: You said '{user_input}'")  #echoing for now

if __name__ == "__main__":
    main()
