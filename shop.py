import datetime
from PIL import Image, ImageDraw, ImageFont
import os
import glob
import natsort
from operator import itemgetter

from jsonshop import shop_json
from drawitems import itemdraw
from drawshop import shopdraw

async def shopapi():
    allitems = await shop_json()
    outfits = []
    musics = []
    emotes = []
    gliders = []
    pickaxes = []
    backpacks = []
    wraps = []


    for item in allitems:
        if item[4] == 'outfit':
            outfits.append(item)
        elif item[4] == 'music':
            musics.append(item)
        elif item[4] == 'emote':
            emotes.append(item)
        elif item[4] == 'glider':
            gliders.append(item)
        elif item[4] == 'pickaxe':
            pickaxes.append(item)
        elif item[4] == 'backpack':
            backpacks.append(item)
        elif item[4] == 'wrap':
            wraps.append(item)
        else:
            print(item[4])

    allshop_path = 'files/allshop/'
    print('Очистка папки')
    all_shop = glob.glob(os.path.join(allshop_path, '*.jpg'))
    for f in all_shop:
        os.remove(f)

    if len(outfits):
        print('Публикую скины.')
        outfits = sorted(outfits, reverse=True, key=itemgetter(0, 1))
        #outfits = sorted(outfits, reverse=True, key=lambda x: x[0])
        for index, item in enumerate(outfits):
            category = item[0]
            price = item[1]
            name = item[2]
            rarity = item[3]
            stype = item[4]
            url_img = item[5]
            added = item[6]
            info = item[7]
            itemdraw(category, price, name, rarity, stype, url_img, added, info, index+1)
    else:
        print('Нет предметов!')
    title = 'Скины'
    await shopdraw(title)


    if len(musics):
        print('Публикую музыку.')
        musics = sorted(musics, reverse=True, key=itemgetter(0, 1))
        for index, item in enumerate(musics):
            category = item[0]
            price = item[1]
            name = item[2]
            rarity = item[3]
            stype = item[4]
            url_img = item[5]
            added = item[6]
            info = item[7]
            itemdraw(category, price, name, rarity, stype, url_img, added, info, index+1)
    else:
        print('Нет предметов!')
    title = 'Музыка'
    await shopdraw(title)


    if len(emotes):
        print('Публикую эмоции.')
        emotes = sorted(emotes, reverse=True, key=itemgetter(0, 1))
        for index, item in enumerate(emotes):
            category = item[0]
            price = item[1]
            name = item[2]
            rarity = item[3]
            stype = item[4]
            url_img = item[5]
            added = item[6]
            info = item[7]
            itemdraw(category, price, name, rarity, stype, url_img, added, info, index+1)
    else:
        print('Нет предметов!')
    title = 'Эмоции'
    await shopdraw(title)

    if len(gliders):
        print('Публикую дельтапланы.')
        gliders = sorted(gliders, reverse=True, key=itemgetter(0, 1))
        for index, item in enumerate(gliders):
            category = item[0]
            price = item[1]
            name = item[2]
            rarity = item[3]
            stype = item[4]
            url_img = item[5]
            added = item[6]
            info = item[7]
            itemdraw(category, price, name, rarity, stype, url_img, added, info, index+1)
    else:
        print('Нет предметов!')
    title = 'Дельтапланы'
    await shopdraw(title)


    if len(pickaxes):
        print('Публикую кирки.')
        pickaxes = sorted(pickaxes, reverse=True, key=itemgetter(0, 3, 1))
        for index, item in enumerate(pickaxes):
            category = item[0]
            price = item[1]
            name = item[2]
            rarity = item[3]
            stype = item[4]
            url_img = item[5]
            added = item[6]
            info = item[7]
            itemdraw(category, price, name, rarity, stype, url_img, added, info, index+1)
    else:
        print('Нет предметов!')
    title = 'Кирки'
    await shopdraw(title)

    if len(backpacks):
        print('Публикую бэкпаки.')
        backpacks = sorted(backpacks, reverse=True, key=itemgetter(0, 1))
        for index, item in enumerate(backpacks):
            category = item[0]
            price = item[1]
            name = item[2]
            rarity = item[3]
            stype = item[4]
            url_img = item[5]
            added = item[6]
            info = item[7]
            itemdraw(category, price, name, rarity, stype, url_img, added, info, index+1)
    else:
        print('Нет предметов!')
    title = 'Бэкпаки'
    await shopdraw(title)

    if len(wraps):
        print('Публикую обертки.')
        wraps = sorted(wraps, reverse=True, key=itemgetter(0, 1))
        for index, item in enumerate(wraps):
            category = item[0]
            price = item[1]
            name = item[2]
            rarity = item[3]
            stype = item[4]
            url_img = item[5]
            added = item[6]
            info = item[7]
            itemdraw(category, price, name, rarity, stype, url_img, added, info, index+1)
    else:
        print('Нет предметов!')
    title = 'Обёртки'
    await shopdraw(title)

    return()
