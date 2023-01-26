def return_sheet(schem, sheet, step=1, wall=1, floor=0, sep=';', player='P'):

    from PIL import Image
    # step = 5
    # schem = 'image142.png'
    im = Image.open(schem)
    w, h = im.size
    pix = im.load()
    # sheet = 'sheet.txt'
    sheet = open(sheet, 'w')
    for y in range(0, h - step + 1, step):
        for x in range(0, w - step + 1, step):
            n = 0
            d = 0
            for i in range(step):
                for j in range(step):
                    s = pix[x+i, y+j]
                    r, g, b = s[:3]
                    if r / 16 > 13 and g / 16 < 2 and b / 16 < 2:
                        d += 1
                    elif r / 16 > 15 and g / 16 > 15 and b / 16 > 15:
                        n += 1
            n = round(n / step**2)
            if not n:
                n = wall
            else:
                n = floor
            d = round(d / step ** 2)
            if d:
                n = player
            print(f'{n}', end=sep, file=sheet)
        print('', file=sheet)


if __name__ == '__main__':
    return_sheet('image142.png', 'sheet3.txt', step=5, wall=1, floor=' ', sep='', player='P')
