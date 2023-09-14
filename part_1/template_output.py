import requests

host = 'http://wttr.dvmn.org'
location = {'London': "Лондон", 
            'svo': "Шереметьево", 
            'Cherepovets': "Череповец"
            }
language = "ru"
parameters = {'1': "0", 
              '2': "1", 
              '3': "2", 
              '4': "n", 
              '5': "q", 
              '6': "Q", 
              '7': "T"
              }
allParam = {"3", "4", "5", "7"}
paramInURL = '?'
for i in allParam:
    paramInURL += parameters.setdefault(i, '')
for i in location:
    get_template = '/{}{}&lang={}'
    url = host + get_template.format(i, paramInURL, language)
    response = requests.get(url)
    if response.ok:
        result = response.text
        print(result.replace(i, location.setdefault(i, ''), 1))