import os
import json

files = os.listdir()

def getConfig():
    with open('config.json' , 'r' , encoding='utf-8') as c:
        return json.load(c)

def setConfig(data):
    with open('config.json' , 'w' , encoding='utf-8') as c:
        json.dump(data , c)

if 'config.json' not in files:
    with open('config.json' , 'w' , encoding='utf-8') as f:
        f.write('''{
    "prefix": "->", 
    "controllerAccountID": "",
    "token": "", 
    "spamTokens" : [],
    "anigameSniper": "", 
    "izziSniper": "", 
    "latency": "0", 
    "respond": "", 
    "baseChannelID": "",
    "baseChannelAnigamePrefix": ".", 
    "baseChannelIzziPrefix": "iz ", 
    "anigameLottery": "", 
    "anigameHourly": "", 
    "anigameBTALL": "",
    "izziLottery": "",
    "izziHourly": "",
    "izziBTALL": "",
    "notificationChannelID": ""
}''')

configdat = getConfig()
for i in list(configdat.keys()):
    if i == 'anigameSniper' \
    or i == 'izziSniper' \
    or i == 'respond' \
    or i == 'anigameLottery'\
    or i == 'anigameHourly'\
    or i == 'anigameBTALL'\
    or i == 'izziLottery'\
    or i == 'izziHourly'\
    or i == 'izziBTALL':
        value = input(f'{i} (on/off) : ')

    elif i== 'latency':
        value = input(f'{i} (number) : ')

    elif i== 'spamTokens':
        much=int(input('how many spamTokens do you want to enter : '))
        value = []
        for j in range(much):
            stoken = input(f'spamToken {j+1} : ')
            value.append(stoken.strip())    
    else:
        value=input(f'{i} : ')
    
    configdat[i] = value
setConfig(configdat)
input('completed! , press enter to continue ')