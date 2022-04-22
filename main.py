import os
try:
    from discord.ext import commands , tasks
except:
    os.system('pip install discord')
    from discord.ext import commands , tasks
try:
    from colorama import Fore, Style , init;init()
except:
    os.system('pip install colorama')
    from colorama import Fore, Style , init;init()
import json
from colorama import Fore, Style , init;init()
import gen3sniper
from datetime import datetime
import asyncio
from spammer import Spammer as sp
import spammer
import threading 
import server
import random

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

def getNotif():
    with open('notificationSettings.json' , 'r' , encoding='utf-8') as c:
        return json.load(c)

def clearText(text):
    newText = ''
    for i in text:
        if i != ' ':
            newText += i
    return newText

def checkSpamFile():
    files=os.listdir()
    if 'spam.json' not in files:
        with open('spam.json' , 'w' , encoding='utf-8') as f:
            f.write('{}')

def spam(spamTokens , token):
    spamChannels=spammer.getSpam()
    for channel in spamChannels:
        spamTokens.append(token)
        sp.threads[str(channel)] = threading.Thread(target=sp.sendMessage , args=(channel , spamTokens , spamChannels[channel] ,  f'channel id : {channel}' ))
        sp.threads[str(channel)].setDaemon(True)
        sp.threads[str(channel)].start()

try:
    configdat = getConfig()
    prefix = configdat['prefix']
    controllerAccountID = configdat['controllerAccountID']
    token = configdat['token']
    spamTokens = configdat['spamTokens']
    anigameSniper = configdat['anigameSniper']
    izziSniper = configdat['izziSniper']
    latency = configdat['latency']
    respond = configdat['respond']
    baseChannelID = configdat['baseChannelID']
    baseChannelAnigamePrefix = configdat['baseChannelAnigamePrefix']
    baseChannelIzziPrefix = configdat['baseChannelIzziPrefix']
    anigameLottery = configdat['anigameLottery']
    anigameHourly = configdat['anigameHourly']
    anigameBTALL = configdat['anigameBTALL']
    izziLottery = configdat['izziLottery']
    izziHourly = configdat['izziHourly']
    izziBTALL = configdat['izziBTALL']
    notificationChannelID = configdat['notificationChannelID']
    anigameFloor = {}
    izziFloor = {}
    anigameFloor['currentFloor'] = configdat['anigameFloorNumber']
    anigameAutoFloor_ = configdat['anigameAutoFloor']
    izziFloor['currentFloor'] = configdat['izziFloorNumber']
    izziAutoFloor_ = configdat['izziAutoFloor']

    notify = getNotif()
    anigameNotif = notify['anigame'];anigameNotif = list(map(lambda x:clearText(x.lower()) , anigameNotif))
    izziNotif = notify['izzi'];izziNotif = list(map(lambda x:clearText(x.lower()) , izziNotif))

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

アニゲームスナイパージェネレーション - 三   ||  version 4.4 \n\nMade by - Sebastian09-09\n""")
    print(infoColour + f'Prefix : "{prefix}" ')
    print(baseColour + f'User : {client.user}\nUser-ID : {client.user.id}')
    print(getColour(anigameSniper)[0] + f'Anigame Sniper : {anigameSniper}')
    print(getColour(izziSniper)[0] + f'Izzi Sniper : {izziSniper}')
    print(infoColour + f'Client Latency : {round(client.latency * 1000)}ms')
    print(infoColour + f'Latency : {latency}s')
    print(infoColour + f'Respond : {respond}')
    print(getColour(anigameLottery)[0] + f'Anigame Lottery : {anigameLottery}')
    print(getColour(anigameHourly)[0] + f'Anigame Hourly : {anigameHourly}')
    print(getColour(anigameBTALL)[0] + f'Anigame bt all : {anigameBTALL}')
    print(getColour(anigameAutoFloor_)[0] + f'Anigame Auto Floor : {anigameAutoFloor_}')
    print(getColour(izziLottery)[0] + f'Izzi Lottery : {izziLottery}')
    print(getColour(izziHourly)[0] + f'Izzi Hourly : {izziHourly}')
    print(getColour(izziBTALL)[0] + f'Izzi bt all : {izziBTALL}')
    print(getColour(izziAutoFloor_)[0] + f'Izzi Auto Floor : {izziAutoFloor_}\n\n')

    if anigameLottery == "on":
        anigameLotteryLoop.start()
    if anigameHourly == "on":
        anigameHourlyLoop.start()
    if anigameAutoFloor_ == "on":
        anigameAutoFloor.start()
    if anigameBTALL == "on":
        anigameBTALLLoop.start() 
    if izziLottery == "on":
        izziLotteryLoop.start()
        await asyncio.sleep(2)
    if izziHourly == "on":
        izziHourlyLoop.start()
        await asyncio.sleep(2)
    if izziAutoFloor_ == "on":
        izziAutoFloor.start()
        await asyncio.sleep(2)
    if izziBTALL == "on":
        izziBTALLLoop.start()
        await asyncio.sleep(2)
    

    checkSpamFile()
    spam(spamTokens , token)

#you can change the time according to the cooldowns


#anigame auto floor/location
@tasks.loop(minutes=30)
async def anigameAutoFloor():
    await client.get_channel(int(baseChannelID)).send(f'{baseChannelAnigamePrefix}fl {anigameFloor["currentFloor"]}')
    await client.get_channel(int(baseChannelID)).send(f'{baseChannelAnigamePrefix}bt')
    await asyncio.sleep(450) 
    await client.get_channel(int(baseChannelID)).send(f'{baseChannelAnigamePrefix}bt all')
    await asyncio.sleep(450)
    await client.get_channel(int(baseChannelID)).send(f'{baseChannelAnigamePrefix}fl {anigameFloor["currentFloor"]+1}')


#anigame lottery
@tasks.loop(minutes=10 , seconds=30)
async def anigameLotteryLoop():
    await client.get_channel(int(baseChannelID)).send(f'{baseChannelAnigamePrefix}lottery')

#anigame hourly
@tasks.loop(hours=1 , seconds=30)
async def anigameHourlyLoop():
    await client.get_channel(int(baseChannelID)).send(f'{baseChannelAnigamePrefix}hourly')

#anigame bt all
@tasks.loop(minutes=30)
async def anigameBTALLLoop():
    await client.get_channel(int(baseChannelID)).send(f'{baseChannelAnigamePrefix}bt all')

#izzi auto floor/location
@tasks.loop(minutes=30)
async def izziAutoFloor():
    await client.get_channel(int(baseChannelID)).send(f'{baseChannelIzziPrefix}fl {izziFloor["currentFloor"]}')
    await asyncio.sleep(5) 
    await client.get_channel(int(baseChannelID)).send(f'{baseChannelIzziPrefix}bt')
    await asyncio.sleep(450) 
    await client.get_channel(int(baseChannelID)).send(f'{baseChannelIzziPrefix}bt all')
    await asyncio.sleep(450)
    await client.get_channel(int(baseChannelID)).send(f'{baseChannelIzziPrefix}fl {izziFloor["currentFloor"]+1}')


#izzi lottery
@tasks.loop(minutes=15 , seconds=30)
async def izziLotteryLoop():
    await client.get_channel(int(baseChannelID)).send(f'{baseChannelIzziPrefix}lottery')

#izzi hourly
@tasks.loop(hours=1 , seconds=30)
async def izziHourlyLoop():
    await client.get_channel(int(baseChannelID)).send(f'{baseChannelIzziPrefix}hourly')

#izzi bt all
@tasks.loop(minutes=30)
async def izziBTALLLoop():
    await client.get_channel(int(baseChannelID)).send(f'{baseChannelIzziPrefix}bt all')

recentClaimTimeAnigame = {}
recentClaimTimeIzzi = {}

async def notificate(bot , name , rarity,channelName,token):
    await client.get_channel(int(notificationChannelID)).send(f'`{bot}` : Claimed **{rarity}** __{name}__ in channel {channelName}')
    gen3sniper.makeUnread(notificationChannelID,token)

async def notificateDefeat(bot ,token):
    await client.get_channel(int(notificationChannelID)).send(f'`{bot}` : Defeated in a battle stopping Auto Floor Loop')
    gen3sniper.makeUnread(notificationChannelID,token)

async def changeArea():
    await client.get_channel(int(baseChannelID)).send(f'{baseChannelAnigamePrefix}area {getConfig()["anigameAreaNumber"]}')

async def changeLoc():
    await client.get_channel(int(baseChannelID)).send(f'{baseChannelIzziPrefix}loc {getConfig()["izziLocNumber"]}')

@client.event
async def on_message(message):
    #Commands
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
                                spamChannels = spammer.getSpam()
                                spamChannels.clear()
                                spammer.setSpam(spamChannels)
                            os._exit(1)
                        
                        elif f'{prefix}spam' in content and len(contentParts) == 2 and contentParts[1].isnumeric():
                            respond = getConfig()['respond']
                            print(successColour + oncolour + f'Starting to spam in channel { message.channel.name + " : " + str(message.channel.id) } ')
                            if respond == "on":
                                a=await message.channel.send(f'``🟩 Starting to spam in channel { message.channel.name + " : " + str(message.channel.id) } ``')
                            spamTokens.append(token)
                            sp.threads[str(message.channel.id)] = threading.Thread(target=sp.sendMessage , args=(message.channel.id , spamTokens , int(contentParts[1]) , message.channel.name))
                            sp.threads[str(message.channel.id)].setDaemon(True)
                            sp.threads[str(message.channel.id)].start()
                            spamChannels = spammer.getSpam()
                            spamChannels[(str(message.channel.id))] = int(contentParts[1])
                            spammer.setSpam(spamChannels)
                            if respond == "on":
                                await asyncio.sleep(10);await a.delete()

                        elif f'{prefix}spam' in content and len(contentParts) == 2 and contentParts[1] == '!':
                            respond = getConfig()['respond']
                            print(successColour + oncolour + f'Starting to spam in channel { message.channel.name + " : " + str(message.channel.id) } ')
                            if respond == "on":
                                a=await message.channel.send(f'``🟩 Starting to spam in channel { message.channel.name + " : " + str(message.channel.id) } ``')
                            spamTokens.append(token)
                            sp.threads[str(message.channel.id)] = threading.Thread(target=sp.sendMessage , args=(message.channel.id , spamTokens , contentParts[1] , message.channel.name))
                            sp.threads[str(message.channel.id)].setDaemon(True)
                            sp.threads[str(message.channel.id)].start()
                            spamChannels = spammer.getSpam()
                            spamChannels[(str(message.channel.id))] = '!'
                            spammer.setSpam(spamChannels)
                            if respond == "on":
                                await asyncio.sleep(10);await a.delete()

                        elif content == f'{prefix}stopspam':
                            respond = getConfig()['respond']
                            if str(message.channel.id) in sp.threads:
                                del sp.threads[str(message.channel.id)]
                                spamChannels = spammer.getSpam()
                                del spamChannels[(str(message.channel.id))]
                                spammer.setSpam(spamChannels)
                                print(successColour + offcolour + f'Stopping spam in channel { message.channel.name + " : " + str(message.channel.id) } ')
                                if respond == "on":
                                    a=await message.channel.send(f'``🟥 Stopping spam in channel { message.channel.name + " : " + str(message.channel.id) } ``')
                                    await asyncio.sleep(10);await a.delete()
                            else:
                                print(infoColour + f'Channel { message.channel.name + " : " + str(message.channel.id) } is not being spammed ')
                                if respond == "on":
                                    a=await message.channel.send(f'``⚠️ Channel { message.channel.name + " : " + str(message.channel.id) } is not being spammed  ``')
                                    await asyncio.sleep(10);await a.delete()
                        
                        elif content == f'{prefix}features':
                            configdat=getConfig()
                            respond = configdat['respond']
                            print(getColour(configdat["anigameLottery"])[0] + f'Anigame Lottery : {configdat["anigameLottery"]}')
                            print(getColour(configdat["anigameHourly"])[0] + f'Anigame Hourly : {configdat["anigameHourly"]}')
                            print(getColour(configdat["anigameBTALL"])[0] + f'Anigame bt all : {configdat["anigameBTALL"]}')
                            print(getColour(configdat["anigameAutoFloor"])[0] + f'Anigame Auto Floor : {configdat["anigameAutoFloor"]}')
                            print(getColour(configdat["izziLottery"])[0] + f'Izzi Lottery : {configdat["izziLottery"]}')
                            print(getColour(configdat["izziHourly"])[0] + f'Izzi Hourly : {configdat["izziHourly"]}')
                            print(getColour(configdat["izziBTALL"])[0] + f'Izzi bt all : {configdat["izziBTALL"]}')
                            print(getColour(configdat["izziAutoFloor"])[0] + f'izzi Izzi Floor : {configdat["izziAutoFloor"]}')
                            if respond == "on":
                                a=await message.channel.send(f'``{getColour(configdat["anigameLottery"])[1]} Anigame Lottery : {configdat["anigameLottery"]} ``\n``{getColour(configdat["anigameHourly"])[1]} Anigame Hourly : {configdat["anigameHourly"]} ``\n``{getColour(configdat["anigameBTALL"])[1]} Anigame bt all : {configdat["anigameBTALL"]} ``\n``{getColour(configdat["anigameAutoFloor"])[1]} Anigame Auto Floor : {configdat["anigameAutoFloor"]} ``\n``{getColour(configdat["izziLottery"])[1]} Izzi Lottery : {configdat["izziLottery"]} ``\n``{getColour(configdat["izziHourly"])[1]} Izzi Hourly : {configdat["izziHourly"]} ``\n``{getColour(configdat["izziBTALL"])[1]} Izzi bt all : {configdat["izziBTALL"]} ``\n``{getColour(configdat["izziAutoFloor"])[1]} Izzi Auto Floor : {configdat["izziAutoFloor"]} ``')
                                await asyncio.sleep(10);await a.delete()
                        
                        elif content.startswith(f'{prefix}features') and len(contentParts) == 2 and contentParts[1].lower() in ['on' , 'off']:
                            configdat=getConfig()
                            respond = configdat["respond"]
                            value = contentParts[1].lower()
                            anigameLottery = value;configdat['anigameLottery'] = anigameLottery
                            anigameHourly = value;configdat['anigameHourly'] = anigameHourly
                            anigameBTALL = value;configdat['anigameBTALL'] = anigameBTALL
                            anigameAutoFloor_ = value;configdat['anigameAutoFloor'] = anigameAutoFloor_
                            izziLottery = value;configdat['izziLottery'] = izziLottery
                            izziHourly = value;configdat['izziHourly'] = izziHourly
                            izziBTALL = value;configdat['izziBTALL'] = izziBTALL
                            izziAutoFloor_ = value;configdat['izziAutoFloor'] = izziAutoFloor_
                            setConfig(configdat)

                            if anigameLotteryLoop.is_running() and anigameLottery == "off":
                                anigameLotteryLoop.cancel()
                            elif not anigameLotteryLoop.is_running() and anigameLottery == "on":
                                anigameLotteryLoop.start()

                            if anigameHourlyLoop.is_running() and anigameHourly == "off":
                                anigameHourlyLoop.cancel()
                            elif not anigameHourlyLoop.is_running() and anigameHourly == "on":
                                anigameHourlyLoop.start()

                            if anigameBTALLLoop.is_running() and anigameBTALL == "off":
                                anigameBTALLLoop.cancel()
                            elif not anigameBTALLLoop.is_running() and anigameBTALL == "on":
                                anigameBTALLLoop.start()

                            if anigameAutoFloor.is_running() and anigameAutoFloor_ == "off":
                                anigameAutoFloor.cancel()
                            elif not anigameAutoFloor.is_running() and anigameAutoFloor_ == "on":
                                anigameAutoFloor.start()

                            if izziLotteryLoop.is_running() and izziLottery == "off":
                                izziLotteryLoop.cancel()
                            elif not izziLotteryLoop.is_running() and izziLottery == "on":
                                izziLotteryLoop.start()
                                
                            if izziHourlyLoop.is_running() and izziLottery == "off":
                                izziHourlyLoop.cancel()
                            elif not izziHourlyLoop.is_running() and izziLottery == "on":
                                izziHourlyLoop.start()
                            
                            if izziBTALLLoop.is_running() and izziBTALL == "off":
                                izziBTALLLoop.cancel()
                            elif not izziBTALLLoop.is_running() and izziBTALL == "on":
                                izziBTALLLoop.start()

                            if izziAutoFloor.is_running() and izziAutoFloor_ == "off":
                                izziAutoFloor.cancel()
                            elif not izziAutoFloor.is_running() and izziAutoFloor_ == "on":
                                izziAutoFloor.start()

                            print(getColour(anigameLottery)[0] + f'Anigame Lottery : {anigameLottery}')
                            print(getColour(anigameHourly)[0] + f'Anigame Hourly : {anigameHourly}')
                            print(getColour(anigameBTALL)[0] + f'Anigame bt all : {anigameBTALL}')
                            print(getColour(anigameAutoFloor_)[0] + f'Anigame Auto Floor : {anigameAutoFloor_}')
                            print(getColour(izziLottery)[0] + f'Izzi Lottery : {izziLottery}')
                            print(getColour(izziHourly)[0] + f'Izzi Hourly : {izziHourly}')
                            print(getColour(izziBTALL)[0] + f'Izzi bt all : {izziBTALL}')
                            print(getColour(izziAutoFloor_)[0] + f'Izzi Auto Floor : {izziAutoFloor_}')
                            if respond == "on":
                                a=await message.channel.send(f'``{getColour(anigameLottery)[1]} Anigame Lottery : {anigameLottery} ``\n``{getColour(anigameHourly)[1]} Anigame Hourly : {anigameHourly} ``\n``{getColour(anigameBTALL)[1]} Anigame bt all : {anigameBTALL} ``\n``{getColour(anigameAutoFloor_)[1]} Anigame Auto Floor : {anigameAutoFloor_} ``\n``{getColour(configdat["izziLottery"])[1]} Izzi Lottery : {configdat["izziLottery"]} ``\n``{getColour(configdat["izziHourly"])[1]} Izzi Hourly : {configdat["izziHourly"]} ``\n``{getColour(izziBTALL)[1]} Izzi bt all : {izziBTALL} ``\n``{getColour(izziAutoFloor_)[1]} Izzi Auto Floor : {izziAutoFloor_} ``')
                                await asyncio.sleep(10);await a.delete()
                        

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

                            if sniper.startswith('anigamel'):
                                configdat['anigameLottery'] = value
                                setConfig(configdat)
                                anigameLottery=value
                                if anigameLottery == "off":
                                    if anigameLotteryLoop.is_running():anigameLotteryLoop.cancel()
                                elif anigameLottery == "on":
                                    if not anigameLotteryLoop.is_running():anigameLotteryLoop.start()
                                print( successColour + getColour(anigameLottery)[0] + f'Anigame Lottery : {anigameLottery}')
                                if respond == "on":
                                    a=await message.channel.send(f'``{getColour(anigameLottery)[1]} Anigame Lottery : {anigameLottery} ``')
                                    await asyncio.sleep(10);await a.delete()

                            elif sniper.startswith('anigameh'):
                                configdat['anigameHourly'] = value
                                setConfig(configdat)
                                anigameHourly=value
                                if anigameHourly == "off":
                                    if anigameHourlyLoop.is_running():anigameHourlyLoop.cancel()
                                elif anigameHourly == "on":
                                    if not anigameHourlyLoop.is_running():anigameHourlyLoop.start()
                                print( successColour + getColour(anigameHourly)[0] + f'Anigame Hourly : {anigameHourly}')
                                if respond == "on":
                                    a=await message.channel.send(f'``{getColour(anigameHourly)[1]} Anigame Hourly : {anigameHourly} ``')
                                    await asyncio.sleep(10);await a.delete()

                            elif sniper.startswith('anigameb'):
                                configdat['anigameBTALL'] = value
                                setConfig(configdat)
                                anigameBTALL=value
                                if anigameBTALL == "off":
                                    if anigameBTALLLoop.is_running():anigameBTALLLoop.cancel()
                                elif anigameBTALL == "on":
                                    if not anigameBTALLLoop.is_running():anigameBTALLLoop.start()
                                print( successColour + getColour(anigameBTALL)[0] + f'Anigame bt all : {anigameBTALL}')
                                if respond == "on":
                                    a=await message.channel.send(f'``{getColour(anigameBTALL)[1]} Anigame bt all : {anigameBTALL} ``')
                                    await asyncio.sleep(10);await a.delete()

                            elif sniper.startswith('anigamea'):
                                configdat['anigameAutoFloor'] = value
                                setConfig(configdat)
                                anigameAutoFloor_=value
                                if anigameAutoFloor_ == "off":
                                    if anigameAutoFloor.is_running():anigameAutoFloor.cancel()
                                elif anigameAutoFloor_ == "on":
                                    if not anigameAutoFloor.is_running():anigameAutoFloor.start()
                                print( successColour + getColour(anigameAutoFloor_)[0] + f'Anigame Auto Floor : {anigameAutoFloor_}')
                                if respond == "on":
                                    a=await message.channel.send(f'``{getColour(anigameAutoFloor_)[1]} Anigame Auto Floor : {anigameAutoFloor_} ``')
                                    await asyncio.sleep(10);await a.delete()

                            elif sniper.startswith('izzil'):
                                configdat['izziLottery'] = value
                                setConfig(configdat)
                                izziLottery=value
                                if izziLottery == "off":
                                    if izziLotteryLoop.is_running():izziLotteryLoop.cancel()
                                elif izziLottery == "on":
                                    if not izziLotteryLoop.is_running():izziLotteryLoop.start()
                                print( successColour + getColour(izziLottery)[0] + f'Izzi Lottery : {izziLottery}')
                                if respond == "on":
                                    a=await message.channel.send(f'``{getColour(izziLottery)[1]} Izzi Lottery : {izziLottery} ``')
                                    await asyncio.sleep(10);await a.delete()

                            elif sniper.startswith('izzih'):
                                configdat['izziHourly'] = value
                                setConfig(configdat)
                                izziHourly=value
                                if izziHourly == "off":
                                    if izziHourlyLoop.is_running():izziHourlyLoop.cancel()
                                elif izziHourly == "on":
                                    if not izziHourlyLoop.is_running():izziHourlyLoop.start()
                                print( successColour + getColour(izziHourly)[0] + f'Izzi Hourly : {izziHourly}')
                                if respond == "on":
                                    a=await message.channel.send(f'``{getColour(izziHourly)[1]} Izzi Hourly : {izziHourly} ``')
                                    await asyncio.sleep(10);await a.delete()

                            elif sniper.startswith('izzib'):
                                configdat['izziBTALL'] = value
                                setConfig(configdat)
                                izziBTALL=value
                                if izziBTALL == "off":
                                    if izziBTALLLoop.is_running():izziBTALLLoop.cancel()
                                elif izziBTALL == "on":
                                    if not izziBTALLLoop.is_running():izziBTALLLoop.start()
                                print( successColour + getColour(izziBTALL)[0] + f'Izzi bt all : {izziBTALL}')
                                if respond == "on":
                                    a=await message.channel.send(f'``{getColour(izziBTALL)[1]} Izzi bt all : {izziBTALL} ``')
                                    await asyncio.sleep(10);await a.delete()

                            elif sniper.startswith('izzia'):
                                configdat['izziAutoFloor'] = value
                                setConfig(configdat)
                                izziAutoFloor_=value
                                if izziAutoFloor_ == "off":
                                    if izziAutoFloor.is_running():izziAutoFloor.cancel()
                                elif izziAutoFloor_ == "on":
                                    if not izziAutoFloor.is_running():izziAutoFloor.start()
                                print( successColour + getColour(izziAutoFloor_)[0] + f'Anigame Auto Floor : {izziAutoFloor_}')
                                if respond == "on":
                                    a=await message.channel.send(f'``{getColour(izziAutoFloor_)[1]} Anigame Auto Floor : {izziAutoFloor_} ``')
                                    await asyncio.sleep(10);await a.delete()
                            
                            elif sniper.startswith('a'):
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
                                
                        elif content.startswith(f'{prefix}setlatency') and len(contentParts) == 2:
                            if contentParts[1].isnumeric():
                                configdat=getConfig()
                                latency = contentParts[1]
                                configdat['latency'] = str(latency)
                                respond = configdat['respond']
                                setConfig(configdat)
                                print(successColour + infoColour + f'Latency : {latency}s')
                                if respond == "on":
                                    a=await message.channel.send(f'``🟨 Latency : {latency}s ``')
                                    await asyncio.sleep(10);await a.delete()

                            elif contentParts[1].split('-')[0].isnumeric() and contentParts[1].split('-')[1].isnumeric():
                                configdat=getConfig()
                                latency = contentParts[1]
                                configdat['latency'] = str(latency)
                                respond = configdat['respond']
                                setConfig(configdat)
                                print(successColour + infoColour + f'Latency : {latency}s')
                                if respond == "on":
                                    a=await message.channel.send(f'``🟨 Latency : {latency}s ``')
                                    await asyncio.sleep(10);await a.delete()


                        elif f'{prefix}addchannel -a' in content and len(contentParts) == 3:
                            guildID = int(contentParts[2].split(':')[0])
                            channelID = int(contentParts[2].split(':')[1])
                            dbid = str(guildID)+'|'+str(channelID)
                            guildName = str(client.get_guild(int(guildID)))
                            channelName = str(client.get_channel(int(channelID)))
                            respond = getConfig()['respond']
                            channeldat=getChannels()
                            if dbid not in channeldat:
                                channeldat[dbid] = [guildName , channelName]
                                setChannels(channeldat)
                                print(successColour + f'Channel {channelName} is now being sniped')
                                if respond == "on":
                                    a=await message.channel.send(f'``🟩 Channel {channelName} is now being sniped ``')
                                    await asyncio.sleep(10);await a.delete()
                            else:
                                print(infoColour + f'Channel {channelName} is already being sniped')
                                if respond == "on":
                                    a=await message.channel.send(f'``⚠️ Channel {channelName} is already being sniped ``')
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
                            
                        elif f'{prefix}removechannel -a' in content and len(contentParts) == 3:
                            guildID = int(contentParts[2].split(':')[0])
                            channelID = int(contentParts[2].split(':')[1])
                            dbid = str(guildID)+'|'+str(channelID)
                            channelName = str(client.get_channel(int(channelID)))
                            channeldat=getChannels()
                            respond = getConfig()['respond']
                            if dbid in channeldat:
                                del channeldat[dbid]
                                print(successColour + offcolour + f'Channel {channelName} is now not being sniped')
                                if respond == "on":
                                    a=await message.channel.send(f'``🟥 Channel {channelName} is now not being sniped ``')
                                    await asyncio.sleep(10);await a.delete()
                            else:
                                print(infoColour + f'Channel {channelName} was not being sniped')
                                if respond == "on":
                                    a=await message.channel.send(f'``⚠️ Channel {channelName} was not being sniped ``')
                                    await asyncio.sleep(10);await a.delete()
                            setChannels(channeldat)

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
                                a=await message.channel.send(f'``⚠️ Could not understand the command : {message.content} ``')
                                await asyncio.sleep(10);await a.delete()
                                
        except Exception as e:
            print(errorColour + f'{e}')

    #Controller
    elif message.author.id == int(controllerAccountID):
        try:
            async for msg in message.channel.history(limit=10):
                if message.id == msg.id:
                    msgContent = msg.content 
                    if msgContent.startswith(f'{prefix}say'):
                        await msg.channel.send(f'{msgContent.split(f"{prefix}say")[-1].strip()}')

        except Exception as e:
            print(errorColour + f'{e}')
        
    #Anigame Sniper
    elif message.author.id == 571027211407196161:
        try:
            #Claimer
            if f'{str(message.guild.id)}|{str(message.channel.id)}' in getChannels():
                configdat=getConfig()
                latency=configdat['latency']
                if '-' not in latency:
                    latency = int(latency)
                else:
                    latency = int(random.randint(int(latency.split('-')[0]),int(latency.split('-')[1])))
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
                                    print(accentColour + f'Anigame : {msg.guild.name} : {msg.channel.name} : {rarity} : {name} : Claimed by {client.user} : {recentClaimTimeAnigame[message.channel.id]}')
                                    if clearText(rarity.lower()) in anigameNotif:
                                        await notificate('Anigame' , name , rarity , msg.channel.name,token)

                                elif description == '*A wild anime card appears!*':
                                    now = datetime.now();current_time = now.strftime("%H:%M:%S")
                                    print(baseColour + f'Anigame : {msg.guild.name} : {msg.channel.name} : A wild anime card appears! : {current_time}')
                                    await asyncio.sleep(latency)
                                    resp=gen3sniper.clickButton(str(msg.guild.id) , str(msg.channel.id) , str(msg.id) , token , 'Claim!','anigame')
                                    if resp == 204:
                                        now = datetime.now();current_time = now.strftime("%H:%M:%S")
                                        recentClaimTimeAnigame[message.channel.id] = current_time
                                    else:
                                        print(errorColour+f'couldnt claim the card : respond - {resp}')

            #checker 
            if message.channel.id == int(getConfig()['baseChannelID']):
                async for msg in message.channel.history(limit=10):
                    if message.id == msg.id:
                        title = description = author = footer = ''
                        for embed in msg.embeds:
                            embedInfo = (embed.to_dict())
                            title = embedInfo['title'] if 'title' in embedInfo else 'nil'
                            description = embedInfo['description'] if 'description' in embedInfo else 'nil'
                            author = embedInfo['author']['name'] if 'author' in embedInfo else 'nil'
                            footer = embedInfo['footer']['text'] if 'footer' in embedInfo else 'nil'
                        if 'Challenging Area' in title:
                            resp=gen3sniper.clickButton(str(msg.guild.id) , str(msg.channel.id) , str(msg.id) , token , '✅' , 'anigame')
                        elif author == client.user.name and f'Travelled to Area [**{getConfig()["anigameAreaNumber"]} - {anigameFloor["currentFloor"]+1}**]' in title and anigameAutoFloor_ == "on":
                            anigameFloor['currentFloor'] += 1
                            data = getConfig();data['anigameFloorNumber']+=1;setConfig(data)
                        elif author == client.user.name and title == 'Error ⛔' and 'this floor is not accessible! Please double check which area ID you would like to go to.' in description and anigameAutoFloor_ == "on":
                            anigameFloor['currentFloor'] = 1
                            data = getConfig();data['anigameFloorNumber']=1;data['anigameAreaNumber']+=1;setConfig(data)
                            await changeArea() 
                        elif author == client.user.name and '**Defeated' in title and anigameAutoFloor_ == "on":
                            if anigameAutoFloor.is_running():
                                anigameAutoFloor.cancel()
                            await notificateDefeat('Anigame' , token)
                        elif author == client.user.name and title == 'Error ⛔' and anigameAutoFloor_ == "on":
                            if 'You do not have enough stamina to proceed!' or 'you must fight atleast once!' in description:
                                if anigameAutoFloor.is_running():
                                    anigameAutoFloor.cancel()
                                await asyncio.sleep(1800)
                                if not anigameAutoFloor.is_running():
                                    anigameAutoFloor.start()


        except Exception as e:
            print(errorColour + f'{e}')            

    
    #Izzi Sniper
    elif message.author.id == 784851074472345633:
        try:
            #Izzi Sniper
            if f'{str(message.guild.id)}|{str(message.channel.id)}' in getChannels():
                configdat=getConfig()
                latency=configdat['latency']
                if '-' not in latency:
                    latency = int(latency)
                else:
                    latency = int(random.randint(int(latency.split('-')[0]),int(latency.split('-')[1])))
                if configdat['izziSniper'] == 'on':
                    async for msg in message.channel.history(limit=10):
                        if message.id == msg.id:
                            if f'has been added to **{client.user.name}\'s** collection.' in msg.content:
                                now = datetime.now();current_time = now.strftime("%H:%M:%S")
                                rarity = msg.content.split('__')[1]
                                name = msg.content.split('**')[1]
                                print(accentColour + f'Izzi : {msg.guild.name} : {msg.channel.name} : {rarity} : {name} : Claimed by {client.user} : {recentClaimTimeIzzi[message.channel.id]}')
                                if clearText(rarity.lower())  in izziNotif:
                                    await notificate('Izzi' , name , rarity , msg.channel.name,token)

                            for embed in msg.embeds:
                                embedInfo = (embed.to_dict())
                                if 'description' in embedInfo:
                                    description = embedInfo['description']
                                else:
                                    description = 'nil'
                                    
                                if description == '_A wild card has appeared._':
                                    now = datetime.now();current_time = now.strftime("%H:%M:%S")
                                    print(baseColour + f'Izzi : {msg.guild.name} : {msg.channel.name} : A wild card has appeared. : {current_time}')
                                    await asyncio.sleep(latency)
                                    resp=gen3sniper.clickButton(str(msg.guild.id) , str(msg.channel.id) , str(msg.id) , token , 'Claim','izzi')
                                    if resp == 204:
                                        now = datetime.now();current_time = now.strftime("%H:%M:%S")
                                        recentClaimTimeIzzi[message.channel.id] = current_time
                                    else:
                                        print(errorColour+f'couldnt claim the card : respond - {resp}')
              
            #checker 
            if message.channel.id == int(getConfig()['baseChannelID']):
                async for msg in message.channel.history(limit=10):
                    if message.id == msg.id:
                        content = msg.content
                        title = description = author = footer = ''
                        for embed in msg.embeds:
                            embedInfo = (embed.to_dict())
                            title = embedInfo['title'] if 'title' in embedInfo else 'nil'
                            description = embedInfo['description'] if 'description' in embedInfo else 'nil'
                            author = embedInfo['author']['name'] if 'author' in embedInfo else 'nil'
                            footer = embedInfo['footer']['text'] if 'footer' in embedInfo else 'nil'
                        if author == client.user.name and f'Travelled to Arena [{getConfig()["izziLocNumber"]}-{izziFloor["currentFloor"]+1}]' in title and izziAutoFloor_ == "on":
                            izziFloor['currentFloor'] += 1
                            data = getConfig();data['izziFloorNumber']+=1;setConfig(data)
                        elif content.strip() == f"Summoner **{client.user.name}**, you have cleared this zone! Use ``zone n`` to move to the next one" and izziAutoFloor_ == "on"::
                            izziFloor['currentFloor'] = 1
                            data = getConfig();data['izziFloorNumber']=1;data['izziLocNumber']+=1;setConfig(data)
                            await changeLoc() 
                        elif author == client.user.name and 'Defeated' in title and izziAutoFloor_ == "on"::
                            if izziAutoFloor.is_running():
                                izziAutoFloor.cancel()
                            await notificateDefeat('Izzi' , token)
                        elif author == client.user.name and 'Error' in title and 'You do not have enough mana to proceed!' in description and izziAutoFloor_ == "on"::
                            if izziAutoFloor.is_running():
                                izziAutoFloor.cancel()
                            await asyncio.sleep(1800)
                            if not izziAutoFloor.is_running():
                                izziAutoFloor.start()
                          

        except Exception as e:
            print(errorColour + f'{e}') 

try:
    server.keep_alive()
    client.run(token, bot=False)
except Exception as e:
    print(errorColour + f'{e}')