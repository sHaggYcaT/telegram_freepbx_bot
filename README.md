# Telegram FreePBX bot. Sends voicemail messages to the telegram.

## Description

Do you want to get your Asterisk/FreePBX voicemails in the Telegram instead of email or webinterface? So, this bot can do this!
Technically, the product are list of following components: 

* systemd background script, contains bot and python library
* client to the systemd script, which can parse FreePBX emails
* systemd config, which supports virtualenv
* ini file (script config)
* bash wrapper (helps start client using virtualenv)
* README.md file - this file
* python virtualenv directory
* python-telegram-bot module from pip and it's dependencies

## Installation

This is bot for FreePBX VoIP server and Telegram. So, you should have FreePBX installation and Telegram account.
I'll write ansible scenario to install bot to the FreePBX servers. In future. Maybe ;) Or maybe not (If I'll be too lazy) 
Today you should install bot by hands. I recommend you:

* create a folderfolder in /opt/, f.e. /opt/telegram_voicemailbot/
* create a subfoler /opt/telegram_voicemailbot/scripts, and put there all files from github
* create a subfolder /opt/telegram_voicemailbot/VirtualEnv
* create a virtualenv in latest folder
* create a simlink  /usr/lib/systemd/system/freepbxtgbot.service to your systemd scenario
* create a simlink /etc/freepbxbot.ini to your ini file
* edit your ini file (add your custom network options, Telegram token, and chat room's id)


##TODO

* add several commands, for example */status* command (currently uses in production server, and monitoring by Prometherius, so, supporting  commands  not requires)
* rewrite systemd condig
* write ansible role to install bot to the FreePBX server
* add unit tests
* (maybe) docker app (but you can pack only server, and should install client script to the FreePBX server anyway. Maybe it's not really requires)


