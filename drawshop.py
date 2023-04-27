import datetime
from PIL import Image, ImageDraw, ImageFont
import os
import glob
import natsort

async def shopdraw(title):
    imback = Image.open('files/sources/shopbackground.jpg')
    imwm = Image.open('files/sources/watermark.png')
    rub = Image.open('files/sources/rub.png')
    title_font = ImageFont.truetype('files/sources/Fort.ttf', size=48)
    title_font2 = ImageFont.truetype('files/sources/Fort.ttf', size=36)
    folder_path = 'files/shop/'

    width_img = imback.size
    title_size = title_font.getlength(title)

    date = datetime.date.today()

    podpis1 = 'Стоимость предмета в магазине E-LECTRICA!'
    podpis2 = ''
    podpis3 = 'Страница'

    draw_title = ImageDraw.Draw(imback)
    #draw_title.text(( (width_img[0] / 2) - (title_size / 2), 170), title, font=title_font2)
    #draw_title.text((824, 130), title, font=title_font)
    draw_title.text((((width_img[0] / 3) * 2) + ((width_img[0] / 3)/2) - (title_size / 2), 150), title, font=title_font)
    draw_title.text((100, 150), str(date), font=title_font)

    #draw_title.text((824, 130), group_name, font=title_font)
    imback.save('files/sources/imback.jpg')

    x_start = 20
    y_start = 250
    x = 20
    y = 250
    xy_img = 359
    step = 20

    files = glob.glob(os.path.join(folder_path, '*.jpg'))

    #files = os.listdir(folder_path)
    files = natsort.natsorted(files)

    #print(files)
    #print(len(files))
    i_start = 0
    i_stop = i_start + 12
    podpis1_size = title_font.getlength(podpis1)

    for ind, i in enumerate((files)[::12]):
        l_page = max(enumerate((files)[::12]))[0]
        for index, filename in enumerate(files[i_start:i_stop]):
          l_ind = max(enumerate(files[i_start:i_stop]))[0]
          with open(filename, 'r') as f:
              imitem = Image.open(filename)
              imback.paste(imitem, (x, y))
              x = x + xy_img + step
              s = (index + 1) / 3
              if (float(s).is_integer()) and (index < int(l_ind)):
                y = y + xy_img + step
                x = x_start
              if index+1 == i_stop-(12*ind):
                draw_footer = ImageDraw.Draw(imback)
                draw_footer.rectangle((120, 1800, 1040, 1850), fill='white')
                draw_title = ImageDraw.Draw(imback)
                draw_title.text((475,200), podpis3 + ' ' + str(ind+1) + ' из ' + str(l_page+1), font=title_font2, fill='white')
                imback.paste(rub, (120, 1801), mask=rub)
                draw_title.text(((width_img[0] / 2) - (podpis1_size / 2), 1797), podpis1, font=title_font, fill='#055BA9')
                #draw_title.text((310, 1850), podpis2, font=title_font, fill='#055BA9')
                imback.paste(imwm, mask=imwm)
                imback.save('files/allshop/' + title + '_' + str(ind) + '.jpg')
              if (index == l_ind) and (l_ind < (i_stop-1)-(12*ind)):
                #print('Последний индекс ' + str(l_ind))
                draw_footer = ImageDraw.Draw(imback)
                draw_footer.rectangle((120, y+413, 1040, y + 463), fill='white')
                imback.paste(rub, (120, y+414), mask=rub)
                draw_title = ImageDraw.Draw(imback)
                draw_title.text((475,200), podpis3 + ' ' + str(ind+1) + ' из ' + str(l_page+1), font=title_font2, fill='white')
                draw_title.text(((width_img[0] / 2) - (podpis1_size / 2), y+410), podpis1, font=title_font, fill='#055BA9')
                #draw_title.text((310, y+510), podpis2, font=title_font, fill='#055BA9')
                im_crop = imback.crop((0, 0, 1152, y+661))
                width_crop = im_crop.size
                imwm.resize(width_crop)
                im_crop.paste(imwm, mask=imwm)
                im_crop.save('files/allshop/' + title + '_' + str(ind) + '.jpg')
          os.remove(filename)

        i_start = i_stop
        i_stop = i_start + 12
        x = x_start
        y = y_start

        #imback.show()

        #imback.paste(imwm, mask=imwm)
        #imback.save('D:/allshop/' + title + '_' + str(ind) + '.jpg')

        imback = Image.open('files/sources//imback.jpg')
