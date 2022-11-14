# Hushhy#8022 on discord.


import discord
import os
import requests
from webserver import keep_alive

intents = discord.Intents().all()

client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))





@client.event
async def on_message(message):
    timess = message.content[10:20] 
    if message.author == client.user:
       return

    autor = message.author.mention
    def get_results(time_inp):
      total = " "
      response = requests.get("https://api.howrare.is/v0.1/drops").json()
      time_keys = response['result']["data"].keys()
      if time_inp in time_keys:
        j = response['result']["data"][time_inp]
        for i in j:
          mint_time = i["time"]
          twitter_acc = i["twitter"]
          price = i['price']
          name = i['name']
          mints = (f" NAME : {name} \n MINT TIME : {mint_time} \n TWITTER: {twitter_acc} \n PRICE : {price} \n \n")
          total += mints
        return  f"{autor} \n \n SOL NFT COLLECTIONS ON {time_inp} \n \n" + total
      else:
        return "Invalid format"
    if message.content.startswith('$projects'):
        await message.channel.send(get_results(timess))
      
  
keep_alive()
client.run(os.getenv('my_token'))
