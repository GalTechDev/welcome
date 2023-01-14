from system.lib  import *

Lib = Lib_UsOS()

welcome_message = """
Bienvenue {}, dans le serveur

Je t'invite à choisir ta classe dans le salon #roles

Si tu as la moindre question, n'hésite pas a demander de l'aide
"""

@Lib.event.event()
async def on_member_join(ctx):

    channel = ctx.guild.get_channel(724498186521280573)
    embed = discord.Embed(title="Bienvenu!", description=welcome_message.format(ctx.mention), color=discord.Color.blue())
    embed.set_thumbnail(url="https://i.ibb.co/Mc4dYdw/team-plante-verte.png")
    await channel.send(embed=embed)


@Lib.event.event()
async def on_member_remove(ctx):

    channel = ctx.guild.get_channel(724498186521280573)
    embed = discord.Embed(title=f"Oh non! {ctx.name} nous a quitté!", color=discord.Color.blue())
    await channel.send(embed=embed)
