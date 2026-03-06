from ollama import chat

response = chat(
    model="llama3:8b",
    messages=[
        {"role": "user", "content": "Explain what an AI Product Manager does in 3 lines."}
    ]
)

print(response["message"]["content"])
