import time
import requests
import telepot

from keep_alive import keep_alive

cookies = {
    's_fid': '13B293E0AA18B7EE-32F7F040400DC3D2',
    's_sq': 'applestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253DAOS%25253A%252520bag%2526link%253Dapple%252520fashion%252520island%252520%252528inner%252520text%252529%252520%25257C%252520no%252520href%252520%25257C%252520body%2526region%253Dbody%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DAOS%25253A%252520bag%2526pidt%253D1%2526oid%253DfunctionVc%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DBUTTON',
    'as_dc': 'nc',
    'dssf': '1',
    'dssid2': '96d1f443-1357-4067-918e-68c63b183284',
    'rtsid': '%7BUS%3D%7Bt%3Da%3Bi%3DR015%3B%7D%3B%7D',
    's_vi': '[CS]v1|31186C32DD0E8CB7-60000C5C166A719D[CE]',
    's_cc': 'true',
    'as_sfa': 'Mnx1cy1lZHV8dXN8fGVuX1VTfGVkdUluZHxpbnRlcm5ldHwxfDB8MQ',
    'as_loc': 'ce83f8d469bb2802ecc32fcda770df27e6a89c85e7c8c2ed34cea80d25c646e63d4de001adef1850f82f069daad274831910b12b48aa8ec3283bc4be27f82732c056b1f89ea392ec6bbd4c35f12606305fadedd500613fc9810bc1cda5211919fc896c543358ae5e7c11a6bf0aff68911fd544456b5038bbc35b8b2e03ae16b10d9b79e6175bbc6325bc8b0b9676371a2566ca3eea83055aa37bdc978878f312',
    'as_uct': '2',
    'as_atb': '1.0|MjAyMi0wMy0xNSAxMTo0Mjo0NA|ebae087a8620f35916ef2701f9fe2d78dfc89ca2',
    'pxro': '2',
    'as_pcts': 'WktTwrlI+BH1Fm1mXetRylZVyAkNqbBoWSA:t7yut7hwQQfoxG03Yww35a64IWBCdpqM313WiZ1w+ZxQR_3tQz:zYKG9_hQZPM_twy:tFoS6GgZMm4QEqpQ_2iNHVgNV+',
    'at_check': 'true',
    'mbox': 'session#134a58520c8040be9cc008b609e0d7d0#1647370154|PC#134a58520c8040be9cc008b609e0d7d0.35_0#1647370094',
    'geo': 'US',
    'POD': 'us~en',
    'as_tex': '~1~|433415:1:1646917679:USA|434643:1:1647842334:USA|1Lqy/Ws8wTZjT+n2HvZU8r6dCUxposeEgONo7ojiYTY',
    'as_disa': 'AAAjAAAB_YUS62o-U_sy2Sgpb4ZMgwpkHDmIiJ0P91oQqQgL49SiDe2VUOzudUx_hVNUXJb-AAIBOIIa2i7Jp052Y55aemv5wlWtk3HgpnYDb6bGkUnuR9c=',
    'accs': 'o',
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Host': 'www.apple.com',
    'Origin': 'https://www.apple.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15',
    'Referer': 'https://www.apple.com/us-edu/shop/bag',
    'Content-Length': '0',
    'Connection': 'keep-alive',
    'X-Requested-With': 'Fetch',
    'x-aos-model-page': 'cart',
    'modelVersion': 'v2',
    'x-aos-stk': '-70XcNhttkyFV3xQE9ww4W4gZzmt-7cCnWAYj8Ds7yE',
    'syntax': 'graviton',
}

params = (
    ('_a', 'storeLocatorView'),
    ('_m', 'shoppingCart.items.item-85a0052a-8e1b-41ed-ae75-22840fece3e0.delivery'),
)


response = requests.get('https://www.apple.com/us-edu/shop/bagx',
                         headers=headers,
                         params=params,
                         cookies=cookies)

count = 0
token = '2056608864:AAGaWoTgT28fqcNV9QKYHv_FEfZnMPi8gD4'
# https://api.telegram.org/bot2056608864:AAGaWoTgT28fqcNV9QKYHv_FEfZnMPi8gD4/getUpdates
receiver_id = 138135010
bot = telepot.Bot(token)
searching = True
shown = set()

keep_alive()

while searching:
    print('starting iteration {}'.format(count + 1))
    response = requests.get('https://www.apple.com/us-edu/shop/bagx',
                         headers=headers,
                         params=params,
                         cookies=cookies)
    
    response = dict(response.json())
    store_list = response['body']['shoppingCart']['items']['item-85a0052a-8e1b-41ed-ae75-22840fece3e0']['delivery']['storeLocator']['searchResults']['d']['retailStores']
    
    for store in store_list:
        for item in store['availability']['lineItemAvailability']:
            itemname = item['partName']
            #itemname = list('' + i for i in item['partName'].split('\xa0')[2:])
            #itemname = itemname[0] + ' ' + itemname[1]
            if item['availableNowForLine']:
                print('{} Available! At {}. Hurry up!'.format(
                    itemname, store['storeName']))
                bot.sendMessage(receiver_id, '{} Available! At {}. Hurry up!'.format(
                            itemname, store['storeName']))
    count += 1
    print('iteration {} completed, pausing for 7 sec'.format(count))
    time.sleep(7)
    