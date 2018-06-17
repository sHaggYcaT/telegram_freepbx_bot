#!/bin/env python3

import email
import sys
import fileinput
import socket
import pickle
#import own module
import bot_daemon
#import os


mailtext = ''
for line in sys.stdin:
    mailtext = mailtext + line

try:
    msg = email.message_from_string(mailtext)
    #print(len(msg.get_payload()))
    attachment = msg.get_payload()[1]
    attachment2 = msg.get_payload()[0]
except:
    sys.exit(1)
    print("cant parse!")

print(10*"-")
print(attachment.get_content_type())
print(attachment2.get_content_type())

# uncomment to debug

# open('attachment.wav','wb').write(attachment.get_payload(decode=True))
# open('attachment1.txt','wb').write(attachment2.get_payload(decode=True))
#wavdata = binary_file.read(write(attachment.get_payload(decode=True))

wavdata = attachment.get_payload(decode=True)

# uncomment to debug
#print(wavdata)
#wavfile = open('att.wav','wb')
#wavfile.write(wavdata)
#mp3data = os.system(lame -V 5 

data4picked = (wavdata,attachment2)
pickleddata = pickle.dumps(data4picked)

sock = socket.socket()
sock.connect((bot_daemon.network_settings["bind_ip"],int(bot_daemon.network_settings["bind_port"])))

sock.send(pickleddata)

sock.close()
