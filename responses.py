def handle_respons(id, message, card) -> str:
    p_message = message.lower()
    
    if p_message == "hello":
        return "hi"
    
    if p_message == "help":
        return "This is a **Tarociarz** bot running on a **taroty** channel\n\nuse **!Tarociarz <command>** to call it on any channel\n**wyslosuj mi** to draw a card for yourself\n**wyslosuj dla <someone>** to draw a card for someone\n**wylosuj wszystkim** to draw a card for everyone"
    
    if p_message =="wylosuj mi":
        return f"<@{id}> Karta dla ciebie to **{card['title']}**\n**{card['description']}**"
    
    if "wylosuj dla" in p_message:
        p_message = p_message.split()
        if(p_message[2]):
            return f"Karta dla **{p_message[2]}** to **{card['title']}**\n**{card['description']}**"
    
    