from bot import bot, settings, db
from bot.command import log

async def on_ready():
    #db.load()
    await log().send('[System] Bot started')
    await log().send(f'[System] Admin commands - {str(settings["admin"])}')
bot.event(coro=on_ready)


async def on_member_join(member):
    guild = member.guild

    async for entry in guild.audit_logs(limit = 100):
        if entry.action == discord.AuditLogAction.invite_create:
            await ctx.send(f'{entry.user} создал приглашение: {entry.target}')

bot.event(coro=on_member_join)