import discord
import asyncio
import io
import random
import requests
import os


type = 1
client = discord.Client()

players = {}

@client.event
async def on_ready():
    print("Eingeloggt als BoredBot V0.1")
    print(client.user.name)
    print(client.user.id)
    print("------------")
    await client.change_presence(game=discord.Game(name="Game", url="twitch.tv/hendrigg", type=1))


@client.event
async def on_message(message):
    if message.content.startswith("!test"):
        await client.send_message(message.channel, "Test erfolgreich")

@client.event
async def on_message(message):
    if message.content.startswith('!join'):
        try:
            channel = message.author.voice.voice_channel
            await client.join_voice_channel(channel)
        except discord.errors.InvalidArgument:
            await client.send_message(message.channel, "Ich habe keinen Voicechannel gefunden.")
        except Exception as error:
            await client.send_message(message.channel, "Ein Error: ```{error}```".format(error=error))

    if message.content.startswith('!quit'):
        try:
            voice_client = client.voice_client_in(message.server)
            await voice_client.disconnect()
        except AttributeError:
            await client.send_message(message.channel, "-No Channel-")
        except Exception as Hugo:
            await client.send_message(message.channel, "Ein Error: ```{haus}```".format(haus=Hugo))

    if message.content.startswith('!play '):
        try:
            yt_url = message.content[6:]
            channel = message.author.voice.voice_channel
            voice = await client.join_voice_channel(channel)
            player = await voice.create_ytdl_player(yt_url)
            players[message.server.id] = player
            player.start()
        except:
            await client.send_message(message.channel, "Error.")

    if message.content.startswith('!pause'):
        try:
            players[message.server.id].pause()
        except:
            pass
    if message.content.startswith('!resume'):
        try:
            players[message.server.id].resume()
        except:
            pass







client.run(str(os.environ.get('BOT_TOKEN')))
