import requests

host = 'http://wttr.dvmn.org'
language = "ru"
location = {'London': "Лондон",
            'svo': "Шереметьево",
            'Cherepovets': "Череповец"
            }
parameters = {'1': "0",
              '2': "1",
              '3': "2",
              '4': "n",
              '5': "q",
              '6': "Q",
              '7': "T",
              '8': "M",
              '9': "m",
              '10': "u"
              }
selectParam = {"3", "4", "5", "7"}
keysForParam = []
for i in selectParam:
    keysForParam.append(parameters.setdefault(i, ''))
paramInURL = dict.fromkeys(keysForParam, '')
paramInURL['lang'] = language
for i in location:
    get_template = '/{}'
    url = host + get_template.format(i)
    response = requests.get(url, params=paramInURL)
    response.raise_for_status()
    if response.ok:
        result = response.text
        print(result.replace(i, location.setdefault(i, ''), 1))
