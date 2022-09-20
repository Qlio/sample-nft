# from PIL import Image, ImageDraw, ImageFont
#
# for i in range(1, 10001):
#     img = Image.new('RGB', (500, 500), color = (0, 255, 255))
#     fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 25)
#     d = ImageDraw.Draw(img)
#     d.text((200,150), f'{i}', font=fnt, fill=(0, 0, 0))
#
#     img.save(f'./images/{i}.png')


import json
for i in range(1, 10001):
    with open(f'./jsons/{i}.json', 'w') as f:
        f.write(json.dumps({
                               "attributes": [
                                   {
                                       "trait_type": "Number",
                                       "value": f'{i}'
                                   }
                               ],
                               "description": "Cyan Test Collection with numbers",
                               "image": f'https://raw.githubusercontent.com/Qlio/sample-nft/main/images/{i}.png',
                               "name": f'Cyan Numbers #{i}'
                           }))
