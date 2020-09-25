# By @Triggheratomale || #TriggheratoSources

from pyrogram.session import session

from userbot import app
from userbot import bot
from userbot import load_modules
from userbot import ClearWindow

from pyrogram import idle

session.Session.notice_displayed = True
ClearWindow()

# CARICA FORTE
print('Carico i moduli...\n')

load_modules()

# STARTATO
bot.start()
app.start()

# AVVIA STUPRI PESANTI (ANDATE SU MAIN.PY NELLA CARTELLA DEI MODULES PER SEGUIRE LO STUPRO)
print('\nUserBot avviato correttamente!')

# IDLA
idle()
