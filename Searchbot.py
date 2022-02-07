import discord
from discord.ext import commands
import json
import ImageSearch
with open('setting.json',mode='r',encoding='utf8') as discord_file:
    discord_data = json.load(discord_file)

bot = discord.Client()
@bot.event
async def on_ready():
    pass

@bot.event
async def on_message(message):
    if 'Pikachu' in message.content:
        Content_url = ImageSearch.search()
        await message.channel.send(f'You just mentioned Pikachu!  \n {Content_url}' )

bot.run(discord_data['bot_token'])