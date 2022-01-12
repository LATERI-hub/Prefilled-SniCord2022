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
    "token": "", 
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
    "izziBTALL": ""
}''')

configdat = getConfig()
for i in configdat:
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
    
    else:
        value=input(f'{i} : ')
    
    configdat[i] = value
setConfig(configdat)
input('completed! , press enter to continue ')
