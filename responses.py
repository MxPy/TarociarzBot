import tarot

def handle_respons(id, message, channel) -> str:
    p_message = message.lower()
    
    if p_message == "hello":
        return "hi"
    
    if p_message == "!help":
        return "This is help message for tarociarz bot"
    
    if p_message =="wylosuj mi":
        card = tarot.get_cards()
        return f"<@{id}> Karta dla ciebie to **{card['title']}**\n{card['description']}"
    