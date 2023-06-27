from PIL import Image, ImageDraw, ImageFont

W, H = 250, 250

bayc_bg = (19, 19, 19)
mayc_bg = (211, 222, 94)
bakc_bg = (0, 0, 0)

font_color = (255, 255, 255)

for i in range(1, 10001):
    font_size = 0
    if i < 1000:
        font_size = 100
    else:
        font_size = 80

    logo = Image.open("bakc.png")
    new_width = W
    new_height = new_width * logo.height // logo.width

    logo = logo.resize((new_width, new_height), Image.LANCZOS)

    img = Image.new('RGB', (W, H), color=bakc_bg)
    img.paste(logo, (0, 50))

    draw = ImageDraw.Draw(img)

    message = f'{i}'

    font = ImageFont.truetype('/Library/Fonts/Arial.ttf', font_size)
    _, _, w, h = draw.textbbox((0, 0), message, font=font)
    draw.text(((W - w) / 2, (H - h) / 2 + 50), message, font=font, fill=font_color)

    img.save(f'./bakc/{i}.png')
