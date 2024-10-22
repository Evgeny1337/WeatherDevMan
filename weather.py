import requests

def main():
    params = {'n':'','T':'','q':'','M':'','lang':'ru'}
    places = ['Череповец', 'svo', 'Лондон']
    for place in places:
        url = f'http://wttr.in/{place}'
        try:
            response = requests.get(url=url,params=params)
            response.raise_for_status()
            print(response.text)
        except requests.exceptions.HTTPError as err:
            print('Response is: {content}'.format(content=err.response.text))

            
if __name__ == '__main__':
    main()

