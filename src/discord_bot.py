from nltk import word_tokenize
from dotenv import load_dotenv
import discord
import bentoml
import itertools
import os

# Create a DISCORD_TOKEN (https://discordpy.readthedocs.io/en/latest/discord.html#discord-intro)
# Store in a .env file with the following structure
"""
# .env
DISCORD_TOKEN={your-discord-token}
DISCORD_GUILD={your-guild-name}
"""
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
# Change this path with your PyTorchModel's latest path
LOAD_PATH = "/home/parthparikh/bentoml/repository/PyTorchModel/20200928112210_3AE3EC"

class Guild_Members:
    def __init__(self):
        self.ids = list()
        self.bento_service = None

guild_obj = Guild_Members()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    
    guild_obj.ids = guild.members
    guild_obj.bento_service = bentoml.load(LOAD_PATH)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(message.content)
    if message.content.startswith('$tag'):
        content = message.content.replace("$tag", "")
        prediction = guild_obj.bento_service.predict([{"sentence": content}])

        tokens = prediction[0].split(",")
        all_words = [[word_tokenize(w), ' '] for w in content.split()]
        all_words = list(itertools.chain(*list(itertools.chain(*all_words))))
        
        member_names = {(member.nick.lower()): member.id for member in guild_obj.ids if member.nick is not None}
        for i in range(len(all_words)):
            if all_words[i].lower() in list(member_names.keys()):
                print("Here!")
                all_words[i] = "<@"+str(member_names[all_words[i].lower()])+">"

        # For Debugging
        # print(prediction, member_names)
        # print(all_words)

        await message.channel.send("".join(all_words))

client.run(TOKEN)