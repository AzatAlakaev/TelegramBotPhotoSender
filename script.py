import random
import glob
import shutil
import telebot
from telebot import apihelper

token = 'token'  
pics = glob.glob('/home/user/pic/*')
chat_id = '@id'  # ID паблика

if len(pics) == 0:
    print('Нет изображений для постинга')
    exit()

pic2post = random.choice(pics)
photo = open (pic2post , 'rb')
bot = telebot.TeleBot(token)

apihelper.proxy = {'https' : 'socks5h://ip:port'} # обход блокировки если нужно

bot.send_photo (chat_id, photo)
shutil.move(pic2post, '/home/user/backup/')   #копируем в папку backup пикчу которую запостили
print('success!')
