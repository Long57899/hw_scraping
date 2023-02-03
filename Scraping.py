import requests
import json

def getPage(page=0):

    params = {
        'text': 'NAME:Python',
        'area': [1,2],
        'description': ['Django','Flask'],
        'page': page,
        'per_page': 10
    }

    response = requests.get('https://api.hh.ru/vacancies', params)
    data = response.json()
    response.close()
    return data

result = getPage()['items']
list_vacancies = []

for vacancie in result:

    if vacancie['salary'] == None:
        salary = 'не указана'
    else:
        salary = {vacancie['salary']['from'] : vacancie['salary']['to']}

    if vacancie['employer']['name'] == None:
        employer = 'не указано'
    else:
        employer = vacancie['employer']['name']

    vacancie = [{'url':vacancie['alternate_url']}, {'вилка зп': salary}, {'Название организации': employer}, {'Город':vacancie['area']['name']}]
    list_vacancies.append(vacancie)

with open('python.json', 'w') as file:
    json.dump(list_vacancies,file)