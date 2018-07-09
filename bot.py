import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.voice_client import VoiceClient
import asyncio
import time
import random
import datetime
import sqlite3

client = commands.Bot(command_prefix = "?")

chat_filter = ["NIG", "NIGGER", "NIGGA", "N1GG3R", "JEW", "JEWS"]
bypass_list = [" "]

@client.event
async def on_member_join(member):
  role = discord.utils.get(member.server.roles, name="Member")
  await client.add_roles(member, role)
  emb = (discord.Embed(description=None, colour=0x3DF270))
  welcome = client.get_channel("465682599008927754")
  emb.add_field(name="New Member", value="Welcome to Adrenaline Gaming, <@%s>! Have a great time here. If you need staff, feel free to use @staff and staff will be with you as soon as possible! " % (member.id), inline=False)
  await client.send_message(welcome, embed=emb)

@client.event
async def on_member_leave(member):
  emb = (discord.Embed(description=None, colour=0x3DF270))
  welcome = client.get_channel("465682599008927754")
  emb.add_field(name="Member Left", value="<@%s> left the server :frowning: " % (member.id), inline=False)
  await client.send_message(welcome, embed=emb)

@client.event
async def on_ready():
  print("Management || Bot is Online and ready.")
  await client.change_presence(game=discord.Game(name="AG BOT | ?cmds"))


@client.event
async def on_message(message):
    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "**HEY DONT SAY THAT!!**")
                except discord.errors.NotFound:
                    return
    if message.content.upper().startswith('?TICKET'):
                                                    args = message.content.split(" ")
                                                    chan = client.get_channel("466022799463415828")
                                                    emb = (discord.Embed(description=None, colour=0x3DF270))
                                                    emb.add_field(name="Bug/Support/Report Ticket by %s" % (message.author), value="%s" % (" ".join(args[1:])), inline=False)
                                                    emb2 = (discord.Embed(description=None, colour=0x3DF270))
                                                    emb2.add_field(name="Success!", value="I successfully created a ticket! You have reported the following: %s" % (" ".join(args[1:])), inline=False)
                                                    await client.send_message(message.channel, embed=emb2)
                                                    await client.send_message(chan, embed=emb)
    if message.content.upper().startswith('?INFORM'):
                                                    embed = discord.Embed(name="AG's info".format(message.server.name), description="Here's what I could find.", color=0x00ff00)
                                                    embed.set_author(name="Adrenaline Gaming")
                                                    embed.add_field(name="Name", value=message.server.name, inline=True)
                                                    embed.add_field(name="ID", value=message.server.id, inline=True)
                                                    embed.add_field(name="Roles", value=len(message.server.roles), inline=True)
                                                    embed.add_field(name="Members", value=len(message.server.members))
                                                    await client.send_message(message.channel, embed=embed)
    if message.content.upper().startswith('?CMDS'):
                                                  embed3 = (discord.Embed(description=None, colour=0x00ff00))
                                                  embed3.set_author(name="Server Commands")
                                                  embed3.add_field(name="?INFORM", value="", inline=False)
                                                  embed3.add_field(name="-gives you server information", value="", inline=False)
                                                  embed3.add_field(name="?8BALL", value="?LOL", inline=False)
                                                  embed3.add_field(name="-gives you a random message", value="Well...", inline=False)
                                                  await client.send_message(message.channel, embed=embed3)
    if message.content.upper().startswith('?ADMINCMDS'):
        if "465702997515829268" in [role.id for role in message.author.roles]:
                                                                             embed3 = (discord.Embed(description=None, colour=0x00ff00))
                                                                             embed3.set_author(name="Server Admin Commands")
                                                                             embed3.add_field(name="?NP(your announcement)", value="", inline=False)
                                                                             embed3.add_field(name="", value="", inline=False)
                                                                             embed3.add_field(name="?WARN @(WARNED PERSON) For (your words)", value="", inline=False)
                                                                             await client.send_message(message.channel, embed=embed3)
        else:
            await client.send_message(message.channel, "You Do Not Have Permission")
    if message.content == "cookies and milk":
        await client.send_message(message.channel, "Here's your cookie :cookie: . Almost forgot your milk :milk:!")
    if message.content.upper().startswith('?PING'):
        userID = message.author.id
        await client.send_message(message.channel, ":ping_pong: pong!")
    if message.content.upper().startswith('?WARN'):
        if "465702997515829268" in [role.id for role in message.author.roles]:
                                                                              args = message.content.split(" ")
                                                                              chan = client.get_channel("466021905820942356")
                                                                              embed = (discord.Embed(description=None, colour=0x00ff00))
                                                                              embed.add_field(name="Someone Has Been Warned By %s" % (message.author), value="%s" % (" ".join(args[1:])), inline=False)
                                                                              embed2 = (discord.Embed(description=None, colour=0x00ff00))
                                                                              embed2.add_field(name="You Have Successfully Warned Somebody!", value="You Have Warned Someone! You Have Warned Them For The Following: %s" % (" ".join(args[1:])), inline=False)
                                                                              await client.send_message(message.channel, embed=embed2)
                                                                              await client.send_message(chan, embed=embed)
        else:
            await client.send_message(message.channel, "You Do Not Have Permission")
    if message.content.upper().startswith('?8BALL'):
        userID = message.author.id
        randnum = random.randint(1,11)
        if randnum == 1:
            await client.send_message(message.channel,"<@%s> :8ball: It is likely. :8ball:" % (userID))
        if randnum == 2:
            await client.send_message(message.channel, "<@%s> :8ball: I am afraid not. :8ball:" % (userID))
        if randnum == 3:
            await client.send_message(message.channel, "<@%s> :8ball: I do not see it in the future. :8ball:" % (userID))
        if randnum == 4:
            await client.send_message(message.channel, "<@%s> :8ball: Very possible. :8ball:" % (userID))
        if randnum == 5:
            await client.send_message(message.channel, "<@%s> :8ball: There is a very bad chance. :8ball:" % (userID))
        if randnum == 6:
            await client.send_message(message.channel, "<@%s> :8ball: I see it in the future. :8ball:" % (userID))
        if randnum == 7:
            await client.send_message(message.channel, "<@%s> :8ball: There is an great chance. :8ball:" % (userID))
        if randnum == 8:
            await client.send_message(message.channel, "<@%s> :8ball: I do not see this happening. :8ball:" % (userID))
        if randnum == 9:
            await client.send_message(message.channel, "<@%s> :8ball: I see something positive. :8ball:" % (userID))
        if randnum == 10:
            await client.send_message(message.channel, "<@%s> :8ball: I don't see it. You may as well walk away. :8ball:" % (userID))
    if message.content.upper().startswith('?LOL'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> :joy: You Are A Loner :joy:" % (userID))
client.run("NDI5MzA2MTg5NDM2NjgyMjUw.DaHimw.qdy9hND0D4lTtkEZotjUB8w9GvU")
