import cairo
from PIL import Image, ImageDraw, ImageFont, ImageColor, ImageEnhance

def footer(color):
    f_im = Image.new('RGBA', (359,79), (0, 0, 0, 0))

    a = color
    h = a.lstrip('#')
    rgb = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    #print(rgb)

    r1 = rgb[0]/1000
    g1 = rgb[1]/1000
    b1 = rgb[2]/1000
    r2 = r1 - 0.057
    g2 = g1
    b2 = b1 - 0.006

    '''
    r1 = 0.148
    g1 = 0
    b1 = 0.211
    r2 = r1 - 0.057
    g2 = g1
    b2 = b1 - 0.006
    '''
    #r2 = 0.205
    #g2 = 0
    #b2 = 0.205

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 359, 79)
    ctx = cairo.Context(surface)

    pattern = cairo.LinearGradient(71, 35, 215, 35)  #(x0,y0 , x1,y1)
    pattern.add_color_stop_rgb(0, r1, g1, b1)
    pattern.add_color_stop_rgb(1, r2, g2, b2)

    ctx.set_source(pattern)

    ctx.set_line_width(10)
    ctx.move_to(0,15)
    ctx.line_to(359,5)
    ctx.stroke()

    ctx.rectangle(0, 54, 359, 30)

    ctx.fill()

    ctx.paint_with_alpha(0)

    #surface.write_to_png('rectangle.png')

    def surface_to_pil():
        return Image.frombuffer(
            mode = 'RGBA',
            size = (surface.get_width(), surface.get_height()),
            data = surface.get_data()
        )

    f_im.paste(surface_to_pil(), (0,0))

    b, g, r, a = f_im.split()
    f_im = Image.merge("RGBA", (r, g, b, a))

    enhancer = ImageEnhance.Brightness(f_im)
    f_im = enhancer.enhance(factor=4)

    #im.show()
    f_im.save('files/sources/footer.png')
    return f_im
