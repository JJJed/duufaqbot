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

        @tasks.loop(seconds=60)  # repeat after every 60 seconds
        async def update():
            print("here")

            complete = rolloutapi_get.get_info()
            stats = complete.split("|")
            new_nitro = stats[0]
            new_non_nitro = stats[1]

            nitro = new_nitro
            non_nitro = new_non_nitro

            embed2 = discord.Embed()
            embed2.title = "Users With Access"
            embed2.type = "rich"
            embed2.description = "Users who should currently have access to the username update.\nAPI by: <@222073294419918848>\nBot by: <@270232807744208898>"
            embed2.url = "https://discordrollout.nekos.sh/"
            embed2.timestamp = datetime_get.get_timestamp()
            embed2.color = 0x5865f2
            embed2.add_field(name="Nitro: ", value=nitro, inline=False)
            embed2.add_field(name="Non-Nitro: ", value=non_nitro, inline=False)
            embed2.set_footer(text="Updates every 60 seconds.")

            await message.edit(embed=embed2)

        update.start()


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

keep_alive()

TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)
