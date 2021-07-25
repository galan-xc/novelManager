import requests
from lxml import etree
import time
class Engine:
    def __init__(self):
        self.Header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        }

    def fetch(self, url):
        print(url)
        time.sleep(8)
        rsp = requests.get(url, headers=self.Header)
        return rsp.content

    @staticmethod
    def get_chapter(content):
        html = etree.HTML(content)
        items = html.xpath("//dd/a")
        return [
            (i.get("href").strip(),
             i.get("title").strip(),
             ) for i in items]

