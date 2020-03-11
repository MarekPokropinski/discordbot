import discord
from discord import *
from discord.ext.commands import Bot
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import textwrap
import os

CLIENT_ID = os.environ['CLIENT_ID']
PATH = "out.png"
BOT_PREFIX = ("%")

TOKEN = os.environ['TOKEN']


client = Bot(command_prefix=BOT_PREFIX)

meme_config = {
    "joker" : {
        "filename": "joker.jpg",
        "positions": [(1459, 187), (1209, 1395)],
        "font_size" : 100,
        "font_color":(255, 255, 255)
        },
    "tablica": {
        "filename": "tablica.jpg",
        "positions": [(73, 687)],
        "font_size" : 70,
        "font_color":(30, 30, 30),
        "text_wrap" : 20
    },
    "lotr": {
        "filename": "lotr.jpg",
        "positions": [(561, 147), (605,1000)],
        "font_size" : 60,
        "font_color":(255, 255, 255)
    }

}



@client.command()
async def meme(ctx,*args):
    await ctx.send("I'm on it boss...")

    meme = args[0]
    config = meme_config[meme]

    temp = " ".join(args[1:])
    text = temp.split(':')

    font = ImageFont.truetype("font.ttf", config["font_size"])

    
    image_file = config["filename"]
    im1 = Image.open(image_file)

    draw = ImageDraw.Draw(im1)
    for i, txt in enumerate(text):
        if "text_wrap" in config:
            for j, line in enumerate(textwrap.wrap(txt, width=config["text_wrap"])):
                pos = config["positions"][i]
                pos = (pos[0],pos[1] + j * config["font_size"])
                draw.text(pos, line, config["font_color"], font=font)
        else:
            draw.text(config["positions"][i], txt, config["font_color"], font=font)

    draw = ImageDraw.Draw(im1)

    im1.save(PATH)    
    await ctx.send("Your meme:", file=discord.File(PATH))



client.run(TOKEN)
