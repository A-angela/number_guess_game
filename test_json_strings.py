import json
#
# # JSON string
# json_string = "{\"conversation_id\":\"123456\",\"timestamp\":\"2024-09-06T12:45:00Z\",\"participants\":{\"user\":{\"id\":\"user_001\",\"name\":\"John Doe\"},\"system\":{\"id\":\"system_001\",\"name\":\"ChatGPT\"}},\"messages\":[{\"sender\":\"user\",\"timestamp\":\"2024-09-06T12:45:10Z\",\"message\":\"Hello! I need some help with my account.\"},{\"sender\":\"system\",\"timestamp\":\"2024-09-06T12:45:15Z\",\"message\":\"Sure! What can I help you with?\"}]}"
#
# # Convert JSON string to JSON object (dictionary in Python)
# json_object = json.loads(json_string)
#
# # Accessing the data
# print(json_object["participants"]["user"]["name"])  # Output: John Doe


conversation = {
    "conversation_id": "123456",
    "timestamp": "2024-09-06T12:45:00Z",
    "participants": {
        "user": {
            "id": "user_001",
            "name": "John Doe"
        },
        "system": {
            "id": "system_001",
            "name": "ChatGPT"
        }
    },
    "messages": [
        {
            "sender": "user",
            "timestamp": "2024-09-06T12:45:10Z",
            "message": "Hello! I need some help with my account."
        },
        {
            "sender": "system",
            "timestamp": "2024-09-06T12:45:15Z",
            "message": "Sure! What can I help you with?"
        }
    ]
}


# Convert the conversation to a JSON string
json_string = json.dumps(conversation, indent=4)
print(json_string)

file_path = "/home/angela/Desktop/conversation.txt"


#Write the JSON string to the file
with open(file_path, "w") as file:
    file.write(json_string)

print(f"JSON string written to {file_path}")

with open(file_path, "r") as file:
    retrieved_json_string = file.read()

print(retrieved_json_string)

retrieved_conversation = json.loads(retrieved_json_string)

for message in retrieved_conversation["messages"]:
    sender = message["sender"]
    timestamp = message["timestamp"]
    text = message["message"]
    print(f"[{timestamp}] {sender} {text}")
