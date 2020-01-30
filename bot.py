import sys
import time
import random
import datetime
import telepot
from picamera import PiCamera

accepted_users = [] #Here you must enter the chat id you want to allow acces to the bots (int)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: ' + command + 'from chat ID: ' + str(chat_id))
    
    if chat_id in accepted_users:
        if command == 'foto':
            camera.capture('/home/pi/Desktop/image.jpg')
            photo = open('/home/pi/Desktop/image.jpg', 'rb')
            bot.sendPhoto(chat_id, photo)
    
        #elif: command == 'whatever': #Here you can add more funcions

camera = PiCamera()

bot = telepot.Bot('BotToken')
bot.message_loop(handle)
print('Bot boot\'s...')
bot.sendMessage(275911827, 'Bot boot\'s')
while 1:
     time.sleep(2) #It accepts messages for each 2 seconds. This is editable, I used
                   #2 secs mainly beacuse it's the time the Pi camera needs between two pics.