import requests
from bs4 import BeautifulSoup as BS
import time



all_animals = []
h3 = "А"

def litter_count(all_animals):                             # создаю функцию которая будет считать количество имен для каждой буквы
    with open("Litter_count.txt", "w") as l:               # для наглядности создаю текстовый файл и открываю его для записи
        dict_litter = {}                                   # внутри файла создаю словарь
        for litter in "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ":     # для каждой буквы русского алфавита создаю цикл с щетчиком
            count = 0
            for element in all_animals:                    # в списке всех животных прохожу по каждому имени
                if element[0] == litter:                   # если имя начинается на букву цикла, то увеличиваю счётчик для этой буквы
                    count += 1
                    dict_litter[litter] = count            # добавляю в словарь "litter": count
            l.write("%s: %i\n" % (litter, count))          # записываю тоже самое в тестовый файл
    return print(dict_litter)                              # для проверки в терминале вызываю функцию print


def get_content(url):                                      # создаю функцию для получения названий животных с википедии
    with open("Animals_name.txt", "w") as f:               # для наглядности создаю тестовый файл со всеми животными
        global all_animals                                 # чтобы изменять глобальный список объявляю его в функции
        header = {                                         # не был уверен, что википедия не будет банить запросы, и для этого делаю запросы от рельного браузера
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"    
                }
        page = requests.get(url, headers=header)
        if page.status_code == 200:                                    # чтобы получить всех животных и исключить утерю каких либо проверяю на статус страницы
            page = requests.get(url, headers=header).text              # получаю страницы в тексте, чтобы применять парсинг
            h3 = "А"                                                   # создаю переменную для начальной точки поиска в заголовке h3
            while h3 != "A":                                           # создаю цикл с ограничением пока h3 не равно английской A повторять цикл, чтобы исключить      
                if h3 in "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ":              # английские названия животных, и далше для каждой буквы русского алфавита проверяю на вхождение заголовка h3
                    soup = BS(page, 'lxml')                                     # текст страницы
                    div_id = soup.find("div", id="mw-pages")                    # поиск нужного блока
                    div_class = div_id.find("div", class_="mw-category-group")  # поиск дива с названиями животных и h3
                    h3 = div_class.find("h3").text                              # нахождения текста в заголовке h3
                    li_all = div_class.find_all("li")                           # нахожу названия всех животных 
                    links = soup.find('div', id='mw-pages').find_all('a')       # нахожу ссылку на следующую странцу
                    for name in li_all:                                         # создаю цикл для названий животных в списке всех значений li
                        all_animals.append(name.text)                           # добавляю в список всех животных
                        f.write("%s\n" % name.text)                             # записываю их в файл All_animals.txt
                        time.sleep(0.001)                                       # команда для создания задержки, чтобы не нагружать сервера википеди, 
                    for a in links:                                             # хотел больше, но получается слишком долгий цикл
                        if a.text == 'Следующая страница' and a.text != "Предыдущая страница":      # создаю цикл для перехода по страницам с исключениями,
                            url = 'https://ru.wikipedia.org/' + a.get('href')                       # была проблема, что в конце цикл не завершался изза перепрыгивания
                            page = requests.get(url).text                                           # по ссылкам. Для каждого элемента "а" нахожу нужную ссылку

                
    return litter_count(all_animals)                                            # возвращаю вызов функции подчёта названий животных со списком


print(get_content("https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"))

# парсингом занимался впервые, было сложно, но мне понравилось. Спасибо за предоставленную возможность, если можно, то хотелось бы получить комментарий
# по проделанной работе, и что можно было реализовать лучше. Спасибо!