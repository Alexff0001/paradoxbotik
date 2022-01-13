import discord
from discord import Embed

from discord.ext import bot
from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord_components import Button, ButtonStyle, Select, SelectOption, DiscordComponents

import sqlite3
import asyncio
import datetime

intents = discord.Intents.default()
intents.members = True

bot = bot.Bot(command_prefix = '!', case_insensitive = True, intents = discord.Intents.all())
bot.remove_command('help')


links = ['www', 'https://']

@bot.event
async def on_message(message):
    await bot.process_commands(message)

    msg = message.content.lower()

    if msg in links:
        await message.delete()


@bot.event
async def on_ready():
    DiscordComponents(bot)
    bot.ready = True
    embed = discord.Embed(description = '**Бот работает!**')
    embed.timestamp = datetime.datetime.utcnow()
    await bot.change_presence(activity=discord.Game(name="Paradox Role Play"))
    await bot.get_channel(930825093238652938).send(embed = embed)


@bot.command(aliases = ['тест'])
async def test(ctx):
	await ctx.reply(embed = discord.Embed(description = 'работаю'))


@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, id = 922190850589622345)
    embed1 = discord.Embed(
        title = 'Пользователь присоединился',
        description = f'{member.mention} {len(list(member.guild.members))} по счёту на сервере\nАккаунт создан ' + f"{member.created_at.strftime('%d %B %Yг.')}",
        color = discord.Color.from_rgb(244, 127, 255)
        )
    embed1.set_author(name = f'{member}', icon_url = member.avatar_url)
    embed1.set_footer(text = f'ID: {member.id}')
    embed1.timestamp = datetime.datetime.utcnow()
    embed = discord.Embed(
        description = '__Добро пожаловать на официальный дискорд сервер проекта__ **__Paradox Role Play__**',
        color = discord.Color.from_rgb(244, 127, 255)
        )
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_author(name = 'Welcome!', icon_url = member.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()
    await member.add_roles(role)
    await bot.get_channel(930825093238652938).send(embed = embed1)
    await bot.get_channel(922190850614763619).send(f'{member.mention}', embed = embed)

bot.run('OTMwODI0NTE4MDUyNzQxMTIw.Yd7f4g.bdwSwg_04wyCusAb0GEJlpmKJqA')
