import requests
import bs4


class Scraping:

    def __init__(self):
        self.__html = None

    def getHtml(self, targetUrl):
        response = requests.get(targetUrl)
        self.__html = bs4.BeautifulSoup(response.text, "html.parser")
        return self.__html

    def getHtmlOfSpecifyClass(self, targetClass):
        return self.__html.select(targetClass)
