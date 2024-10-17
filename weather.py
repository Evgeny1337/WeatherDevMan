import requests

def main():
    places = ['Череповец', 'svo', 'Лондон']
    params = {'n':'','T':'','q':'','M':'','lang':'ru'}
    for place in places:
        url = f'http://wttr.in/{place}'
        yield [url,params]

if __name__ == '__main__':
    result = main()
    for item in result:
        response = requests.get(url=item[0],params=item[1])
        response.raise_for_status()
        print(response.text)
