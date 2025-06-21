from transformers import pipeline

chatbot = pipeline("text-generation", model="microsoft/DialoGPT-small")

print("Welcome to Hugging Face Chatbot! Type 'exit' or 'quit' to stop.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye! 👋")
        break

    response = chatbot(user_input, max_length=100, num_return_sequences=1, pad_token_id=50256)
    reply = response[0]["generated_text"].replace(user_input, "")
    print(f"Chatbot:{reply}")
