Isimport nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix='/', intents=nextcord.Intents.all())
guild_id = None

@bot.event
async def on_member_join(member: nextcord.Member):
    # get the welcome channel
    welcome_channel = await bot.fetch_channel(1040001321308270793)

    # send a welcome message as an embed
    embed = nextcord.Embed(title=f'Welcome to the server, {member.name}!', description='We\'re excited to have you here!', color=0x008080)
    await welcome_channel.send(embed=embed)


bot.run('MTA2NTU4NjEwMjY1Nzg4ODI1Ng.G8g-p3.zrrDXf4Rqkg8n_Yzm0Sz7amVBnOwLKPcAmIhQ0')
