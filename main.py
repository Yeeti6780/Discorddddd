#https://replit.com/talk/learn/Hosting-discordpy-bots-with-replit/11008

import discord
import os
import keep_alive
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
#^ basic imports for other features of discord.py and python ^


client = discord.Client()

client =  commands.Bot(command_prefix = '!') #put your own prefix here

@client.event
async def on_ready():
    print("Bot Online")

@client.event
async def on_member_join(member):
    joinTestEmbed = discord.Embed(
        title = "New Member Alert! Wait, is there free Pizza?",
        color = 0x63cf5b,
        description = "A new user has joined this here server! Please welcome" + member.mention + "!"
    )
    print("testing")
    channel = client.get_channel(891433129305341984)
    await channel.send(embed=joinTestEmbed)

@client.command()
async def send(ctx, channel, *, content):
    channel = client.get_channel(int(channel))
    await channel.send(content)


@client.command()
async def dinner(ctx):
  await ctx.send("🔔🔔🔔🔔🔔🔔🔔🔔𝕋𝕚𝕞𝕖 𝕗𝕠𝕣 𝕕𝕚𝕟𝕟𝕖𝕣!🔔🔔🔔🔔🔔🔔🔔🔔🔔")



@client.command()
async def baby(ctx):
  await ctx.send("https://media.discordapp.net/attachments/846859972075454485/871120107806543902/image0.gif")


@client.command()
async def prefix(ctx, p):
  client = commands.Bot(command_prefix = p)


@client.command()
@commands.has_permissions(manage_channels=True)
async def nuke(ctx, channel):
    await ctx.send("Launching a Nuke...")
    time.sleep(0.5)
    await ctx.send("SAY YOUR PRAYERS " + channel + " WILL DIE IN")
    for x in range(5, 0, -1):
      await ctx.send(x)
      time.sleep(1)
    await ctx.channel.delete()



@client.command()
async def ping(ctx):
    await ctx.send("Pong!") #sximple command so that when you type "!ping" the bot will respond with "pong!"

@client.command()
async def debug(ctx):
    await ctx.send("https://media3.giphy.com/media/l7fdqmHQ1jCg2HzQlx/giphy.gif")

@client.command()
async def dad(ctx):
  await ctx.send("https://media4.giphy.com/media/tn1cGqW0xWyfm/giphy.gif")





@client.command(name = "join")
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


@client.command()
async def invite(ctx):
  await ctx.send("https://discord.com/oauth2/authorize?client_id=886056987022983208&permissions=8&scope=bot%20applications.commands")


@client.command()
async def rickroll(ctx):
  await ctx.send("https://media.giphy.com/media/10kABVanhwykJW/giphy.gif")




@client.command()
async def ban(ctx,*, member : discord.Member):
    try:
      await member.ban(reason=None)
      await ctx.send("Banned "+member.mention) 
      #simple kick command to demonstrate how to get and use member mentions
    except:
      await ctx.send("Bot does not have the ban members permission!")
    


@client.command() 
async def cat(ctx):
  await ctx.send("https://www.bing.com/th/id/OGC.6b1fe1e127f5ef1e52afc85016bcba5f?pid=1.7&rurl=https%3a%2f%2fres.cloudinary.com%2fjerrick%2fimage%2fupload%2ffl_progressive%2cq_auto%2cw_1024%2fteqcyxcn1hboqpuwifcq.gif&ehk=lP%2f3EuHGImelu%2bsArGFvHRxNmp%2btTPSF2Mu4ylNdxuQ%3d.gif")
  
@client.command()
async def kick(ctx,*, member : discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send("Kicked "+member.mention) #simple kick command to demonstrate how to get and use member mentions
    except:
        await ctx.send("Bot does not have the kick members permission!")

@client.command()
async def member(ctx, member : discord.Member):
    joinTestEmbed = discord.Embed(
        title = "Member: ",
        color = 0x63cf5b,
        description = "Hello " + member.mention + "!"
    ) 
    joinTestEmbed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=joinTestEmbed)
    

    
keep_alive.keep_alive()

#token in line 60
client.run("ODg2MDU2OTg3MDIyOTgzMjA4.YTwC3w.He9sPedAt1vKZb0TpbGKKHhIJJg")
#to keep your bot from shutting down use https://uptimerobot.com then create a https:// monitor and put the link to the website that appewars when you run this repl in the monitor and it will keep your bot alive by pinging the flask server
#enjoy!


