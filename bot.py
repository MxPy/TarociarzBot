import discord
import responses
import os

async def send_message(message, user_message, is_private):
    try:
        response =responses.handle_respons(message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
        
def run_discord_bot():
    TOKEN = os.environ["BOT_KEY"]