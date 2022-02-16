import requests 
import json

buttonurl = "https://discord.com/api/v9/interactions"

def getcustomID(channelID , messageID , token):
    buttons = {}
    headers = {
        'authorization' : token
    }
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
    
def clickButton(guildID , channelID , messageID , token , click):
    headers = {
        'authorization' : token
    }
    buttons = getcustomID(channelID , messageID , token)
    for i in buttons:
        if i.strip() == click:
            data = {
                "type": 3,
                "session_id": ' ',
                "guild_id": guildID,
                "channel_id": channelID,
                "message_id": messageID,
                "application_id": "571027211407196161",
                "data": {
                    "component_type": 2,
                    "custom_id": buttons[i] 
                    }
                }
            r = requests.post(buttonurl, json = data, headers = headers)
            return(r.status_code)

def add_reaction(channelID , messageID , emoji , token):
    headers = {
        'authorization' : token
    }
    r = requests.put(
        f'https://discord.com/api/v9/channels/{channelID}/messages/{messageID}/reactions/{emoji}/%40me' , headers=headers
    )
    return(r.status_code)

def makeUnread(channelID,token):
    headers = {
        'authorization' : token
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelID}/messages?limit=2' , headers=headers)
    jsondat = json.loads(r.text)
    messageID = jsondat[-1].get('id')
    url = f'https://discord.com/api/v9/channels/{channelID}/messages/{messageID}/ack'
    r = requests.post(url , headers={"authorization":token} , json={"manual":True , "mention_count":0})
    return(r.status_code)
