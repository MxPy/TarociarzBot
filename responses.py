def handle_respons(id, message, card) -> str:
    p_message = message.lower()
    
    if p_message == "hello":
        return "hi"
    
    if p_message == "!help":
        return "This is help message for tarociarz bot"
    
    if p_message =="wylosuj mi":
        return f"<@{id}> Karta dla ciebie to **{card['title']}**\n**{card['description']}**"
    
    if "wylosuj dla" in p_message:
        p_message = p_message.split()
        if(p_message[2]):
            return f"<@{id}> Karta dla **{p_message[2]}** to **{card['title']}**\n**{card['description']}**"
    
    