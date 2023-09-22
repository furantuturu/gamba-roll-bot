import os
from dotenv import load_dotenv
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

import discord
import response

async def send_message(message, user_message, is_private):
    try:
        responses = response.get_roll_response(user_message)
        await message.author.send(responses) if is_private else await message.channel.send(responses)
    except Exception as err:
        print(err)

def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f"{client.user} is now online")
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author) # ex: haemoffy#6965
        user_message = str(message.content) # ex: "wysi"
        channel = str(message.channel) # ex: #bro-code-dsa

        # debugging
        print(f"{username} said: \"{user_message}\" ({channel})")
        
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message=message, user_message=user_message, is_private=True)
        else:
            await send_message(message=message, user_message=user_message, is_private=False)
    
    client.run(DISCORD_TOKEN)

