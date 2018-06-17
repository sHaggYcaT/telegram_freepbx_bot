#!/usr/bin/env python3
import socket
import threading
from time import gmtime, strftime
import pickle
import telegram
#import telegram.ext
#import telegram.error
import logging
import sys
import configparser
from io import BytesIO
 
 
def ConfigSectionMap(section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1
 
 
def bot_start():
    global bot
    bot = telegram.Bot(telegram_settings["token"])
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None
    bot_message("bot starts!")

def testm(MessageText):
    print(MessageText)
 
def bot_message(MessageText):
    bot.send_message(chat_id=telegram_settings["chat_id"], text=MessageText)
 
def bot_voice_message(VoiceMessage):
    bio = BytesIO(VoiceMessage)
    bio.name = 'voicemail.wav'
    bot.send_voice(chat_id=telegram_settings["chat_id"], voice=bio)
 
 
def connection_worker(conn,addr):
    returndata = b''
    while True:
        data = conn.recv(1024)
        if not data:
            break
        returndata = returndata+data
    #filename=strftime("%Y_%m_%d____%H_%M_%S", gmtime()) + '.wav'
    #wavfile = open(filename,'wb')
    #try to un-pickle touple, and use their elements
    #try:
    touple_pickled=pickle.loads(returndata)
    #wavfile.write(touple_pickled[0])
    #print(touple_pickled[1])
    #print(type(touple_pickled[1]))
    #print(type(touple_pickled[0]))
    bot_message(str(touple_pickled[1]))
    #bot_message(filename)
    #testm(filename)
    bot_voice_message(touple_pickled[0])
    #except:
    #    pass
 
 
 
def workers_create(sock):
    while True:
        conn,addr = sock.accept()
        print('connected:', addr)
        worker = threading.Thread(target=connection_worker,args=(conn,addr))
        worker.start()
 
 
 
 
def main():
    #bind to socket
    sock = socket.socket()
 
    try:
        sock.bind((network_settings["bind_ip"],int(network_settings["bind_port"])))
        sock.listen(10)
    except:
        print("cant bind to socket!")
        sys.exit(1)
    #using dedicated thread, run worker creator
    #bot_start(telegram_settings['token'],telegram_settings['chat_id'])
    bot_start()
#    bot_message("testmessage from main!")
    worker_creator_thread = threading.Thread(target=workers_create(sock))
    worker_creator_thread.start()
 
 
 
#use ini config to determinate Network settings
config = configparser.ConfigParser()
 
try:
    config.read('/etc/freepbxbot.ini')
    network_settings = ConfigSectionMap('Network')
    telegram_settings = ConfigSectionMap('Telegram')
 
except:
    print('cant read config!')
    sys.exit(1)
 
if __name__ == "__main__":
    main()


