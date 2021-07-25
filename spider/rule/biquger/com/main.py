from lxml import etree
import requests

from spider.rule.base import Engine as BaseEngine


class Engine(BaseEngine):
    def __init__(self):
        super().__init__()

    @staticmethod
    def get_context(content):
        html = etree.HTML(content)
        context = html.xpath("//div[@id='booktext']/text()")
        return "\n".join(x.strip().replace("\xa0", "") for x in context)


if __name__ == "__main__":
    eg = Engine()
    url = "https://www.biquger.com/biquge/134221/"
    content = eg.fetch(url)
    ret = eg.get_chapter(content)
    print(ret)
    content = eg.fetch(ret[0][0])
    print(eg.get_context(content))
