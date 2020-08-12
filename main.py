import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, dns.name, asyncio, functools, logging

import discord
import time
from discord.ext import commands
from colorama import Fore, init 
import requests
import os 
import base64
import random
 
# Dont just skid it, gimme some credits, thank you - Janky 
 # Dont just skid it, gimme some credits, thank you - Janky
  # Dont just skid it, gimme some credits, thank you - Janky
   # Dont just skid it, gimme some credits, thank you - Janky
    # Dont just skid it, gimme some credits, thank you - Janky
     # Dont just skid it, gimme some credits, thank you - Janky 
      # Dont just skid it, gimme some credits, thank you - Janky
       # Dont just skid it, gimme some credits, thank you - Janky
        # Dont just skid it, gimme some credits, thank you - Janky
         # Dont just skid it, gimme some credits, thank you - Janky
          # Dont just skid it, gimme some credits, thank you - Janky
           # Dont just skid it, gimme some credits, thank you - Janky
            # Dont just skid it, gimme some credits, thank you - Janky

prefix = "."

JANKY = commands.Bot(command_prefix=prefix, self_bot=True)
JANKY.remove_command('help')

@JANKY.event
async def on_connect():
    print(f'''{Fore.RED}

 ▄▄▄██▀▀▀▄▄▄       ███▄    █  ██ ▄█▀▓██   ██▓
   ▒██  ▒████▄     ██ ▀█   █  ██▄█▒  ▒██  ██▒
   ░██  ▒██  ▀█▄  ▓██  ▀█ ██▒▓███▄░   ▒██ ██░
▓██▄██▓ ░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██ █▄   ░ ▐██▓░
 ▓███▒   ▓█   ▓██▒▒██░   ▓██░▒██▒ █▄  ░ ██▒▓░
 ▒▓▒▒░   ▒▒   ▓▒█░░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒   ██▒▒▒ 
 ▒ ░▒░    ▒   ▒▒ ░░ ░░   ░ ▒░░ ░▒ ▒░ ▓██ ░▒░ 
 ░ ░ ░    ░   ▒      ░   ░ ░ ░ ░░ ░  ▒ ▒ ░░  
 ░   ░        ░  ░         ░ ░  ░    ░ ░     
                                     ░ ░     
                                                                                           
                                                                                                                                     
                                                                       
            {Fore.WHITE}[+] MADE BY JANKY
              {Fore.WHITE}_________________    
                {Fore.WHITE}
                {Fore.WHITE}[-]    J
                  {Fore.WHITE}[-]   A
                    {Fore.WHITE}[-]  N
                     {Fore.WHITE}[-]  K
                       {Fore.WHITE}[-] Y
                                                                                               
                                                                               ''')
@JANKY.command()
async def help(ctx):
    embed = discord.Embed(title="𝙓𝙗𝙤𝙭 𝙎𝙚𝙡𝙛𝙗𝙤𝙩", color= discord.Color(random.randint(0x2fff00, 0x2fff00)))
    embed.add_field(name="`Nigger`", value="**SENDS KID SAYING NIGGER.**\n", inline=False)
    embed.add_field(name="`Minecraft`", value="**GET OUT MY ROOM IM PLAYING MINECRAFT.**\n", inline=False)  
    embed.add_field(name="`Gay`", value="**SENDS KID BEING SUS.**\n", inline=False)
    embed.add_field(name="`Rage`", value="**SENDS KID RAGING.**\n", inline=False)
    embed.add_field(name="`Scam`", value="**SCAMMER GETS SCAMMED.**\n", inline=False)
    embed.add_field(name="`Scream`", value="**SENDS E-SEX PARAGRAPH.**\n", inline=False)
    embed.add_field(name="`Fight`", value="**SENDS KID FIGHTING WITH PARRENTS.**\n", inline=False)
    embed.add_field(name='**MADE BY JANKY**', value="`JANKY MADE THIS (SKIDS K)`", inline=False)
    embed.set_footer(text=f"Logged in as : {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_image(url="https://media1.tenor.com/images/1af9a5ab8b0e5b3ec8f90648b9d79857/tenor.gif")
    await ctx.send(embed=embed)

@JANKY.command()
async def Nigger(ctx):
    await ctx.message.delete()
    await ctx.send('https://cdn.discordapp.com/attachments/738243069115105291/742982380779864165/2020-08-12_01-46-24.mp4')

@JANKY.command()
async def Minecraft(ctx):
    await ctx.message.delete()
    await ctx.send('https://cdn.discordapp.com/attachments/738243069115105291/742983087419293776/2020-08-12_01-49-15.mp4')

@JANKY.command()
async def Gay(ctx):
    await ctx.message.delete()
    await ctx.send('https://cdn.discordapp.com/attachments/738243069115105291/742983765357363250/2020-08-12_01-52-00.mp4')

@JANKY.command()
async def Rage(ctx):
    await ctx.message.delete()
    await ctx.send('https://cdn.discordapp.com/attachments/738243069115105291/742984243923124317/2020-08-12_01-53-13.mp4')

@JANKY.command()
async def Scam(ctx):
    await ctx.message.delete()
    await ctx.send('https://cdn.discordapp.com/attachments/738243069115105291/742986229699837972/2020-08-12_01-58-53.mp4')
    
@JANKY.command()
async def Scream(ctx):
    await ctx.message.delete()
    await ctx.send('https://cdn.discordapp.com/attachments/738243069115105291/742986897646813184/2020-08-12_02-03-59.mp4')

@JANKY.command()
async def Fight(ctx):
    await ctx.message.delete()
    await ctx.send('https://cdn.discordapp.com/attachments/741191098847854632/742987736675516456/2020-08-12_02-05-46.mp4')

JANKY.run('YOUR TOKEN HERE', bot=False)