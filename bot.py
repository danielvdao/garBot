import discord
import asyncio
import properties
import giphypop
import urllib.request

g = giphypop.Giphy()
client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('!lucky'):
        searchResults = [x for x in g.search(message.content.split('!lucky ')[1])]
        if not searchResults:
            await client.send_message(message.channel, 'There is no image to be found')
        else:
            img = searchResults[0].media_url
            imgFile = urllib.request.urlopen(img)
            await client.send_file(message.channel, imgFile, filename='giphy.gif')
            await client.send_message('Powered by GIPHY')

client.run(properties.TOKEN)
