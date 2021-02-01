#DISCORD.PY IMPORTS
import discord
from discord.ext import commands

#ESV API IMPORTS
import re
import requests
import random

#ESV API STUFF
API_KEY =
API_URL =

def get_passage(book, chapter, verse):

    return str(book) + '%s:%s' % (chapter, verse)


def get_esv_text(passage):
    params = {
        'q': passage,
        'indent-poetry': False,
        'include-headings': False,
        'include-footnotes': False,
        'include-verse-numbers': False,
        'include-short-copyright': False,
        'include-passage-references': False
    }

    headers = {
        'Authorization': 'Token %s' % API_KEY
    }

    data = requests.get(API_URL, params=params, headers=headers).json()

    text = re.sub('\s+', ' ', data['passages'][0]).strip()

    return '%s – %s' % (text, data['canonical'])


def render_esv_text(data):
    text = re.sub('\s+', ' ', data['passages'][0]).strip()

    return '%s – %s' % (text, data['canonical'])


client = commands.Bot(command_prefix='.')

QUERY = []


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('ESV.org'))
    print("Welcome Mr. Stark")

@client.command()
async def bsearch(ctx, arg, arg2, arg3):
    text = get_esv_text(get_passage(arg, arg2, arg3))
    await ctx.send(text)

#CLIENT.RUN GOES HERE
