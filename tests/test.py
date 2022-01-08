import requests
chid=''
auth = ''
url = "https://discord.com/api/v9/interactions"
headers = {
        'authorization' : auth
    }

r = requests.get(f'https://discord.com/api/v9/channels/{chid}/messages?limit=50' , headers=headers)
print(r)