from lxml import etree
import requests

from spider.rule.base import Engine as BaseEngine

class Engine(BaseEngine):

    @staticmethod
    def get_chapter(content):
        html = etree.HTML(content)
        items = html.xpath("//dd/a")
        return [
            (i.get("href").strip(),
             i.get("title").strip(),
             ) for i in items]


if __name__ == "__main__":
    eg = Engine()
    content = eg.fetch("https://www.biquwx.la/104_104845/")