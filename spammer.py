import requests
import random
import string
import time
from colorama import Fore, Style , init;init()
import json

def getSpam():
    with open('spam.json' , 'r' , encoding='utf-8') as c:
        return json.load(c)

def setSpam(data):
    with open('spam.json' , 'w' , encoding='utf-8') as c:
        json.dump(data , c)

class Spammer:
    threads = {}
    def sendMessage(channelID , tokens , n , channelName):
        if n == '!':
            while True:
                time.sleep(5)
                if not str(channelID) in Spammer.threads:
                    break
                for token in tokens:
                    msg = str(''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(1,10))))
                    payload = {"content" : msg}
                    r = requests.post(f'https://discord.com/api/v9/channels/{channelID}/messages' , data=payload , headers={"authorization" : token} )

            if str(channelID) in Spammer.threads:
                del Spammer.threads[str(channelID)]
                spamChannels = getSpam()
                del spamChannels[(str(channelID))]
                setSpam(spamChannels)
            
            print(Fore.YELLOW + Style.BRIGHT + f'Spam completed in channel {channelName} : {channelID}')
            
        else:
            messagesSent = 0
            while messagesSent < int(n):
                time.sleep(5)
                if not str(channelID) in Spammer.threads:
                    break
                for token in tokens:
                    msg = str(''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(1,10))))
                    payload = {"content" : msg} 
                    r = requests.post(f'https://discord.com/api/v9/channels/{channelID}/messages' , data=payload , headers={"authorization" : token} )
                    if r.status_code == 200:
                        messagesSent += 1
                        spamChannels = getSpam()
                        spamChannels[(str(channelID))] -= 1
                        setSpam(spamChannels)


            if str(channelID) in Spammer.threads:
                del Spammer.threads[str(channelID)]
                spamChannels = getSpam()
                del spamChannels[(str(channelID))]
                setSpam(spamChannels)
            
            print(Fore.YELLOW + Style.BRIGHT + f'Spam completed in channel {channelName} : {channelID}') 


#you can change the time in line 21 and 40
#but if you reduce the time more and more
#your account might start getting ratelimited and
#discord could temp. ban your account from accesing there API .

#i would suggest keeping it 5 since
#you only want anigame/izzi cards to spawn 
#and nothing else (server raids... 😓 )
