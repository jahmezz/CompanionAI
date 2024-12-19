import openai

# Set up OpenAI API key
openai.api_key = "your-api-key-here"


def chatbot_response(prompt):
    try:
        # Make a request to OpenAI's API
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use GPT-3.5 or other models
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        # Extract the response text
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"


# Test the chatbot
if __name__ == "__main__":
    print("AI Chatbot Ready! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        response = chatbot_response(user_input)
        print(f"AI: {response}")
