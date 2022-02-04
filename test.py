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
    await bot.get_channel(881448669809885254).send(embed = embed)


@bot.command(aliases = ['тест'])
async def test(ctx):
	await ctx.reply(embed = discord.Embed(description = 'работаю'))


@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, id = 938309468180074497)
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
    await bot.get_channel(881448669809885254).send(embed = embed1)
    await bot.get_channel(938309496114147388).send(f'{member.mention}', embed = embed)


@bot.command(aliases = ['инфо'])
async def info(ctx):
    em = discord.Embed(
        title = 'Paradox Role Play Информация',
        description = 'Для подключения к серверу просто найдите в списке серверов PARADOX RP\n\n**Торговая площадка ->** https://discord.gg/db3mnTRG8R\n\n**Мы Вконтакте ->** https://vk.com/paradox_gta\n**Беседа в ВК ->** https://vk.me/join/X7U86XsIq6hTYhcKgogzo1SBHnHYhnBT53A=\n**YouTube Канал ->** https://www.youtube.com/channel/UCQzUrQC6u6a0EFgGOSAO76w\n\n**Cчёт для пожертвований на развитие сервера ->** https://www.tinkoff.ru/cf/6nLsTXiR397\n*В комментариях указываем свой ник. На сервере выдаём коины в Х3 размере от пополнения.*'
        )
    em.set_footer(text = 'Paradox RP Bot')
    em.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed = em)


@bot.command(aliases = ['правила'])
async def rules(ctx):
    em = discord.Embed(
        title = 'Paradox Role Play Правила',
        description = '📗 **ОСНОВНЫЕ ПРАВИЛА:**\n• После входа на сервер, вы автоматически соглашаетесь и принимаете правила нашего Discord сервера\n• Правила могут добавляться, корректироваться, а так же дополняться без ведома пользователей Discord сервера, поэтому рекомендуется следить за правилами и новостями\n• За чрезмерное нарушение правил сервера, а также поиски их обхода, вы получите наказание в виде исключения/блокировки с сервера (на усмотрение модерации)\n• Запрещены любые формы оскорблений, неадекватного поведения, издевательств, расизма, дискриминации, религиозной враждебности, сексизма, токсичность и т.п\n• Запрещены шокирующий, Rx и NSFW контенты (18+)\n• Запрещена реклама любых сторонних проектов, ресурсов, сайтов и т.п. без согласования с командой редакции Discord (упоминание - не есть реклама)\n• Запрещён деанон в любом виде (адрес проживания, номер телефона, личные фотографии/сообщения, разглашение любой личной информации)\n\n• Запрещены какие-либо действия перечащие регламенту проекта (покупка/продажа валюты и т.д.)\n• Команда Discord вправе выбирать степень и длительность наказания, по своему усмотрению и в зависимости от тяжести нарушения, в разумных рамках\n• Если вы считаете, что получили наказание незаслуженно, то можете написать жалобу на модератора, который выдал вам наказание, на форуме проекта/личные сообщения старшей модерации/главной модерации\n• Запрещено вводить в заблуждение/обманывать модерацию Discord\n• Запрещено оскорблять модерацию Discord в личных сообщениях DS\n• Пользователи Discord имеют возможность предоставить свои улучшения в личные сообщения старшей/главной модерации\n• Запрещено распространение политических воззрений, мнений, суждений(либерализм, демократизм, коммунизм и т.д)\n• Запрещено распространие нацизма, фашизма и любых связанных с этим аббревиатур, понятий, движений и т.п.\n\n💬 **ПРАВИЛА ОБЩЕНИЯ В ТЕКСТОВЫХ КАНАЛАХ:**\n• Запрещено несоблюдение тематики чата\n• Запрещено злоупотребление капсом, флудом, спамом и т.п\n• Запрещено упоминание пингующихся ролей просто так, так же и пользователей\n• Запрещено провоцировать пользователей/модераторов Discord на какие-либо оскорбления, действия\n\n🔊 **ПРАВИЛА ОБЩЕНИЯ В ГОЛОСОВЫХ КАНАЛАХ:**\n• Запрещено умышлено создавать разговорные помехи. (Шумы, визги, стоны, громкие звуки через стороннее ПО и прочее)\n• Разрешено использование сторонние программ для воспроизведения звуков через микрофон\n• Запрещено оскорбление администрации сервера, модерации Discord\n• Запрещено ставить себе неподобающий nickname в Discord, как либо задевающий других пользователей\n\n🎉 **ПРАВИЛА МЕРОПРИЯТИЙ:**\n• Ведущими мероприятий могут являться модераторы Discord, администраторы сервера, а также ведущие назначенные модерацией\n• Правила того или иного мероприятия назначают модераторы Discord, ведущие, администраторы в зависимости от проводящегося мероприятия\n• При нахождении на мероприятии, вы также соблюдаете правила по голосовым каналам, а также основные правила'
        )
    em.set_footer(text = 'Paradox RP Bot')
    em.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed = em)


bot.run('OTMwODI0NTE4MDUyNzQxMTIw.Yd7f4g.bdwSwg_04wyCusAb0GEJlpmKJqA')
