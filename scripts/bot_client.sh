#!/bin/bash

ATTACHMENT=$1

source  /opt/telegram_voicemailbot/VirtualEnv/bin/activate


/opt/telegram_voicemailbot/scripts/bot_client.py $ATTACHMENT
