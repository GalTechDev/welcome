from understar.system import lib
import discord
from PIL import Image, ImageDraw, ImageOps, ImageFont
Lib = lib.App()

welcome_message = """
Bienvenue {}, dans le serveur

Si tu as la moindre question, n'hésite pas a demander de l'aide
"""



# -------------------------------- Event --------------------------------------

@Lib.event.event()
async def on_member_join(member: discord.Member):
    channel = member.guild.system_channel
    embed = discord.Embed(title="Bienvenu!", description=welcome_message.format(member.mention), color=discord.Color.yellow())
    embed.set_thumbnail(url=member.guild.icon.url)
    await channel.send(embed=embed)
    #await send_banner(member)

@Lib.event.event()
async def on_member_remove(member: discord.Member):

    channel = member.guild.system_channel
    embed = discord.Embed(title=f"Oh non! {member.name} nous a quitté!", color=discord.Color.yellow())
    await channel.send(embed=embed)

# --------------------------------- Type --------------------------------------

async def send_banner(member: discord.Member):
    # Ouvre l'image template.png
    image = Image.open(Lib.save.get_full_path(name='template.png'))
    draw = ImageDraw.Draw(image)
    
    # Télécharge l'avatar de l'utilisateur qui a rejoint le serveur
    avatar_data = await member.avatar.read()
    Lib.save.write(name=f"{member.id}_avatar.png", path="avatar", data=avatar_data, binary_mode=True)

    # Ouvre l'avatar téléchargé
    avatar = Image.open(Lib.save.get_full_path(name=f"{member.id}_avatar.png", path="avatar")).convert('RGBA')

    # Redimensionne l'avatar à la taille souhaitée
    avatar = avatar.resize((200, 200), Image.ANTIALIAS)
    mask = Image.new('L', avatar.size, 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((0, 0, avatar.width, avatar.height), fill=255)

    # Application du masque à l'avatar
    avatar = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
    avatar.putalpha(mask)

    # Calcule les coordonnées du centre de l'image
    center_x = (image.width - avatar.width) // 2
    center_y = (image.height - avatar.height) // 2

    # Ajoute l'avatar au centre de l'image
    image.paste(avatar, (center_x, center_y), avatar)
    
    # Ajout du nom de l'utilisateur en bas de l'image
    font = ImageFont.truetype('arial.ttf', 24)
    text_width, text_height = draw.textsize(member.name, font=font)
    text_x = (image.width - text_width) // 2
    text_y = image.height - text_height - 10
    draw.text((text_x, text_y), member.name, font=font, fill=(255, 255, 255))

    # Enregistre l'image modifiée avec le nom de l'utilisateur
    image.save(f'{member.id}_banner.png')

    # Envoie l'image sur le canal de bienvenue
    channel = member.guild.system_channel
    if not channel:
        return
            
    await channel.send(file=discord.File(f'{member.id}_banner.png'))

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
