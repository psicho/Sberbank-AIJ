import requests
# import selenium

from selenium import webdriver
import time
from fake_useragent import UserAgent
from lxml import html

def test_selenium():
    from selenium import webdriver

    # Драйвер FireFox
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36")
    driver = webdriver.Firefox(profile)

    # # Driver Chrome
    # from selenium.webdriver.chrome.options import Options
    # opts = Options()
    # opts.add_argument("user-agent=whatever you want")
    # driver = webdriver.Chrome(chrome_options=opts)

    try:

        driver.get("http://fipi.ru/")
        driver.get("http://www.fipi.ru/content/otkrytyy-bank-zadaniy-ege")
        button = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div[3]/div/div[2]/div/div/div/div/div/div/div/table/tbody/tr[2]/td[1]/p[1]/a/span/strong')
        button.click()
        # driver.get("http://www.fipi.ru/content/otkrytyy-bank-zadaniy-ege")
        time.sleep(1)
        # driver.get("http://ege.fipi.ru/os11/xmodules/qprint/index.php?theme_guid=aa5e3a609541e311a2f5001fc68344c9&proj_guid=AF0ED3F2557F8FFC4C06F80B6803FD26&groupno=0")
        time.sleep(3)

        # driver.switch_to.default_content()

        driver.switch_to.window(driver.window_handles[len(driver.window_handles) - 1])
        # driver.switch_to.window(driver.current_window_handle)

        driver.get("http://ege.fipi.ru/os11/xmodules/qprint/index.php?theme_guid=aa5e3a609541e311a2f5001fc68344c9&proj_guid=AF0ED3F2557F8FFC4C06F80B6803FD26&groupno=0")
        time.sleep(3)

        button = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[1]/div/div[2]/a')
        button.click()
        time.sleep(3)

        # driver.get("https://selenium-python.readthedocs.io/locating-elements.html")
        # assert "Python" in driver.title
        # text = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[0]/tbody/tr/td/table[1]/tbody/tr//td")
        text = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr/td/table[1]/tbody/tr/td/form[1]/table/tbody/tr[1]/td/p/i")
        # text = driver.find_element_by_xpath('//*[@id="locating-by-xpath"]/ol[1]/li[2]/text()')
        # elem = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[0]/tbody/tr/td/table[1]/tbody/tr//td')
        print(text.text)
    except:
        pass

    # driver.close()

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

# parseLinkArticles()
test_selenium()