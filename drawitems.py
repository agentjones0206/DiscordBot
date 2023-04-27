from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
from gradient import footer

imwm = Image.open('files/sources/watermark.png')
imvbacks = Image.open('files/sources/vbuck.png')
rub = Image.open('files/sources/rub.png')
price_font = ImageFont.truetype('files/sources/Fort.ttf', size=32)
info_font = ImageFont.truetype('files/sources/Fort.ttf', size=10)
folder_path = 'files/shop/'

k = 0.35
jump_size = 4
#chars = ['.', ',', '!', '?']

def itemdraw(category, price, name, rarity, stype, url_img, added, info, index):

    name_font = ImageFont.truetype('files/sources/Fort.ttf', size=28)
    response = requests.get(url_img)
    im = Image.open(BytesIO(response.content))

    if rarity == 'rare':      # редкий - голубой
        color = '#058FD9'
    elif rarity == 'epic':
        color = '#895DDA'
    elif rarity == 'uncommon':
        color = '#509F39'
    elif rarity == 'icon':
        color = '#ffb833'
    elif rarity == 'dc':
        color = '#055BA9'
    elif rarity == 'legendary':
        color = '#ffff00'
    else:
        color = '#A0A0A0'

    new_image = im.resize((359, 359))

    if im.format == 'PNG' or im.mode == 'RGBA':
        try:
            blank_image = Image.new('RGB',(359,359),color)
            blank_image.paste(new_image, mask=new_image)
            new_image = blank_image
            new_image.convert('RGB')
        except:
            new_image.convert('RGB')
    else:
        new_image = im.resize((359,     359))

    width_img = new_image.size


    draw_footer = ImageDraw.Draw(new_image)
    #draw_footer.line((-10, 310, 365, 300), fill=color, width=50)
    #draw_footer.rectangle((0, 290, 359, 335), fill='#4d4d4d')
    #draw_footer.rectangle((0, 335, 359, 359), fill=color)

    f_im = footer(color)

    draw_footer.rectangle((0, 290, 359, 335), fill='white')
    new_image.paste(f_im, (0,280),mask=f_im)
    new_image.paste(imvbacks, (310, 310), mask=imvbacks)
    new_image.paste(rub, (-5, 310), mask=rub)

    rub_price = int(price) * k
    draw_text = ImageDraw.Draw(new_image)

    while name_font.getlength(name) >= width_img[0] - 10:
        size_font = name_font.size - jump_size
        name_font = ImageFont.truetype('files/sources/Fort.ttf', size_font)

    draw_text.text((width_img[0] / 2, 315), name, font=name_font, anchor="mm", fill='black')
    draw_text.text((width_img[0] / 2, 330), info, font=info_font, anchor="mm", fill='grey')
    draw_text.text((260, 325), str(price), font=price_font)
    draw_text.text((50, 325), str(round(rub_price)), font=price_font)

    #name_file = name.translate(str.maketrans({ord(x): '' for x in chars}))
    new_image.save(folder_path  + 'file' + '_0' + str(index) + '.jpg')
