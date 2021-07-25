from lxml import etree
import requests

from spider.rule.base import Engine as BaseEngine


class Engine(BaseEngine):
    def __init__(self):
        super().__init__()

    @staticmethod
    def get_context(content):
        html = etree.HTML(content)
        context = html.xpath("//div[@id='content']")
        return context


if __name__ == "__main__":
    eg = Engine()
    url = "https://www.biquwx.la/104_104845/"
    content = eg.fetch(url)
    ret = eg.get_chapter(content)
    print(ret)
    content = eg.fetch(url + ret[0][0])
    print(eg.get_context(content))
