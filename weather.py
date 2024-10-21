import requests

def get_urls():
    places = ['Череповец', 'svo', 'Лондон']
    for place in places:
        yield f'http://wttr.in/{place}'

def main():
    params = {'n':'','T':'','q':'','M':'','lang':'ru'}
    urls = get_urls()
    for url in urls:
        response = requests.get(url=url,params=params)
        yield response.text

if __name__ == '__main__':
    responses = main()
    for response in responses:
        print(response)

