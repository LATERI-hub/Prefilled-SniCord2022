import requests 
import json

auth = ''
url = "https://discord.com/api/v9/interactions"
headers = {
        'authorization' : auth
    }

def getcustomID(channelID , messageID):
    buttons = {}
    r = requests.get(f'https://discord.com/api/v9/channels/{channelID}/messages?limit=50' , headers=headers)
    jsondat = json.loads(r.text)
    for message in jsondat:
        if message['id'] == messageID:
            for components in message['components']:
                for component in components['components']:
                    if 'label' in component:
                        buttons[ component['label'] ] = component['custom_id'].strip()
                    if 'emoji' in component:
                        buttons[ component['emoji']['name'] ] = component['custom_id'].strip()
    
    return buttons
    
def clickButton(guildID , channelID , messageID):
    buttons = getcustomID(channelID , messageID)
    for i in buttons:
        doit = input(str(i) + '   ').lower()
        if doit == 'y':
            data = {
                "type": 3,
                "guild_id": guildID,
                "channel_id": channelID,
                "message_id": messageID,
                "application_id": "XXX",
                "data": {
                    "component_type": 2,
                    "custom_id": buttons[i] 
                    }
                }
            r = requests.post(url, json = data, headers = headers)
            print(r)
            break

clickButton('' , '' , '')