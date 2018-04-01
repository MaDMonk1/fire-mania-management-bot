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

@client.event
async def on_member_join(member):
  role = discord.utils.get(member.server.roles, name="Member")
  await client.add_roles(member, role)
  emb = (discord.Embed(description=None, colour=0x3DF270))
  welcome = client.get_channel("417043672144543765")
  emb.add_field(name="New Member", value="Welcome to SASRP, <@%s>! Have a great time with your RP. Before going anywhere, feel free to check out the useful links text channel! If you need staff, feel free to use @staff and staff will be with you as soon as possible! Also say '?INFORM' to get started! " % (member.id), inline=False)
  await client.send_message(welcome, embed=emb)

@client.event
async def on_ready():
  print("Management || Bot is Online and ready.")
  await client.change_presence(game=discord.Game(name="SASRP BOT | ?cmds"))


@client.event
async def on_message(message):
    if message.content.upper().startswith('?TICKET'):
                                                    args = message.content.split(" ")
                                                    chan = client.get_channel("428731112559476756")
                                                    emb = (discord.Embed(description=None, colour=0x3DF270))
                                                    emb.add_field(name="Bug Report Ticket by %s" % (message.author), value="%s" % (" ".join(args[1:])), inline=False)
                                                    emb2 = (discord.Embed(description=None, colour=0x3DF270))
                                                    emb2.add_field(name="Success!", value="I successfully created a bug report ticket! You have reported the following: %s" % (" ".join(args[1:])), inline=False)
                                                    await client.send_message(message.channel, embed=emb2)
                                                    await client.send_message(chan, embed=emb)
    if message.content.upper().startswith('?INFORM'):
                                                    embed = discord.Embed(name="SASRP's info".format(message.server.name), description="Here's what I could find.", color=0x00ff00)
                                                    embed.set_author(name="SASRP")
                                                    embed.add_field(name="Name", value=message.server.name, inline=True)
                                                    embed.add_field(name="ID", value=message.server.id, inline=True)
                                                    embed.add_field(name="Roles", value=len(message.server.roles), inline=True)
                                                    embed.add_field(name="Members", value=len(message.server.members))
                                                    await client.send_message(message.channel, embed=embed)
    if message.content.upper().startswith('?LINKS'):
                                                    await client.send_message(message.channel, "Website-http://www.sas-rp.com/ , CAD-http://cad.sas-rp.com/home")
    if message.content.upper().startswith('?NP'):
                                                  args = message.content.split(" ")
                                                  chan = client.get_channel("421382437910872084")
                                                  embed = (discord.Embed(description=None, colour=0x00ff00))
                                                  embed.add_field(name="Admin Announcement By %s" % (message.author), value="%s" % (" ".join(args[1:])), inline=False)
                                                  embed2 = (discord.Embed(description=None, colour=0x00ff00))
                                                  embed2.add_field(name="You Have Successfully Announced Your Words!", value="You Have Made An Announcement! You Have Announced The Following: %s" % (" ".join(args[1:])), inline=False)
                                                  await client.send_message(message.channel, embed=embed2)
                                                  await client.send_message(chan, embed=embed)
    if message.content.upper().startswith('?MPS'):
                                                 args = message.content.split(" ")
                                                 chan = client.get_channel("417033016930467873")
                                                 embed = (discord.Embed(description=None, colour=0x00ff00))
                                                 embed.add_field(name="More Players Announcement By %s" % (message.author), value="%s" % (" ".join(args[1:])), inline=False)
                                                 embed2 = (discord.Embed(description=None, colour=0x00ff00))
                                                 embed2.add_field(name="You Have Successfully Announced Your MPS!", value="You Have Made A MPS Announcement! You Have Announced The Following MPS: %s" % (" ".join(args[1:])), inline=False)
                                                 await client.send_message(message.channel, embed=embed2)
                                                 await client.send_message(chan, embed=embed)

    if message.content.upper().startswith('?CMDS'):
                                                  embed3 = (discord.Embed(description=None, colour=0x00ff00))
                                                  embed3.set_author(name="Server Commands")
                                                  embed3.add_field(name="?INFORM", value="?LINKS", inline=True)
                                                  embed3.add_field(name="-gives you server information", value="-gives you links to the website and the CAD", inline=True)
                                                  embed3.add_field(name="N/A", value="N/A", inline=True)
                                                  embed3.add_field(name="N/A", value="N/A", inline=True)
                                                  await client.send_message(message.channel, embed=embed3)
    if message.content.upper().startswith('?ADMINCMDS'):
                                                  embed3 = (discord.Embed(description=None, colour=0x00ff00))
                                                  embed3.set_author(name="Server Admin Commands")
                                                  embed3.add_field(name="?NP(your announcement)", value="?MPS(ask for more players)", inline=True)
                                                  embed3.add_field(name="N/A", value="N/A", inline=True)
                                                  embed3.add_field(name="?WARN @(WARNED PERSON) For (your words)", value="N/A", inline=True)
                                                  await client.send_message(message.channel, embed=embed3)
    if message.content == "cookies and milk":
        await client.send_message(message.channel, "Here's your cookie :cookie: . Almost forgot your milk :milk:!")
    if message.content.upper().startswith('?PING'):
        userID = message.author.id
        await client.send_message(message.channel, ":ping_pong: pong!")
    if message.content.upper().startswith('?WARN'):
        if "417059335634681856" in [role.id for role in message.author.roles]:
                                                                              args = message.content.split(" ")
                                                                              chan = client.get_channel("429808605236035595")
                                                                              embed = (discord.Embed(description=None, colour=0x00ff00))
                                                                              embed.add_field(name="Someone Has Been Warned By %s" % (message.author), value="%s" % (" ".join(args[1:])), inline=False)
                                                                              embed2 = (discord.Embed(description=None, colour=0x00ff00))
                                                                              embed2.add_field(name="You Have Successfully Warned Somebody!", value="You Have Warned Someone! You Have Warned Them For The Following: %s" % (" ".join(args[1:])), inline=False)
                                                                              await client.send_message(message.channel, embed=embed2)
                                                                              await client.send_message(chan, embed=embed)
        else:
            await client.send_message(message.channel, "You Do Not Have Permission")
            
client.run("NDI5MzA2MTg5NDM2NjgyMjUw.DaHimw.qdy9hND0D4lTtkEZotjUB8w9GvU")
