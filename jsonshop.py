import json
import requests

async def shop_json():
    url = 'https://fortnite-api.com/v2/shop/br/combined'
    params = dict(language='ru')
    resp = requests.get(url=url, params=params)
    binary = resp.content
    output = json.loads(binary)

    data = output['data']['featured']['entries']
    #print(data)

    allitems = []

    for content in data:
        #categories = content['categories']
        #category = categories[0]
        if content['section']:
            category = content['section']['id']
        else:
            category = content['sectionId']
        if content['bundle']:
            info = content['bundle']['info']
        else:
            info = ''
        if content['bundle']:
            bundle_name = content['bundle']['name']
        else:
            bundle_name = ''
        #landingprioryty = content['section']['landingPriority']
        price = content['regularPrice']
        items = content['items']
        name = items[0]['name']
        # description = items[0]['description']
        rarity = items[0]['rarity']['value']
        stype = items[0]['type']['value']
        # image = items[0]['images']['smallIcon']
        if content['newDisplayAsset']:
            try:
                image = content['newDisplayAsset']['materialInstances'][0]['images']['Background']
            except:
                image = content['newDisplayAsset']['materialInstances'][0]['images']['OfferImage']
        elif items[0]['images']['icon']:
            image = items[0]['images']['icon']
        else:
            image = 'no image'
        added = items[0]['added']
        items = (category, price, name, rarity, stype, image, added, info, bundle_name)
        allitems.append(items)

    data = output['data']['daily']['entries']

    for content in data:
        #categories = content['categories']
        #category = categories[0]
        if content['section']:
            category = content['section']['id']
        else:
            category = content['sectionId']
        if content['bundle']:
            info = content['bundle']['info']
        else:
            info = ''
        if content['bundle']:
            bundle_name = content['bundle']['name']
        else:
            bundle_name = ''
        #landingprioryty = content['section']['landingPriority']
        price = content['regularPrice']
        items = content['items']
        name = items[0]['name']
        #description = items[0]['description']
        rarity = items[0]['rarity']['value']
        stype = items[0]['type']['value']
        # image = items[0]['images']['smallIcon']
        if content['newDisplayAsset']:
            try:
                image = content['newDisplayAsset']['materialInstances'][0]['images']['Background']
            except:
                image = content['newDisplayAsset']['materialInstances'][0]['images']['OfferImage']
        elif items[0]['images']['icon']:
            image = items[0]['images']['icon']
        else:
            image = 'no image'
        added = items[0]['added']
        items = (category, price, name, rarity, stype, image, added, info, bundle_name)
        allitems.append(items)
    return allitems
