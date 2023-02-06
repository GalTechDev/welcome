from system.lib  import *

Lib = Lib_UsOS()

welcome_message = """
Bienvenue {}, dans le serveur

Je t'invite à choisir ta classe dans le salon <#812841349610471444>

Si tu as la moindre question, n'hésite pas a demander de l'aide
"""

# -------------------------------- Event --------------------------------------

@Lib.event.event()
async def on_member_join(ctx):

    channel = ctx.guild.get_channel(724498186521280573)
    embed = discord.Embed(title="Bienvenu!", description=welcome_message.format(ctx.mention), color=discord.Color.yellow())
    embed.set_thumbnail(url="https://i.ibb.co/Mc4dYdw/team-plante-verte.png")
    await channel.send(embed=embed)


@Lib.event.event()
async def on_member_remove(ctx):

    channel = ctx.guild.get_channel(724498186521280573)
    embed = discord.Embed(title=f"Oh non! {ctx.name} nous a quitté!", color=discord.Color.yellow())
    await channel.send(embed=embed)

# --------------------------------- Modal ------------------------------------- 

# --------------------------------- View --------------------------------------

# --------------------------------- Menu --------------------------------------
async def edit_welcome(ctx):
    pass

async def edit_bye(ctx):
    pass

@Lib.app.config()
async def config(ctx: discord.Interaction):
    if not ctx.response.is_done():
        await ctx.response.send_message(embed=discord.Embed(title="Chargement..."), ephemeral=True)
    embed=discord.Embed(title=":gear:  Welcome Message Config")
    await ctx.edit_original_response(embed=embed)
