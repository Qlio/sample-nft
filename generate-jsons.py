import json
for i in range(1, 10001):
    with open(f'./bayc-jsons/{i}.json', 'w') as f:
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
