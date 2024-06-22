import discord
from discord import SyncWebhook
import datetime
from utils.handler import handler

def check_for_new(last_time, key, webhook_url):
  out = handler(key)
  webhook = SyncWebhook.from_url(webhook_url)
  for item in out['data']['issues']['edges']:
    year = int(item['node']['createdAt'][:4])
    month = int(item['node']['createdAt'][5:7])
    day = int(item['node']['createdAt'][8:10])
    hour = int(item['node']['createdAt'][11:13])
    min = int(item['node']['createdAt'][14:16])
    sec = int(item['node']['createdAt'][17:19])
    ctddt = datetime.datetime(year, month, day, hour, min, sec)
    isNew = False
    if ctddt > last_time:
      isNew = True
    last_time = datetime.datetime.now()
    if isNew:
      webhook.send("**NEW Issue Alert**: \'" + item['node']['title'] + "\', assigned to " + item['node']['assignee']['name'])
   

def send_urgent(key, webhook_url):
    out = handler(key)
    webhook = SyncWebhook.from_url(webhook_url)
    for item in out['data']['issues']['edges']:
      if item['node']['priority'] == 1 and item['node']['state']['name'] == 'Todo':
        year = int(item['node']['createdAt'][:4])
        month = int(item['node']['createdAt'][5:7])
        day = int(item['node']['createdAt'][8:10])
        hour = int(item['node']['createdAt'][11:13])
        min = int(item['node']['createdAt'][14:16])
        sec = int(item['node']['createdAt'][17:19])
        ctddt = datetime.datetime(year, month, day, hour, min, sec)
        curr = datetime.datetime.now()
        delta = curr - ctddt

        webhook.send("**URGENT ISSUE ALERT**: " + "Issue \'" + item['node']['title'] + "\' with id " + item['node']['id'] + " has NOT YET BEEN ACTED ON! This issue has already been up for " + str(delta/datetime.timedelta(hours=1)) + " hours!")
        webhook.send("**"+item['node']['assignee']['name'] + "**, please get to it NOW!")

def send_high(key, webhook_url):
    out = handler(key)
    webhook = SyncWebhook.from_url(webhook_url)
    for item in out['data']['issues']['edges']:
      if item['node']['priority'] == 2 and item['node']['state']['name'] == 'Todo':
        year = int(item['node']['createdAt'][:4])
        month = int(item['node']['createdAt'][5:7])
        day = int(item['node']['createdAt'][8:10])
        hour = int(item['node']['createdAt'][11:13])
        min = int(item['node']['createdAt'][14:16])
        sec = int(item['node']['createdAt'][17:19])
        ctddt = datetime.datetime(year, month, day, hour, min, sec)
        curr = datetime.datetime.now()
        delta = curr - ctddt
        webhook.send("**High Priority Issue Reminder**: " + "Issue \'" + item['node']['title'] + "\' with id " + item['node']['id'] + " has not yet been acted on! This issue has already been up for " + str(delta.days) + " days!")
        webhook.send("**"+item['node']['assignee']['name'] + "**, we're counting on you to get this done!")
    
      
