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
        searchResults = g.search(message.content.split('!lucky ')[1])
        if not imgSearch:
            await client.send_message(message.channel, 'There is no image to be found')
        else:
            img = searchResults[0].media_url
            imgFile = urllib.request.urlopen(img)
            await client.send_file(message.channel, imgFile, filename='giphy.gif')

client.run(properties.TOKEN)
