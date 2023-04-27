import discord

import datetime
import contextlib
import io
import typing

from aiohttp import payload
from discord.ext import commands, tasks
from discord import reaction, guild, member
from discord import emoji
from discord.utils import get
import asyncio
import os
import glob
import natsort
from PIL import Image, ImageDraw, ImageFont

from messages import mess, roles, itogo, price, shopmtask
from newspars import epic
from shop import shopapi
from fortniteapi import stat

token = 
client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
time = datetime.time(hour=13, minute=1, second=0,microsecond=0, tzinfo=None)

with open('files/curseWord.txt', 'r', encoding='utf-8') as f:
    curseWord = f.read().splitlines()


@client.listen('on_message')
async def whatever_you_want_to_call_it(message):
    msg_content = message.content.lower()
    words = str.split(msg_content)
    # if any(word in msg_content for word in curseWord):
    sum_word = (list(set(curseWord).intersection(words)))
    if len(sum_word):
        await message.delete()
        await message.channel.send(
            f"{message.author.mention} На этом сервере так не выражаются. Мне придется доложить об этом администратору.")
    else:
        return


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('```Укажите аргументы```')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("```Недостаточно прав```")


@client.event
async def on_ready():
    print("Я запущен")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="!info"))
    # task_news.start()
    task_shop.start()

@client.command()
async def info(ctx):
    await ctx.send('Не пиши так больше, иначе отправлю в мут на год!')


# функция проверки и публикации новых новостей
@tasks.loop(hours=1.0)
async def task_news():
    print('Запуск таска - ' + str(datetime.datetime.now()))
    allnews = await epic()
    try:
        if len(allnews):
            print('Публикую новости.')
            channel = client.get_channel(933835165313146953)
            for news in allnews:
                newscontent = discord.Embed()
                newscontent.title = 'Новости Fortnite ' + str(news[0]).lower()
                newscontent.set_image(url=news[3])
                newscontent.colour = discord.Color.blue()
                newscontent.url = news[2]
                newscontent.description = news[1]
                await channel.send(embed=newscontent)
        else:
            print('Нет новостей!')
    except Exception:
        print(f"Проверить VPN")


@task_news.before_loop
async def task_news_before():
    await client.wait_until_ready()


# команда отправки сообщения с правилами
@client.command()
async def rules(ctx):
    await mess(ctx)


# команда отправки сообщения с ролями
@client.command()
async def desrole(member):
    await roles(member)


@client.command()
async def pricem(ctx):
    await price(ctx)


# команда выдачи роли old по прошествии 6 месяцев
@client.command()
async def old(ctx):
    dayz = datetime.timedelta(days=182)
    guild = client.get_guild(933835165313146950)
    role = discord.utils.get(guild.roles, id=1006269033328418937)
    all_users = client.get_all_members()
    i = 0
    for ind, user in enumerate(all_users):
        if not user.bot:
            if datetime.date.today() - user.joined_at.date() > dayz:
                print(str(ind) + ' ' + user.name + ' ' + str(user.joined_at.date()))
                if role not in user.roles:
                    await user.add_roles(role)
                    message = f"Выдана роль Old пользователю {user.name}"
                    await ctx.send(message)
                    i += 1
    if i == 0:
        message = f"Роль Old никому не выдана"
        await ctx.send(message)
    '''
    guild = client.get_guild(933835165313146950)
    user = guild.get_member(1006217657005125704) # lubavca
    role = discord.utils.get(guild.roles, id=1006269033328418937)
    dayz = datetime.timedelta(days = 160)
    user_date = user.joined_at.date()
    today = datetime.date.today()
    join = today - user_date
    if join > dayz:
        await user.add_roles(role)
    else:
        print('мимо')
    '''


# команда информации по пользователю (имя мользователя необзятательный параметр)
@client.command()
async def user(ctx, *, user: typing.Optional[discord.Member]):
    if not user:
        user = ctx.author
    if user.nick:
        nick = user.nick
    else:
        nick = 'ник не задан'

    date = user.joined_at.date()

    name = user._user
    top_role = user.top_role.mention

    if user.activity:
        # noinspection PyUnresolvedReferences
        if user.activity.type.name == 'playing':
            status = f"Играет в **{str(user.activity.name)}**"
        else:
            status = user.activity
    else:
        status = 'статус не установлен'

    # print('Участвует с ' + str(date) + ' ник ' + str(nick) + ' имя ' + str(name) + 'топ роль ' + str(top_role) + 'статус ' + str(status))
    content = f"**Участник сервера с** {str(date)} \n" \
              f"**Ник** -  {str(nick)} \n" \
              f"**Top роль** - {str(top_role)} \n" \
              f"**Статус** - {str(status)} \n"
    user_cnt = discord.Embed()
    user_cnt.colour = discord.Color.green()
    user_cnt.description = content
    user_cnt.set_author(name=name)
    await ctx.send(embed=user_cnt)


# команда отправки сообщения с новостями с сайта epic
@client.command()
async def news(ctx):
    allnews = await epic()
    # await ctx.send(len(allnews))
    if len(allnews):
        print('Публикую новости.')
        for news in allnews:
            newscontent = discord.Embed()
            newscontent.title = 'Новости Fortnite ' + str(news[0]).lower()
            newscontent.set_image(url=news[3])
            newscontent.colour = discord.Color.blue()
            newscontent.url = news[2]
            newscontent.description = news[1]
            await ctx.send(embed=newscontent)
    else:
        await ctx.send('Нет новостей!')


# команда проверки соответствия правилам участия в розыгрыше
@client.command()
async def parti(member):
    users_list = []
    inv_list = []
    channel = client.get_channel(1007952831711543346)
    mess = await channel.fetch_message(1011658743504707654)
    async for user in mess.reactions[0].users():
        users_list.append(user.name)
        users_list.sort()
    gd = member.guild
    async for entry in gd.audit_logs(limit=500):
        if entry.action == discord.AuditLogAction.invite_create:
            inv_list.append(entry.user.name)
            inv_list.sort()
    # same_values = set(users_list) & set(inv_list)
    # sum_list = ('\n'.join(same_values))
    sum_list = (list(set(users_list).intersection(inv_list)))
    lenght = len(sum_list)
    list.sort(sum_list)
    # iff_list = list(set(users_list)-set(inv_list))
    # print(diff_list)
    await member.send('@everyone')
    content = ''
    title = 'Текущие участники розыгрыша!'
    for i in range(lenght):
        content += f"{str(i + 1)}. {sum_list[i]}\n"
    # await member.send(content)
    discrcont = discord.Embed(
        title=title,
        description=content,
        color=discord.Color.brand_green()
    )
    await member.send(embed=discrcont)

    # print(list(set(users_list).intersection(inv_list)))
    # print('\n'.join(same_values))

    diff_list = list(set(users_list) - set(inv_list))
    difflenght = len(diff_list)
    # print(diff_list)
    diffcont = ''
    title = 'Не создали приглашения(не учавствуют)!'
    for i in range(difflenght):
        diffcont += f"{str(i + 1)}. {diff_list[i]}\n"
    diffcontext = discord.Embed(
        title=title,
        description=diffcont,
        color=discord.Color.red()
    )
    await member.send(embed=diffcontext)


# команда публикации магазина
@client.command()
async def shop(ctx):
    await shopapi()
    folder_path = 'files/allshop/'
    files = glob.glob(os.path.join(folder_path, '*.jpg'))
    if len(files):
        print('Читаю файлы магазина')
        for file in files:
            with open(file, 'r') as f:
                imitem = discord.File(file)
                await ctx.send(file=imitem)
    else:
        print('Нет файлов магазина')


@client.command()
async def shopm(ctx):
    await itogo(ctx)


# функция проверки и публикации новых новостей
@tasks.loop(time=time)
async def task_shop():
    print('Запуск автоматической публикации магазина - ' + str(datetime.datetime.now()))
    await shopapi()
    message = await shopmtask()
    try:
        folder_path = 'files/allshop/'
        channel = client.get_channel(1009851212667039825)
        files = glob.glob(os.path.join(folder_path, '*.jpg'))
        title = f"Магазин предметов: {datetime.date.today()}"
        if len(files):
            print('Читаю файлы магазина')
            for file in files:
                with open(file, 'r') as f:
                    imitem = discord.File(file)
                    await channel.send(file=imitem)
            embed = discord.Embed(title=title,color=discord.Color.blue(),description=message)
            await channel.send(embed=embed)
        else:
            print('Нет файлов магазина')
    except Exception as err:
        print(str(err))

@task_news.before_loop
async def task_shop_before():
    await client.wait_until_ready()


@client.command()
async def stats(ctx, nik):
    message = stat(nik)
    message_cnt = discord.Embed()
    message_cnt.title = nik
    message_cnt.colour = discord.Color.green()
    message_cnt.description = message
    # message_cnt.set_author(name=ctx.author)
    await ctx.send(embed=message_cnt)


client.run(token)
