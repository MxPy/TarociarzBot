import discord
import responses
import os
from dotenv import load_dotenv


async def send_message(message, user_message, is_private):
    try:
        response =responses.handle_respons(message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
        
def run_discord_bot():
    load_dotenv()
    TOKEN = os.getenv("BOT_TOKEN")
    client = discord.Client(intents=discord.Intents.default())
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
        
    client.run(TOKEN)