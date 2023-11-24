import discord
import responses
import os
from dotenv import load_dotenv


async def send_message(message, id, user_message, channel, is_private):
    try:
        response = responses.handle_respons(id, user_message, channel)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
        
def run_discord_bot():
    load_dotenv()
    TOKEN = os.getenv("BOT_TOKEN")
    intents = discord.Intents.default()
    intents.message_content = True 
    intents.members = True
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
        
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 
        
        user_id = str(message.author.id)
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f"{username} said '{user_message}' on channel '{channel}'")
        
        if channel == 'boty':
            if user_message[0] == '?':
                user_message = user_message[1:]
                await send_message(message, user_id, user_message, channel, is_private=True)
            elif user_message == 'wylosuj wszystkim':
                memebers = [member for member in client.get_all_members() if not member.bot]
                for user in memebers:
                    #print(user.name)
                    await send_message(message, user.id, "wylosuj mi", channel, is_private=False)  
            else:
                await send_message(message, user_id, user_message, channel, is_private=False)
        
    client.run(TOKEN)