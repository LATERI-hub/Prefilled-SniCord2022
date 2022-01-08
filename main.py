from discord.ext import commands
import json
from colorama import Fore, Back, Style , init
from discord.utils import get;init()
import gen3sniper
from datetime import datetime
import asyncio
import os
from spammer import Spammer as sp
import threading 

baseColour = Fore.CYAN + Style.BRIGHT
errorColour = Fore.RED + Style.BRIGHT + "Error : "
infoColour = Fore.YELLOW + Style.BRIGHT
accentColour = Fore.MAGENTA + Style.BRIGHT + "Claimed : "
successColour = Fore.GREEN + Style.BRIGHT + "Success : "
offcolour = Fore.RED + Style.BRIGHT
oncolour = Fore.GREEN + Style.BRIGHT

def getColour(event):
    if event == "on":
        return oncolour , '🟩'
    if event == "off":
        return offcolour , '🟥'
    if event == "info":
        return infoColour , '🟨'

def getChannels():
    with open('channels.json' , 'r' , encoding='utf-8' ) as f:
        return json.load(f)

def setChannels(data):
    with open('channels.json' , 'w' , encoding='utf-8') as f:
        json.dump(data , f)

def getConfig():
    with open('config.json' , 'r' , encoding='utf-8') as c:
        return json.load(c)

def setConfig(data):
    with open('config.json' , 'w' , encoding='utf-8') as c:
        json.dump(data , c)

try:
    configdat = getConfig()
    prefix = configdat['prefix']
    token = configdat['token']
    anigameSniper = configdat['anigameSniper']
    izziSniper = configdat['izziSniper']
    latency = configdat['latency']
    respond = configdat['respond']
except Exception as e:
    print(errorColour + f'Failed to Fetch config data\n{e}')

try:
    client = commands.Bot(
        command_prefix=prefix,  
        case_insensitive=True 
    )
except Exception as e:
    print(errorColour + f'{e}')


@client.event 
async def on_ready(): 
    print(baseColour+"""

   ___        _                    
  / _ | ___  (_)__ ____ ___ _  ___ 
 / __ |/ _ \/ / _ `/ _ `/  ' \/ -_)
/_/ |_/_//_/_/\_, /\_,_/_/_/_/\__/ 
   ____     _/___/                 
  / __/__  (_)__  ___ ____         
 _\ \/ _ \/ / _ \/ -_) __/         
/___/_//_/_/ .__/\__/_/            
  _____   /_/       ____           
 / ___/__ ___  ____|_  /           
/ (_ / -_) _ \/___//_ <            
\___/\__/_//_/   /____/            

アニゲームスナイパージェネレーション-3
                                                                                                                 
- ver.4.0 \n\n\nMade by - Sebastian09-09\n\n""")
    print(infoColour + f'Prefix : "{prefix}" ')
    print(infoColour + f'User : {client.user}\nUser-ID : {client.user.id}')
    print(infoColour + f'Anigame Sniper : {anigameSniper}')
    print(infoColour + f'Izzi Sniper : {izziSniper}')
    print(infoColour + f'Client Latency : {round(client.latency * 1000)}ms')
    print(infoColour + f'Latency : {latency}s')
    print(infoColour + f'Respond : {respond}\n\n')


recentClaimTimeAnigame = {}
recentClaimTimeIzzi = {}
threads = {}

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        try:
            async for msg in message.channel.history(limit=10):
                if message.id == msg.id:
                    content = msg.content
                    contentParts = content.split()
                    if content.startswith(prefix):
                        await msg.delete()
                        if content == f'{prefix}exit':
                            respond = getConfig()['respond']
                            print(offcolour + 'Exiting the sniper... ')
                            if respond == "on":
                                await message.channel.send(f'``🟥 Exiting the sniper... ``')
                            os._exit(1)
                        
                        elif f'{prefix}spam' in content and len(contentParts) == 2 and contentParts[1].isnumeric():
                            respond = getConfig()['respond']
                            print(successColour + infoColour + f'Starting to spam in channel { message.channel.name + " : " + str(message.channel.id) } ')
                            if respond == "on":
                                await message.channel.send(f'``🟩 Starting to spam in channel { message.channel.name + " : " + str(message.channel.id) } ``')
                            sp.threads[str(message.channel.id)] = threading.Thread(target=sp.sendMessage , args=(message.channel.id , token , int(contentParts[1])))
                            sp.threads[str(message.channel.id)].setDaemon(True)
                            sp.threads[str(message.channel.id)].start()

                        elif content == f'{prefix}snipers':
                            configdat=getConfig()
                            respond = configdat['respond']
                            
                            print(getColour(configdat["anigameSniper"])[0] + f'Anigame Sniper : {configdat["anigameSniper"]}')
                            print(getColour(configdat["izziSniper"])[0] + f'Izzi Sniper : {configdat["izziSniper"]}')

                            if respond == "on":
                                a=await message.channel.send(f'``{getColour(configdat["anigameSniper"])[1]} Anigame Sniper : {configdat["anigameSniper"]} ``\n``{getColour(configdat["izziSniper"])[1]} Izzi Sniper : {configdat["izziSniper"]} ``')
                                await asyncio.sleep(10);await a.delete()

                        elif content.startswith(f'{prefix}snipers') and len(contentParts) == 2 and contentParts[1].lower() in ['on' , 'off']:
                            configdat=getConfig()
                            value = contentParts[1].lower()
                            configdat['anigameSniper'] = value
                            configdat['izziSniper'] = value
                            respond = configdat['respond']
                            anigameSniper = value
                            izziSniper = value
                            setConfig(configdat)
                            print( successColour + getColour(anigameSniper)[0] + f'Anigame Sniper : {anigameSniper}')
                            print( successColour +  getColour(izziSniper)[0] + f'Izzi Sniper : {izziSniper}')
                            if respond == "on":
                                a=await message.channel.send(f'``{getColour(anigameSniper)[1]} Anigame Sniper : {anigameSniper} ``\n``{getColour(izziSniper)[1]} Izzi Sniper : {izziSniper} ``')
                                await asyncio.sleep(10);await a.delete()

                        elif len(contentParts) == 3 and contentParts[0] == f'{prefix}toggle' and contentParts[2].lower() in ['on' , 'off']:
                            sniper = contentParts[1].lower()
                            value = contentParts[2].lower()
                            configdat=getConfig()
                            respond = configdat['respond']
                            if sniper.startswith('a'):
                                configdat['anigameSniper'] = value
                                setConfig(configdat)
                                anigameSniper = value
                                print( successColour + getColour(anigameSniper)[0] + f'Anigame Sniper : {anigameSniper}')
                                if respond == "on":
                                    a=await message.channel.send(f'``{getColour(anigameSniper)[1]} Anigame Sniper : {anigameSniper} ``')
                                    await asyncio.sleep(10);await a.delete()
                            elif sniper.startswith('i'):
                                configdat['izziSniper'] = value
                                setConfig(configdat)
                                izziSniper = value
                                print( successColour + getColour(izziSniper)[0] + f'Izzi Sniper : {izziSniper}')
                                if respond == "on":
                                    a=await message.channel.send(f'``{getColour(izziSniper)[1]} Izzi Sniper : {izziSniper} ``')
                                    await asyncio.sleep(10);await a.delete()

                            elif sniper.startswith('r'):
                                configdat['respond'] = value
                                setConfig(configdat)
                                respond=value
                                print( successColour + getColour(respond)[0] + f'Respond : {respond}')
                                if respond == "on":
                                    a=await message.channel.send(f'``{getColour(respond)[1]} Respond : {respond} ``')
                                    await asyncio.sleep(10);await a.delete()

                            else:
                                print(errorColour + 'Could not understand the command')
                                if respond == "on":
                                    a=await message.channel.send(f'``⚠️ Could not understand the command ``')
                                    await asyncio.sleep(10);await a.delete()
                        
                        elif content == f'{prefix}latency':
                            configdat=getConfig()
                            respond = configdat['respond']
                            lat = round(client.latency * 1000)
                            print(infoColour + f'Client Latency : {lat}ms')
                            print(infoColour + f'Latency : {configdat["latency"]}s')
                            if respond == "on":
                                a=await message.channel.send(f'``🟨 Client Latency : {lat}ms ``\n``🟨 Latency : {configdat["latency"]}s ``')
                                await asyncio.sleep(10);await a.delete()
                                
                        elif content.startswith(f'{prefix}setlatency') and len(contentParts) == 2 and contentParts[1].isnumeric():
                            configdat=getConfig()
                            latency = contentParts[1]
                            configdat['latency'] = latency
                            respond = configdat['respond']
                            setConfig(configdat)
                            print(successColour + infoColour + f'Latency : {latency}s')
                            if respond == "on":
                                a=await message.channel.send(f'``🟨 Latency : {latency}s ``')
                                await asyncio.sleep(10);await a.delete()
                        
                        elif content == f'{prefix}addchannel':
                            dbid = str(msg.guild.id)+'|'+str(msg.channel.id)
                            respond = getConfig()['respond']
                            channeldat=getChannels()
                            if dbid not in channeldat:
                                channeldat[dbid] = [msg.guild.name , msg.channel.name]
                                setChannels(channeldat)
                                print(successColour + f'Channel {msg.channel.name} is now being sniped')
                                if respond == "on":
                                    a=await message.channel.send(f'``🟩 Channel {msg.channel.name} is now being sniped ``')
                                    await asyncio.sleep(10);await a.delete()
                            else:
                                print(infoColour + f'Channel {msg.channel.name} is already being sniped')
                                if respond == "on":
                                    a=await message.channel.send(f'``⚠️ Channel {msg.channel.name} is already being sniped ``')
                                    await asyncio.sleep(10);await a.delete()
                        
                        elif content == f'{prefix}addguild':
                            channeldat=getChannels()
                            respond = getConfig()['respond']
                            message_=''
                            for channel in msg.guild.channels:
                                if str(channel.type) == 'text':
                                    if str(msg.guild.id)+'|'+str(channel.id) not in channeldat:
                                        channeldat[str(msg.guild.id)+'|'+str(channel.id)] = [msg.guild.name , channel.name]
                                        setChannels(channeldat)
                                        print(successColour + f'Channel {channel.name} is now being sniped')
                                        if respond == "on":
                                            message_ += f'``🟩 Channel {channel.name} is now being sniped ``\n'
                                    else:
                                        print(infoColour + f'Channel {channel.name} is already being sniped')
                                        if respond == "on":
                                            message_ += f'``⚠️ Channel {channel.name} is already being sniped ``\n'
                            if respond == "on":
                                a=await message.channel.send(message_)
                                await asyncio.sleep(10);await a.delete()
                            

                        elif content == f'{prefix}removechannel':
                            dbid = str(msg.guild.id)+'|'+str(msg.channel.id)
                            channeldat=getChannels()
                            respond = getConfig()['respond']
                            if dbid in channeldat:
                                del channeldat[dbid]
                                print(successColour + offcolour + f'Channel {msg.channel.name} is now not being sniped')
                                if respond == "on":
                                    a=await message.channel.send(f'``🟥 Channel {msg.channel.name} is now not being sniped ``')
                                    await asyncio.sleep(10);await a.delete()
                            else:
                                print(infoColour + f'Channel {msg.channel.name} was not being sniped')
                                if respond == "on":
                                    a=await message.channel.send(f'``⚠️ Channel {msg.channel.name} was not being sniped ``')
                                    await asyncio.sleep(10);await a.delete()
                            setChannels(channeldat)

                        elif content == f'{prefix}removeguild':
                            channeldat=getChannels()
                            respond = getConfig()['respond']
                            message_ = ''
                            for channel in list(channeldat.keys()):
                                if channel.startswith(str(msg.guild.id)):
                                    channelName = channeldat[channel][1]
                                    del channeldat[channel]
                                    print( successColour + offcolour + f'Channel {channelName} is now not being sniped')
                                    if respond == "on":
                                        message_ += f'``🟥 Channel {channelName} is now not being sniped ``\n'
                            print(successColour + offcolour + 'Removed all the channels from this guild ')
                            setChannels(channeldat)
                            if respond == "on":
                                if message_ != '':
                                    a=await message.channel.send(message_)
                                else:
                                    a=await message.channel.send(f'``⚠️ Guild was not being sniped ``')
                                await asyncio.sleep(10);await a.delete()

                        elif content == f'{prefix}clearchannels':
                            respond = getConfig()['respond']
                            channeldat=getChannels()
                            channeldat.clear()
                            print(successColour + offcolour + f'Cleared all the channels')
                            if respond == "on":
                                a=await message.channel.send('``🟩 Cleared all the channels ``')
                                await asyncio.sleep(10);await a.delete()
                            setChannels(channeldat)

                        elif content == f'{prefix}channels':
                            channeldat=getChannels()
                            l = len(channeldat) 
                            message_ = ''
                            respond = getConfig()['respond']
                            if l == 1:
                                print(infoColour + f"sniper is \"on\" in {l} channel!")
                                if respond == "on":
                                    message_ += f"``🟩 sniper is \"on\" in {l} channel! ``\n"
                            else:
                                print(infoColour + f"sniper is \"on\" in {l} channels!")
                                if respond == "on":
                                    message_ += f"``🟩 sniper is \"on\" in {l} channels! ``\n"
                            for channel in channeldat:
                                print(infoColour + f"---> {channeldat[channel][0]} : {channeldat[channel][1]}")
                                if respond == "on":
                                    message_ += f'``🟨 ---> {channeldat[channel][0]} : {channeldat[channel][1]} ``\n'
                            if respond == "on":
                                a=await message.channel.send(message_)
                                await asyncio.sleep(10);await a.delete()
                                
                        
                        else:
                            print(errorColour + f'Could not understand the command : {message.content}')
                            if getConfig()['respond'] == "on":
                                a=await message.channel.send(f'``🟥 Could not understand the command : {message.content} ``')
                                await asyncio.sleep(10);await a.delete()
                                
        
        except Exception as e:
            print(errorColour + f'{e}')
        
    
    elif message.author.id == 571027211407196161 and f'{str(message.guild.id)}|{str(message.channel.id)}' in getChannels():
        try:
            configdat=getConfig()
            latency=int(configdat['latency'])
            if configdat['anigameSniper'] == 'on':
                async for msg in message.channel.history(limit=10):
                    if message.id == msg.id:
                        for embed in msg.embeds:
                            embedInfo = (embed.to_dict())
                            if 'description' in embedInfo:
                                description = embedInfo['description']
                            else:
                                description = 'nil'
                            
                            if f'has been added to **{client.user.name}\'s** collection!' in description:
                                now = datetime.now();current_time = now.strftime("%H:%M:%S")
                                rarity = description.split('__')[1]
                                name = description.split('**')[1]
                                print(accentColour + f'Anigame : {rarity} : {name} : Claimed by {client.user} : {recentClaimTimeAnigame[message.channel.id]}')

                            elif description == '*A wild anime card appears!*':
                                now = datetime.now();current_time = now.strftime("%H:%M:%S")
                                print(baseColour + f'Anigame : A wild anime card appears! : {current_time}')
                                await asyncio.sleep(latency)
                                resp=gen3sniper.clickButton(str(msg.guild.id) , str(msg.channel.id) , str(msg.id) , token , 'Claim!')
                                if resp == 204:
                                    now = datetime.now();current_time = now.strftime("%H:%M:%S")
                                    recentClaimTimeAnigame[message.channel.id] = current_time

        except Exception as e:
            print(errorColour + f'{e}')            

        

    elif message.author.id == 784851074472345633 and f'{str(message.guild.id)}|{str(message.channel.id)}' in getChannels():
        try:
            configdat=getConfig()
            latency=int(configdat['latency'])
            if configdat['izziSniper'] == 'on':
                async for msg in message.channel.history(limit=10):
                    if message.id == msg.id:
                        if f'has been added to **{client.user.name}\'s** collection.' in msg.content:
                            now = datetime.now();current_time = now.strftime("%H:%M:%S")
                            rarity = msg.content.split('__')[1]
                            name = msg.content.split('**')[1]
                            print(accentColour + f'Izzi : {rarity} : {name} : Claimed by {client.user} : {recentClaimTimeIzzi[message.channel.id]}')

                        for embed in msg.embeds:
                            embedInfo = (embed.to_dict())
                            if 'description' in embedInfo:
                                description = embedInfo['description']
                            else:
                                description = 'nil'
                                
                            if description == '_A wild card has appeared._':
                                now = datetime.now();current_time = now.strftime("%H:%M:%S")
                                print(baseColour + f'Izzi : A wild card has appeared. : {current_time}')
                                await asyncio.sleep(latency)
                                resp=gen3sniper.add_reaction(msg.channel.id , msg.id , '✅' , token)
                                if resp == 204:
                                    now = datetime.now();current_time = now.strftime("%H:%M:%S")
                                    recentClaimTimeIzzi[message.channel.id] = current_time
                                


        except Exception as e:
            print(errorColour + f'{e}')

try:
    client.run(token, bot=False)
except Exception as e:
    print(errorColour + f'{e}')