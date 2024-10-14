import requests

places = ['Череповец', 'Шереметьево', 'Лондон']
for place in places:
    url = f'http://wttr.in/{place}?nTquM&lang=ru'
    response = requests.get(url)
    if not response.ok:
        print(requests.exceptions.HTTPError(response=response))
    else:
        print(response.text)
