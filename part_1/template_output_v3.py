import requests

host = 'http://wttr.dvmn.org'
language = "ru"


def input_data():
    # Города для отображения
    location = {'London': "Лондон",
                'svo': "Шереметьево",
                'Cherepovets': "Череповец"
                }
    # Словарь доступных параметров запроса
    parameters = {'1': "0",  # только текущая погода
                  '2': "1",  # погода сегодня + 1 день
                  '3': "2",  # погода сегодня + 2 дня
                  '4': "n",  # узкая версия (только день и ночь)
                  '5': "q",  # тихая версия (без текста "Прогноз погоды")
                  '6': "Q",  # сверхтихая версия (без "Прогноз погоды", нет названия города)
                  '7': "T",  # отключить терминальные последовательности (без цветов)
                  '8': "M",  # показывать скорость ветра в м/с
                  '9': "m",  # метрические (СИ) (используются везде кроме США)
                  '10': "u"  # USCS (используются в США)
                  }
    # Выбирать значения по ключам из parameters{}
    selectParam = {"3", "4", "5", "7"}
    weather_output(location, parameters, selectParam)


def weather_output(location, parameters, selectParam):
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


input_data()