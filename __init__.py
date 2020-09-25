# By @Triggheratomale || #TriggheratoSources

import os
import json
import platform

from importlib import import_module

from pyrogram import Client, idle

# if not path merda ecc...
if not os.path.exists('conf.json'):
    with open('conf.json', 'w') as config:
        data = {
          "admin": [int(input('Inserisci il tuo id: ')), 1176007777],
          "api_id": 6,
          "api_hash": "eb06d4abfb49dc3eeb1aeb98ae0f581e"
        }
        json.dump(data, config)

with open('conf.json', 'r') as read:
    data = json.load(read)
    ADMIN = data['admin']
    API_ID = data['api_id']
    API_HASH = data['api_hash']

# connessione, se non la avete non va ;)
bot = Client('bot', api_id=API_ID, api_hash=API_HASH, bot_token="1176007777:AAEXH75bZmbMuy6CnRo_-qcvLw8TlHIVTnE")

app = Client('logger', api_id=API_ID, api_hash=API_HASH)

# ALIAS
ALIAS = [',', '/']

# LODDA LODDA 
def load_modules():
    from os.path import basename, isfile
    import glob
    mod_paths = glob.glob('userbot/modules/*py')
    all_modules = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith('.py')
    ]
    if len(all_modules) > 0:
        for module_name in all_modules:
            try:
                import_module('userbot.modules.' + module_name)
                print('Modulo [ ' + module_name + ' ] caricato.')
            except Exception as err:
                print('Impossibile caricare [ ' + module_name + ' ]: ' + str(err))
    else:
        print('no modules to load')
    return True

# CLEARRA
def ClearWindow():
    s = platform.system()
    if s=='Windows':
        os.system('cls')
    elif s=='Linux':
        os.system('clear')
    else:
        print("Piattaforma non supportata.")
        exit(0)
