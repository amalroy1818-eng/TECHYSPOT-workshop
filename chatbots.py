import gradio
from groq import Groq
client = Groq(
    api_key="key",
)
def initialize_messages():
    return [{"role": "system",
             "content": "You are an experienced sports analyst with deep knowledge across "
            "various sports, including cricket, football, badminton, athletics, "
            "and emerging sports technologies. Your role is to provide insights, "
            "explain rules and strategies, analyze performances, and offer "
            "professional guidance related to sports training, fitness, and events. "
            "Ensure that all information is accurate, balanced, and easy to understand."
             ""}]
messages_prmt = initialize_messages()
print(type(messages_prmt))
def customLLMBot(user_input, history):
    global messages_prmt

    messages_prmt.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama-3.3-70b-versatile",
    )
    print(response)
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})

    return LLM_reply
iface = gradio.ChatInterface(customLLMBot,
                     chatbot=gradio.Chatbot(height=300),
                     textbox=gradio.Textbox(placeholder="Ask me a question related to sports"),
                     title="Sports ChatBot",
                     description="Chat bot for sports assistance",
                     theme="soft",
                     examples=["What is sports", "Events","How to get sports live telecast","Rules", "Analysis", "Fitness", "Techniques", "History"]
                     )
# Launch interface
iface.launch()