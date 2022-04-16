from discord.ext import commands
from bot.config import settings

bot = commands.Bot(command_prefix=settings['prefix'],help_command=None,owner_id=settings['owner'])



from db import DB

db_obj = {}

db = DB('bot.db',bot,db_obj)

from logics import Logs

from bot import command, event
if settings['admin'] == True:
    from bot import admin
    print('[LOG] Admin commands - True')
