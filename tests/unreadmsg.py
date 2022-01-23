import requests
token = ''
messageID = ''
channelID = ''
url = f'https://discord.com/api/v9/channels/{channelID}/messages/{messageID}/ack'
r = requests.post(url , headers={"authorization":token} , json={"manual":True , "mention_count":1})
print(r)