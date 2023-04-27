import datetime

import discord
from aiohttp import payload
from discord.ext import commands
from discord import reaction, guild, member
from discord import emoji
from discord.utils import get

from jsonshop import shop_json
import discord


async def mess(ctx):
    message = f"\n" \
              f"1.0. Уважительно относится к старшим по роли вне зависимости от вашего возраста.\n" \
              f"\n" \
              f"1.1. Запрещена ненормативная лексика и использование нецензурных слов в профиле — в никах/аватарах/статусах. Мат разрешен в неоскорбительном для других пользователей контексте. Чрезмерное употребление мата (более 3 сообщений подряд) запрещено. (мут 24 часа) \n" \
              f"\n" \
              f"1.2. Запрещено писать бессмысленную или малосодержательную информацию, не несущую смысловой нагрузки — флудить. Флудить смайликами, буквами и разными стилями шрифта. (мут час) \n" \
              f"\n" \
              f"1.3. Запрещается дискриминация по любому признаку — расовому, национальному, гражданскому, половому, религиозному, возрастному, по инвалидности, роду занятий или сексуальной ориентации. (мут 24 часа) \n" \
              f"\n" \
              f"1.4. Запрещается токсичное неадекватное поведение, оскорбление пользователей, а также попрошайничество в любом виде (кроме канала ""ты мне я тебе""). (мут 24 часа) \n" \
              f"\n" \
              f"1.5. Запрещено оскорблять администрацию сервера. (мут 24 часа)\n" \
              f"\n" \
              f"1.6. Запрещено оскорбление родных. (бан)\n" \
              f"\n" \
              f"1.7. Запрещается публикация материалов грубого, насильственного характера, жестокости, призывы к таковым, расизм, свастика и сообщения экстремистского толка, обсуждение политики. (бан)\n" \
              f"\n" \
              f"1.8. Запрещено размещение материалов 18+ (текстов, статусов, ссылок, медиа). (бан)\n" \
              f"\n" \
              f"1.9. Запрещено пропаганда наркотиков, алкоголя, никотиносодержащих веществ и их заменителей. (бан)\n" \
              f"\n" \
              f"1.10. Любого рода реклама товаров, услуг, самореклама и любая другая коммерческая деятельность запрещена. (бан)\n" \
              f"\n" \
              f"2.0. Любой пользователь сервера может пожаловаться в личные сообщения администратору сервера на админов и модераторов.\n" \

    embed = discord.Embed(
        title="Правила сервера:",
        # url="",
        description=message,
        color=discord.Color.red())
    await ctx.send(embed=embed)

async def roles(member):
    # Роли за активность в DS
    role1 = member.guild.get_role(1006230387002986527)  # Банан
    role2 = member.guild.get_role(1006264353999294507)  # Карась
    role3 = member.guild.get_role(1006265050832580658)  # Лама
    role4 = member.guild.get_role(1006265650852929669)  # Мяускл
    role5 = member.guild.get_role(1006266865452056736)  # Джоунси
    role6 = member.guild.get_role(1006267282701418516)  # Мидас
    role7 = member.guild.get_role(1006267649438777484)  # Основатель

    message1 = f"✷{role1.mention} роль для новичков \n" \
               f"✷{role2.mention} 10 lvl в главном чате \n" \
               f"✷{role3.mention} 20 lvl в главном чате \n" \
               f"✷{role4.mention} 30 lvl в главном чате \n" \
               f"✷{role5.mention} 50 lvl в главном чате \n" \
               f"✷{role6.mention} 70 lvl в главном чате \n" \
               f"✷{role7.mention} 100 lvl в главном чате \n" \

    # Выдаваемые роли
    srole1 = member.guild.get_role(1017047219586736228)  # Даритель
    srole2 = member.guild.get_role(1017046535202152460)  # Донатер
    srole3 = member.guild.get_role(1014245427924717672)  # Фартовый
    srole4 = member.guild.get_role(1010245193171226674)  # artist
    srole5 = member.guild.get_role(1006268226319167498)  # Girl
    srole6 = member.guild.get_role(1006269033328418937)  # Old
    srole7 = member.guild.get_role(1014240058884247553)  # Кибер
    srole8 = member.guild.get_role(1014232417185316886)  # TikToker
    srole9 = member.guild.get_role(1020967551091609632)  # YouTuber
    srole10 = member.guild.get_role(1020969149138214973)  # Streamer

    message2 = f"✷{srole1.mention} выдаётся за подаренные подарки в Fortnite \n" \
               f"✷{srole2.mention} выдаётся за донат от 500р \n" \
               f"✷{srole3.mention} выдаётся за победы в розыгрыше \n" \
               f"✷{srole4.mention} выдаётся авторам эмодзи \n" \
               f"✷{srole5.mention} выдаётся девочкам \n" \
               f"✷{srole6.mention} выдаётся за 6 месяцев пребывания на ds-сервере \n" \
               f"✷{srole7.mention} выдаётся за самый частый Топ1 в творке \n" \
               f"✷{srole8.mention} выдаётся от 15 тысяч подписчиков на TikTok \n" \
               f"✷{srole9.mention} выдаётся от 500 подписчиков на YouTube \n" \
               f"✷{srole10.mention} выдаётся от 1000 подписчиков на Twitch \n"

    embed = discord.Embed(
        title="Роли за активность:",
        # url="",
        description=message1,
        color=discord.Color.blue())
    await member.send(embed=embed)


    embed = discord.Embed(
        title="Эксклюзивные роли:",
        # url="",
        description=message2,
        color=discord.Color.blue())
    await member.send(embed=embed)

async def itogo(ctx):
    allitems = await shop_json()

    bundle = []
    message2 = ''

    for item in allitems:
        bundle_n = item[8]
        bundle_i = item[7]
        if bundle_n not in bundle and bundle_i:
            bundle_all = (bundle_n, bundle_i)
            bundle.append(bundle_all)

    for ind, i in enumerate(bundle):
        message2 = message2 + str(ind + 1) + '. ' + i[0] + ' ' + str.lower(i[1]) + '\n'
        #print(ind + 1, i[0], i[1])

    outfit = 0
    musics = 0
    emotes = 0
    gliders = 0
    pickaxes = 0
    backpacks = 0
    wraps = 0
    itogo = 0

    for item in allitems:
        itogo += 1
        if item[4] == 'outfit':
            outfit += 1
        elif item[4] == 'music':
            musics += 1
        elif item[4] == 'emote':
            emotes += 1
        elif item[4] == 'glider':
            gliders += 1
        elif item[4] == 'pickaxe':
            pickaxes += 1
        elif item[4] == 'backpack':
            backpacks += 1
        elif item[4] == 'wrap':
            wraps += 1
        else:
            print(item[4])

    message = ''
    if outfit:
        message = message + f"Скинов - {outfit} \n"
    if musics:
        message = message + f"Скинов - {musics} \n"
    if emotes:
        message = message + f"Эмоций - {emotes} \n"
    if gliders:
        message = message + f"Дельтапланов - {gliders} \n"
    if pickaxes:
        message = message + f"Кирок - {pickaxes} \n"
    if backpacks:
        message = message + f"Бэкпаков - {backpacks} \n"
    if wraps:
        message = message + f"Оберток - {wraps} \n"
    message = message + f"Всего предметов в магазине - {itogo} \n"

    title = f"Магазин предметов: {datetime.date.today()}"
    embed = discord.Embed(
        title=title,
        color=discord.Color.blue(),
        description=message)
    await ctx.send(embed=embed)


    embed2 = discord.Embed(
        color=discord.Color.blue(),
        description=message2)
    await ctx.send(embed=embed2)

async def shopmtask():
    allitems = await shop_json()

    bundle = []
    message2 = ''

    for item in allitems:
        bundle_n = item[8]
        bundle_i = item[7]
        if bundle_n not in bundle and bundle_i:
            bundle_all = (bundle_n, bundle_i)
            bundle.append(bundle_all)

    for ind, i in enumerate(bundle):
        message2 = message2 + str(ind + 1) + '. ' + i[0] + ' ' + str.lower(i[1]) + '\n'
        #print(ind + 1, i[0], i[1])

    outfit = 0
    musics = 0
    emotes = 0
    gliders = 0
    pickaxes = 0
    backpacks = 0
    wraps = 0
    itogo = 0

    for item in allitems:
        itogo += 1
        if item[4] == 'outfit':
            outfit += 1
        elif item[4] == 'music':
            musics += 1
        elif item[4] == 'emote':
            emotes += 1
        elif item[4] == 'glider':
            gliders += 1
        elif item[4] == 'pickaxe':
            pickaxes += 1
        elif item[4] == 'backpack':
            backpacks += 1
        elif item[4] == 'wrap':
            wraps += 1
        else:
            print(item[4])

    message = ''
    if outfit:
        message = message + f"Скинов - {outfit} \n"
    if musics:
        message = message + f"Скинов - {musics} \n"
    if emotes:
        message = message + f"Эмоций - {emotes} \n"
    if gliders:
        message = message + f"Дельтапланов - {gliders} \n"
    if pickaxes:
        message = message + f"Кирок - {pickaxes} \n"
    if backpacks:
        message = message + f"Бэкпаков - {backpacks} \n"
    if wraps:
        message = message + f"Оберток - {wraps} \n"
    message = message + f"Всего предметов в магазине - {itogo} \n"

    #title = f"Магазин предметов: {datetime.date.today()}"
    message = f"{message} \n{message2}"
    return message

    '''embed = discord.Embed(
        title=title,
        color=discord.Color.blue(),
        description=message)
    await ctx.send(embed=embed)


    embed2 = discord.Embed(
        color=discord.Color.blue(),
        description=message2)
    await ctx.send(embed=embed2)
    '''

async def price(ctx):
    #user1 = get_user(1006217657005125704)
    #user2 = client.get_user(933833283479945247)
    message = f"\n" \
              f"Стоимость покупки через подарок: \n" \
              f"\n" \
              f"200 V-BUCKS - 70 руб.\n" \
              f"300 V-BUCKS - 105 руб. \n" \
              f"500 V-BUCKS - 175 руб.\n" \
              f"800 V-BUCKS - 280 руб.\n" \
              f"1000 V-BUCKS - 350 руб. \n" \
              f"1200 V-BUCKS - 420 руб.\n" \
              f"1500 V-BUCKS - 525 руб.\n" \
              f"1800 V-BUCKS - 630 руб.\n" \
              f"2000 V-BUCKS - 700 руб.\n" \
              f"\n" \
              f"Если вы планируете в ближайшее время покупку, обращайтесь к e-lectrica и l-ubavka.e-lca!\n" \

    embed = discord.Embed(
        title="Стоимость V-BUCKS подарками из магазина предметов:",
        # url="",
        description=message,
        color=discord.Color.yellow())
    await ctx.send(embed=embed)
