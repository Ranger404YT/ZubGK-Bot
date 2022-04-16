from bot import bot, settings

def guest_add():
    return 'pass'

def no_command(command_type=None):
    if command_type == 1:
        return f"NotFoundError: Bot can't found command"
    elif command_type != None:
        return f'+admin {command_type} command'
    else:
        return f"NotFoundError: Bot can't found command_type"

def chack_admin_command(command_type, command):
    if command_type == 'quest':
        if command == 'add':
            return guest_add()
        elif command == None:
            return no_command(command_type)
        else:
            return no_command(1)
    else:
        return no_command()

@bot.command()
async def admin(ctx,command_type=None,command=None):
    if str(ctx.message.author)==str(bot.owner_id) or str(ctx.message.author) in settings['admins']:
        if command_type != None:
            await ctx.send(chack_admin_command(command_type,command))
        else:
            await ctx.send('+admin command_type command')
    else:
        await ctx.send("You are don't have permission!")