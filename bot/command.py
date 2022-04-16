from bot import bot, db, settings
from logics import rand_ball, Logs, Quest
import discord

color = 0xffff00

quest = Quest(db)

log_use = Logs()
log = log_use.log

@bot.command()
async def инвайт(ctx):
    member = ctx.message.author
    guild = member.guild
    async for entry in guild.audit_logs(limit=1):
        if entry.action == discord.AuditLogAction.invite_create:
            await ctx.send(f'{member.mention} создал приглашение: <{entry.target}>')

def взять(quest,embed):
    if quest==None:
        embed.description = 'Введите название квеста'
    else:
        pass

@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def hello(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Hello, {author.mention}!') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.

@bot.command()
async def донат(ctx):
    embed = discord.Embed(color=color,title='Донат')  # Создание Embed'a
    embed.description = 'qiwi: ITUTI762'
    await ctx.send(embed=embed)

@bot.command()
async def квест(ctx,message=None,user_quest=None):
    await log().send(f'{ctx.message.author}: Использовал команду +квест')
    if db.check(ctx.message.author,1):
        embed = discord.Embed(color=color,title='Квесты')  # Создание Embed'a
        if message == None:
            geted = quest.get_quest(member=ctx.message.author)
            quests = 'Квесты:\nНазвание - Награда\n'
            for i in range(len(geted)): quests+=f'{geted[i][1]} - {geted[i][4]}\n'
            embed.description = f'Участник:\n{geted[0][0]}\nКоличество: {len(geted)}\n{quests}'
        else:
            if len(message)==5:
                command=''
                for i in range(5): command+=message[i]
                if command == 'взять':
                    взять(user_quest,embed)
                else:
                    geted = quest.get_quest(member=ctx.message.author,quest=message)
                    if geted == None:
                        embed.description = 'Квеста с таким названием у вас нет!'
                    else:
                        embed.description = f'Участник:\n{geted[0][0]}\nКвест:\nНазвание: {geted[0][1]}\nНаграда: {geted[0][4]}'

    else:
        embed = discord.Embed(color=color,title='Профиль')
        embed.description = 'Вы не зарегистрированны введите +профиль для регистрации'
    await ctx.send(embed=embed)

@bot.command()
async def профиль(ctx):
    await log().send(f'{ctx.message.author}: Использовал команду +профиль')
    info=db.load_member(ctx.message.author)
    embed = discord.Embed(color=color,title='Профиль')  # Создание Embed'a
    if info != None:
        embed.description = f'Профиль участника:\n{info[0]}\nБаланс: {info[1]}'
    else:
        embed.description = 'Вы были зарегестрированы, введите команду заного!'
    await ctx.send(embed=embed)

@bot.command()
async def ball(ctx, message=None):
    if message == None:
        embed = discord.Embed(color=color)  # Создание Embed'a
        embed.description = 'Пожалуйста введите вопрос!'
    else:
        embed = discord.Embed(color=color,title=message)  # Создание Embed'a
        embed.description = rand_ball()
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    await log().send(f'{ctx.message.author}: Использовал команду +help')
    embed = discord.Embed(color=color,title='Help')  # Создание Embed'a
    embed.description = ('Не настроенно')
    await ctx.send(embed=embed)

@bot.command()
async def creator(ctx):
    await ctx.send(bot.owner_id)

@bot.command()
async def admins(ctx):
    if settings['admin'] == True:
        _send = 'Админы:\n'
        for namber in range(len(settings['admins'])): _send+=f'{settings["admins"][namber]}\n'
        await ctx.send(_send)
    else:
        await ctx.send('Взаимодействие администрации отключено!')