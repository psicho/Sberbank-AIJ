import requests
import selenium
# from xml.etree import ElementTree
# from googleapiclient import sample_tools
# from oauth2client import client
# import time
# import sys
# import json
from lxml import html
import re


# Формируем массив ссылок для парсинга выбранной категории
# http://ege.fipi.ru/os11/xmodules/qprint/index.php?proj_guid=AF0ED3F2557F8FFC4C06F80B6803FD26&theme_guid=aa5e3a609541e311a2f5001fc68344c9&groupno=1&groupno=2
def parseLinkArticles(startLink='http://ege.fipi.ru/os11/xmodules/qprint/index.php?theme_guid=aa5e3a609541e311a2f5001fc68344c9&proj_guid=AF0ED3F2557F8FFC4C06F80B6803FD26&groupno=', pages=1000000):
    tests = []
    # for page in range(0, pages + 1):
    for page in range(1, 2):
        try:
            link = startLink + str(page)
            print(link)

            # response = requests.get(link)
            # print('responce', response)
            # # pages = html.fromstring(response.text)
            # pages = html.fromstring(response.content)

            page = requests.get(link)
            print('page.content', page.content)
            pages = html.fromstring(page.content)

            # str1 = '//*[contains(@class, "question-hyperlink")]/@href'  # '//div[2]/h2/a/@href'
            for test in range(2, 12):
                str1 = '/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[' + str(test) + ']/tbody/tr/td/table[1]/tbody/tr//td'
                # str1 = '//*[@id="checkform"]/table/tbody/tr[1]/td/p/i'
                # str1 = '/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[3]/tbody/tr/td/table[1]/tbody/tr/td'
                print(test, str1)

                news_text = pages.xpath(str1)
                print('pages', pages)
                print('news_text', news_text)
                # news_text = news_text[:-1]

                tests.append(news_text)
                # print(news_text)

                # for i in range(len(news_text)):
                #     news_text[i] = 'https://ru.stackoverflow.com' + news_text[i]


            # if len(news_text) < 1:
            #     break

            # print(news_text)
            # print(len(news_text))

            # newses.extend(news_text.copy())
            # news_text = []
            # print('Страница: ', page, 'Ссылок', len(tests))

        except:
            print('Error')
            break
    #
    # print('Массив ссылок: ', newses)
    # json.dump(newses, open("newses_Coding.json", "w"))
    # print('Количество ссылок: ', len(newses))
    # print('Парсинг адресов страниц закончен')
    # # time.sleep(100)

parseLinkArticles()