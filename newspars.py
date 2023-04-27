from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

async def epic():

    # ToDO проверка доступности файла на чтение и запись, если файл не читается, возврат сообщения проблемы с файлом
    f = open('files/newsid.txt', 'r+', encoding='utf-8')
    newsidlist = f.read().splitlines()
    print(f"В файле {len(newsidlist)} записей.")

    allnews = []

    #chrome_options = Options()
    #chrome_options.add_argument('--headless')
    #browser = webdriver.Chrome(options=chrome_options)
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
 
    # ToDO проверка доступности сайта, если статус не 200, но возврат сообщения что сайт недоступен
    try:
        browser.get("https://www.epicgames.com/fortnite/ru/news")
        html = browser.find_element(By.TAG_NAME, 'html')
        html.send_keys(Keys.PAGE_DOWN)

        blog = browser.find_element(By.CLASS_NAME, 'row')
        newscontent = blog.find_elements(By.TAG_NAME, 'a')

        try:
            for content in newscontent:
                nid = content.get_attribute('id')
                if nid not in newsidlist:
                    f.write(nid + '\n')
                    newstitle = content.get_attribute('title')
                    newslink = content.get_attribute('href')
                    newsimgclass = content.find_element(By.TAG_NAME, 'img')
                    newsimg = newsimgclass.get_attribute('src')
                    datenews = content.find_element(By.CLASS_NAME, 'date')
                    news = (datenews.text, newstitle, newslink, newsimg)
                    allnews.append(news)
            print(f"Получен список новостей в количестве {len(allnews)}")

        except Exception:
            print(f"Ошибка парсинга")

        browser.close()
        f.close()
        return allnews
    except Exception:
        print(f"Сайт недоступен")
