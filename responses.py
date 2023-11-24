def handle_respons(message) -> str:
    p_message = message.lower()
    
    if p_message == "hello":
        return "hi"
    
    if p_message == "!help":
        return "This is help message for tarociarz bot"
    