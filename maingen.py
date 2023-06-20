import discord
import requests
import time
import re
import rolloutapi_get
import datetime_get
from discord.ext import commands, tasks
from webserver import keep_alive
import os

complete = rolloutapi_get.get_info()
stats = complete.split("|")
nitro = stats[0]
non_nitro = stats[1]


class MyClient(discord.Client):
    complete = rolloutapi_get.get_info()
    stats = complete.split("|")
    # nitro = stats[0]
    # non_nitro = stats[1]
    nitro = "a"
    non_nitro = "b"

    global message
    print("here")
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        channel = client.get_channel(1117969208597286993)

        embed = discord.Embed()
        embed.title = "Users With Access"
        embed.type = "rich"
        embed.description = "Users who should currently have access to the username update.\nAPI by: <@222073294419918848>\nBot by: <@270232807744208898>"
        embed.url = "https://discordrollout.nekos.sh/"
        embed.timestamp = datetime_get.get_timestamp()
        embed.color = 0x5865f2
        embed.add_field(name="Nitro: ", value=nitro, inline=False)
        embed.add_field(name="Non-Nitro: ", value=non_nitro, inline=False)

        embed.set_footer(text="Checks for updates every 60 seconds.")
        message = await channel.send(embed=embed)
        print("embed created")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

keep_alive()

TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)
