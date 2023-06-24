import openai

openai.api_key = "###"

messages = [{"role": "system", "content": "Ti si developer asistent"}]

def CustomChatGPT(users_input):
    messages.append({"role": "user", "content": users_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply