import discord
import asyncio
import properties
import giphypop
import urllib.request

g = giphypop.Giphy()
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!lucky'):
        counter = 0
        imgSearch = message.content.split('!lucky ')
        img = [x for x in g.search(imgSearch[1])][0].media_url
        imgFile = urllib.request.urlopen(img)
        ##### todo handle the case where there is no media url or image could not be found
        # await client.send_message(message.channel, [x for x in g.search(imgSearch[1])][0].url)
        await client.send_file(message.channel, imgFile, filename='giphy.gif')

client.run(properties.TOKEN)
