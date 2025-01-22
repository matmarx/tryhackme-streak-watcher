#!/usr/bin/python3
import os
from time import gmtime, strftime
import requests
import json
from datetime import datetime

# VARIABLES TO DEFINE
username = "you-thm-username" #Tryhackme username
start_date = datetime.strptime("2020-04-27", "%Y-%m-%d") #Enter the date when you started doing the streak
discord_webhook_url = "https://discord.com/api/webhooks/___/___" #Discord webhook

url = f"https://tryhackme.com/api/v2/public-profile?username={username}"
response = requests.get(url)
data = response.json()

# Extract the streak value
if response.status_code == 200:
    data = response.json()
    streak = data["data"]["streak"]
else:
    print("Failed to fetch data from TryHackMe API")
    streak = 0
print("streak: ",streak)

# Calculate days since a specific date
current_date = datetime.now()
days_since = (current_date - start_date).days
print("days: ",days_since)

def notify_discord(msg):
    now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    message = str(msg) + '\n'
    message += '## ' + str(now)+ '\n'
    message += '### Here are some answers for: https://tryhackme.com/r/room/blockroom' + '\n'
    message += '- `mrealman`' + '\n'
    message += '- `Blockbuster1`' + '\n'
    message += '- `THM{SmB_DeCrypTing_who_Could_Have_Th0ughT}`' + '\n'
    message += '- `eshellstrop`'+ '\n'
    message += '- `3f29138a04aadc19214e9c04028bf381`' + '\n'
    message += '- `THM{No_PasSw0Rd?_No_Pr0bl3m}`'

    payload = {"content": message}
    response = requests.post(discord_webhook_url, json=payload)
    response.raise_for_status()

if __name__ == '__main__':
	if streak == days_since:
		print("streak ok")
	else:
		msg="# THM Streak will drop, don't do that"
		notify_discord(msg)
